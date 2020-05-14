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


def config():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--artistic",
        "-art",
        default=True,
        type=bool,
        help="Artistic model achieves the highest quality results in image coloration, "
        "in terms of interesting details and vibrance."
        "Stable model achieves the best results with landscapes and portraits.",
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
        default=False,
        type=bool,
        help="I respect the spirit of the original author adding a watermark to distinguish AI works, "
        "but setting it to False is more convenient for use in a production environment.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = config()

    if args.artistic:
        colorizer = get_artistic_image_colorizer(root_folder=Path(DeOldify))
    else:
        colorizer = get_stable_image_colorizer(root_folder=Path(DeOldify))

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
