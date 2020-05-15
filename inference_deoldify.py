"""Todo(C.Feng, 20200515): Video format"""

from pathlib import Path
from mvimp_utils.file_op_helper import clean_folder
from mvimp_utils.location import *
import shutil
import os
from tqdm import tqdm
import argparse
from third_party.DeOldify.deoldify.visualize import get_artistic_image_colorizer
from third_party.DeOldify.deoldify.visualize import get_stable_image_colorizer
import torch

torch.backends.cudnn.benchmark = True


def config():
    parser = argparse.ArgumentParser(description="Inference DeOldify.")
    parser.add_argument(
        "--artistic",
        "-art",
        action="store_true",
        help="Artistic model achieves the highest quality results in image coloration, "
        "in terms of interesting details and vibrance.",
    )
    parser.add_argument(
        "--stable",
        "-st",
        action="store_true",
        help="Stable model achieves the best results with landscapes and portraits.",
    )
    parser.add_argument(
        "--render_factor",
        "-factor",
        default=35,
        type=int,
        help="Between 7 and 40, try more times for better performance.",
    )
    parser.add_argument(
        "--watermarked",
        "-mark",
        action="store_true",
        help="I respect the spirit of the original author adding a watermark to distinguish AI works, "
        "but setting it to False is more convenient for use in a production environment.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    print(f"Current PyTorch version is {torch.__version__}")

    args = config()
    assert 7 <= args.render_factor <= 40, "Render factor out of range!"
    assert (args.artistic + args.stable) not in [
        0,
        2,
    ], "Please choose either artistic or stable version model."

    print(
        f"\n--------------------CURR CFG--------------------\n"
        f"Current model version is {'Artistic' if args.artistic else 'Stable'},\n"
        f"The render factor is set at {args.render_factor},\n"
        f"Watermark will{' ' if args.watermarked else ' not'} be added after processing.\n"
        f"--------------------NOW END--------------------\n\n"
    )

    model_version = None
    if args.artistic:
        model_version = get_artistic_image_colorizer
    if args.stable:
        model_version = get_stable_image_colorizer
    colorizer = model_version(root_folder=Path(DeOldify))

    file_list = os.listdir(input_data_dir)
    for file in tqdm(file_list):
        colored_image = colorizer.get_transformed_image(
            path=Path(os.path.join(input_data_dir, file)),
            render_factor=args.render_factor,
            post_process=True,
            watermarked=args.watermarked,
        )
        colored_image.save(os.path.join(output_data_dir, file))

    shutil.rmtree(os.path.join(LOC, "dummy"))
    shutil.rmtree(os.path.join(LOC, "result_images"))
    clean_folder(input_data_dir)
