from mvimp_utils.location import *
import torch
import os
from mvimp_utils.file_op_helper import file_transfer, clean_folder
import shutil
import argparse


def config():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--fps", "-f", type=int, default=40, help="FPS of the output videos.",
    )
    parser.add_argument(
        "--frames",
        "-n",
        type=int,
        default=240,
        help="Frame number of the output videos.",
    )
    parser.add_argument(
        "--longer_side_len",
        "-l",
        type=int,
        default=960,
        help="Longer side of the output videos.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    os.chdir(Photo_3D)
    print(f"Current PyTorch version is {torch.__version__}")

    # receive new configuration
    args = config()
    print(
        f"Current configuration is :\n"
        f"fps: {args.fps} \n"
        f"num_frames: {args.frames} \n"
        f"longer_side_len: {args.longer_side_len}"
    )

    # rewrite new configuration
    ori_cfg_file = os.path.join(Photo_3D, "argument.yml")
    curr_cfg_file = os.path.join(Photo_3D, "curr_argument.yml")
    shutil.copy(ori_cfg_file, curr_cfg_file)
    os.system(f"sed -i 's/fps: 40/fps: {args.fps}/g' curr_argument.yml")
    os.system(
        f"sed -i 's/num_frames: 240/num_frames: {args.frames}/g' curr_argument.yml"
    )
    os.system(
        f"sed -i 's/longer_side_len: 960/longer_side_len: {args.longer_side_len}/g' curr_argument.yml"
    )

    # start processing
    file_list = os.listdir(input_data_dir)
    actual_input_dir = os.path.join(Photo_3D, "image")
    actual_output_dir = os.path.join(Photo_3D, "video")

    for i in range(len(file_list)):
        # transfer inputs
        shutil.copy(
            src=os.path.join(input_data_dir, file_list[i]), dst=actual_input_dir
        )
        # file_transfer(
        #     src=os.path.join(input_data_dir, file_list[i]), dst=actual_input_dir
        # )
        # inference
        os.system("python3 main.py --config curr_argument.yml")
        # transfer outputs
        file_transfer(src=actual_output_dir, dst=output_data_dir)
        # clean cache
        clean_folder(actual_input_dir)
        clean_folder(actual_output_dir)

    # clean input
    clean_folder(input_data_dir)
    os.remove(curr_cfg_file)
