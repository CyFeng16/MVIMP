import sys

sys.path.append("./3d-photo-inpainting")

from location import *
import torch
import os
import sys
from file_op_helper import file_transfer, clean_folder
import shutil


def main(argv):
    # receive new configuration
    cfgs = [40, 240, 960]
    if len(argv) > 1:
        for i, arg in enumerate(argv[1:]):
            cfgs[i] = arg
    fps, num_frames, longer_side_len = cfgs
    print(
        f"Current configuration is :\n"
        f"fps: {fps} \n"
        f"num_frames: {num_frames} \n"
        f"longer_side_len: {longer_side_len} \n"
    )
    cfg_file = os.path.join(Photo_3D, "argument.yml")
    curr_cfg_file = os.path.join(Photo_3D, "curr_argument.yml")
    shutil.copy(cfg_file, curr_cfg_file)
    os.system(f"sed -i 's/fps: 40/fps: {fps}/g' curr_argument.yml")
    os.system(
        f"sed -i 's/num_frames: 240/num_frames: {num_frames}/g' curr_argument.yml"
    )
    os.system(
        f"sed -i 's/longer_side_len: 960/longer_side_len: {longer_side_len}/g' curr_argument.yml"
    )

    # inference and transfer files
    actual_input_dir = os.path.join(Photo_3D, "image")
    actual_output_dir = os.path.join(Photo_3D, "video")
    file_transfer(src=input_data_dir, dst=actual_input_dir)
    clean_folder(input_data_dir)
    os.system("python3 main.py --config curr_argument.yml")
    file_transfer(src=actual_output_dir, dst=output_data_dir)
    clean_folder(output_data_dir)
    os.remove(curr_cfg_file)


if __name__ == "__main__":
    """
    argv[1]: fps
    argv[2]: num_frames
    argv[3]: longer_side_len
    """
    os.chdir(Photo_3D)
    print(f"Current PyTorch version is {torch.__version__}")
    main(sys.argv)
