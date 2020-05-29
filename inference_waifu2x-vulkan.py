from mvimp_utils.file_op_helper import clean_folder
from mvimp_utils.location import *
import os
import argparse
from tqdm import tqdm
from subprocess import run, DEVNULL


def config():
    parser = argparse.ArgumentParser(description="Inference waifu2x-ncnn-vulkan.")
    parser.add_argument(
        "--scale",
        "-s",
        type=int,
        default=2,
        choices=[1, 2],
        help="Scale image. 1 or 2. Default is 2",
    )
    parser.add_argument(
        "--noise",
        "-n",
        type=int,
        default=0,
        choices=[-1, 0, 1, 2, 3],
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
        type=str,
        default="cunet",
        choices=["cunet", "photo", "animeart"],
        help="Model to use. Default is cunet.",
    )
    parser.add_argument(
        "--tta",
        "-x",
        action="store_true",
        help="TTA mode able to reduce several types of artifacts but it's 8x slower than the non-TTA mode."
        "See https://github.com/nagadomi/waifu2x/issues/148#issuecomment-255754265 for details",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = config()

    build_dir = os.path.join(waifu2x_vulkan, "build")
    bin_dir = os.path.join(build_dir, "./waifu2x-ncnn-vulkan")

    assert 32 <= args.tilesize <= 19327352831, "Tile size is out of range!"
    model_version = {
        "cunet": "models-cunet",
        "photo": "models-upconv_7_photo",
        "animeart": "models-upconv_7_anime_style_art_rgb",
    }
    model_version = os.path.join(build_dir, model_version[args.model])

    print(
        f"\n--------------------CURR CFG--------------------\n"
        f"Current model version is {model_version},\n"
        f"Scale is set at {args.scale},\n"
        f"Noise reduction is set at {args.noise},\n"
        f"Tile size is set at {args.tilesize}.\n"
        f"TTA mode is {'on' if args.tta else 'off'}.\n"
        f"--------------------NOW END--------------------\n\n"
    )

    file_list = os.listdir(input_data_dir)
    for file in tqdm(file_list):
        input_file = os.path.join(input_data_dir, file)
        output_file = os.path.join(output_data_dir, f"{file.split('.')[0]}.png")
        cmd = f"{bin_dir} -i {input_file} -o {output_file} -m {model_version} -s {args.scale} -n {args.noise} -t {args.tilesize}"
        if args.tta:
            cmd = cmd + " -x"
        run(cmd, shell=True, stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL)

    clean_folder(input_data_dir)
