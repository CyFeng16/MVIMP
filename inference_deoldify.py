"""
The basic function of DeOldify comes from https://deepai.org/machine-learning-model/colorizer

Todo(C.Feng, 20200511): Use original DeOldify instead of SaaS provided by DeepAI.
"""
from pathlib import Path
from mvimp_utils.file_op_helper import clean_folder
from mvimp_utils.location import *
import os
from tqdm import tqdm
import argparse
from third_party.DeOldify.deoldify.visualize import get_image_colorizer
from third_party.DeOldify.deoldify.visualize import   get_artistic_image_colorizer


def config():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--artistic", "-art", default=True, type=bool, help=" ",  # TODO
    )
    parser.add_argument(
        "--render_factor", "-factor", default=35, type=int, help=" ",  # TODO
    )
    parser.add_argument(
        "--watermarked", "-mark", default=False, type=bool, help=" ",  # TODO
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = config()

    if args.artistic:
        colorizer = get_artistic_image_colorizer(
            root_folder=Path(DeOldify),
        )

    file_list = os.listdir(input_data_dir)
    for file in tqdm(file_list):
        colored_image = colorizer.get_transformed_image(
            path=Path(os.path.join(input_data_dir, file)),
            render_factor=args.render_factor,
            post_process=True,
            watermarked=args.watermarked,
        )
        colored_image.save(os.path.join(output_data_dir, file))
