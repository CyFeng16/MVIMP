"""
It's a helper for video continues frames insertion.

Input: A series of frames(images);
Output: A series of frames(images).
"""

import os

from torch.autograd import Variable
import torch
import numpy as np
import numpy
from networks import DAIN_slowmotion
from my_args import args
import shutil
from tqdm import tqdm
import cv2


def continue_frames_insertion_helper(input_dir: str, output_dir: str, time_step: float):
    """For continue insert operation into curr input dir."""

    # curr_input_dir = os.path.join(INPUT_DATA, input_dir)
    print(f"************** current handling frame from {input_dir}. **************")
    print(f"************** current time_step is {time_step} **************")
    print(f"************** current output_dir is {output_dir} **************")
    print(
        f"************** high resolution method{' ' if args.high_resolution else ' not '}used. **************"
    )

    # curr all_frame is out of order.
    all_frames = os.listdir(input_dir)
    # all_frames.sort(key=lambda x: int(x[:-4]))
    # Todo(C.Feng, Mar 30): More precise string processing.
    all_frames.sort()
    frames_num = len(all_frames)
    for num in tqdm(range(frames_num - 1)):
        begin_frame = os.path.join(input_dir, f"{all_frames[num]}")
        end_frame = os.path.join(input_dir, f"{all_frames[num+1]}")
        frames_insertion_helper(
            output_dir=output_dir,
            begin_frame=begin_frame,
            end_frame=end_frame,
            time_step=time_step,
        )

    # handle the last frame.
    shutil.copy(
        os.path.join(input_dir, f"{all_frames[-1]}"),
        os.path.join(output_dir, f"{all_frames[-1].split('.')[0]}00.png"),
    )


def frames_insertion_helper(
    output_dir: str, begin_frame: str, end_frame: str, time_step: float
):
    """For insert operation between two frames."""

    # First, we copy the beginning frame into output dir.
    shutil.copy(
        begin_frame,
        os.path.join(
            output_dir, f"{os.path.split(begin_frame)[-1].split('.')[0]}00.png"
        ),
    )

    im_0 = cv2.imread(begin_frame)
    im_1 = cv2.imread(end_frame)
    h, w, c = im_0.shape
    assert im_0.shape == im_1.shape

    im_0 = np.transpose(im_0, (2, 0, 1)).astype("float32") / 255.0
    im_1 = np.transpose(im_1, (2, 0, 1)).astype("float32") / 255.0

    if not args.high_resolution:
        y_0 = model_inference_helper(im_0, im_1)
    else:
        frames_num = int(1.0 / time_step) - 1
        y_0 = []
        ym_0_0 = model_inference_helper(im_0[:, 0::2, 0::2], im_1[:, 0::2, 0::2])
        ym_0_1 = model_inference_helper(im_0[:, 0::2, 1::2], im_1[:, 0::2, 1::2])
        ym_1_0 = model_inference_helper(im_0[:, 1::2, 0::2], im_1[:, 1::2, 0::2])
        ym_1_1 = model_inference_helper(im_0[:, 1::2, 1::2], im_1[:, 1::2, 1::2])
        for i in range(frames_num):
            y_0.append(np.zeros(shape=(h, w, c)))
            y_0[-1][0::2, 0::2, :] = ym_0_0[i]
            y_0[-1][0::2, 1::2, :] = ym_0_1[i]
            y_0[-1][1::2, 0::2, :] = ym_1_0[i]
            y_0[-1][1::2, 1::2, :] = ym_1_1[i]

        del ym_0_0, ym_0_1, ym_1_0, ym_1_1

    for i, item in enumerate(y_0):
        curr_output_tail = (
            f"{os.path.split(begin_frame)[-1].split('.')[0]}{i+1:02d}.png"
        )
        cv2.imwrite(
            os.path.join(output_dir, curr_output_tail),
            np.round(item).astype(numpy.uint8),
        )

    del y_0


def model_inference_helper(x_0: np.array, x_1: np.array):
    """ Input: x_0, x_1; Output: y_0 """
    x_0 = torch.from_numpy(x_0).type(args.dtype)
    x_1 = torch.from_numpy(x_1).type(args.dtype)
    y_0 = torch.FloatTensor()

    intWidth = x_0.size(2)
    intHeight = x_0.size(1)
    channel = x_0.size(0)
    assert channel == 3, "input frame's channel is not equal to 3."

    if intWidth != ((intWidth >> 7) << 7):
        intWidth_pad = ((intWidth >> 7) + 1) << 7  # more than necessary
        intPaddingLeft = int((intWidth_pad - intWidth) / 2)
        intPaddingRight = intWidth_pad - intWidth - intPaddingLeft
    else:
        intWidth_pad = intWidth
        intPaddingLeft = 32
        intPaddingRight = 32

    if intHeight != ((intHeight >> 7) << 7):
        intHeight_pad = ((intHeight >> 7) + 1) << 7  # more than necessary
        intPaddingTop = int((intHeight_pad - intHeight) / 2)
        intPaddingBottom = intHeight_pad - intHeight - intPaddingTop
    else:
        intHeight_pad = intHeight
        intPaddingTop = 32
        intPaddingBottom = 32

    # torch.set_grad_enabled(False)
    x_0 = Variable(torch.unsqueeze(x_0, 0))
    x_1 = Variable(torch.unsqueeze(x_1, 0))
    x_0 = torch.nn.ReplicationPad2d(
        [intPaddingLeft, intPaddingRight, intPaddingTop, intPaddingBottom]
    )(x_0)
    x_1 = torch.nn.ReplicationPad2d(
        [intPaddingLeft, intPaddingRight, intPaddingTop, intPaddingBottom]
    )(x_1)

    # if use_cuda:
    x_0 = x_0.cuda()
    x_1 = x_1.cuda()

    # y_s, offset, filter = model(torch.stack((X0, X1), dim=0))
    y_s, _, _ = model(torch.stack((x_0, x_1), dim=0))
    y_0 = y_s[args.save_which]

    if not isinstance(y_0, list):
        y_0 = y_0.data.cpu().numpy()
    else:
        y_0 = [item.data.cpu().numpy() for item in y_0]
    y_0 = [
        np.transpose(
            255.0
            * item.clip(0, 1.0)[
                0,
                :,
                intPaddingTop : intPaddingTop + intHeight,
                intPaddingLeft : intPaddingLeft + intWidth,
            ],
            (1, 2, 0),
        )
        for item in y_0
    ]

    return y_0


if __name__ == "__main__":
    model = DAIN_slowmotion(
        channel=args.channels,
        filter_size=args.filter_size,
        timestep=args.time_step,
        training=False,
    )
    model = model.cuda()

    # load weight
    if os.path.exists(args.SAVED_MODEL):
        print("The model weight is: " + args.SAVED_MODEL)
        pretrained_dict = torch.load(args.SAVED_MODEL)

        model_dict = model.state_dict()
        # 1. filter out unnecessary keys
        pretrained_dict = {k: v for k, v in pretrained_dict.items() if k in model_dict}
        # 2. overwrite entries in the existing state dict
        model_dict.update(pretrained_dict)
        # 3. load the new state dict
        model.load_state_dict(model_dict)
        # 4. release the pretrained dict for saving memory
        pretrained_dict = []
    else:
        raise FileNotFoundError("We don't load any trained weights.")
    model = model.eval()  # deploy mode

    # model inference
    with torch.no_grad():
        continue_frames_insertion_helper(
            input_dir=args.src, output_dir=args.dst, time_step=args.time_step,
        )
