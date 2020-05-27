from mvimp_utils.file_op_helper import clean_folder
from mvimp_utils.location import *
import os
import argparse
from tqdm import tqdm
from subprocess import run, DEVNULL


def config():
    parser = argparse.ArgumentParser(description="Inference waifu2x-ncnn-vulkan.")
    parser.add_argument(
        "--scale", "-s", default=2, type=int, help="Scale image. 1 or 2. Default is 2"
    )
    parser.add_argument(
        "--noise",
        "-n",
        default=0,
        type=int,
        help="Reduce the image noise. Between -1 and 3. Default is 0",
    )
    parser.add_argument(
        "--tilesize",
        "-t",
        default=400,
        type=int,
        help="Tile size. Between 32 and 19327352831. No appreciable effect. Default is 400",
    )
    parser.add_argument(
        "--model",
        "-m",
        default="cunet",
        type=str,
        help="Model to use. cunet (defaul) / photo / animeart",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = config()

    build_dir = os.path.join(waifu2x_vulkan, "build")
    bin_dir = os.path.join(build_dir, "./waifu2x-ncnn-vulkan")

    assert 1 <= args.scale <= 2, "Scale is out of range!"
    assert -1 <= args.noise <= 3, "Noise is out of range!"
    assert 32 <= args.tilesize <= 19327352831, "Tile size is out of range!"
    model_version = ""
    if args.model == "cunet":
        model_version = os.path.join(build_dir, "models-cunet")
    elif args.model == "photo":
        model_version = os.path.join(build_dir, "models-upconv_7_photo")
    elif args.model == "animeart":
        model_version = os.path.join(build_dir, "models-upconv_7_anime_style_art_rgb")
    else:
        print("Model not available")

    print(
        f"\n--------------------CURR CFG--------------------\n"
        f"Current model version is {model_version},\n"
        f"Scale is set at {args.scale},\n"
        f"Noise reduction is set at {args.noise},\n"
        f"Tile size is set at {args.tilesize}.\n"
        f"--------------------NOW END--------------------\n\n"
    )

    file_list = os.listdir(input_data_dir)
    for file in tqdm(file_list):
        input_file = os.path.join(input_data_dir, file)
        output_file = os.path.join(output_data_dir, file)
        cmd = f"{bin_dir} -i {input_file} -o {output_file} -m {model_version} -s {args.scale} -n {args.noise} -t {args.tilesize}"
        run(cmd, shell=True, stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL)

    clean_folder(input_data_dir)
