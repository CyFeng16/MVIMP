"""
The basic function of DeOldify comes from https://deepai.org/machine-learning-model/colorizer

Todo(C.Feng, 20200511): Use original DeOldify instead of SaaS provided by DeepAI.
"""
from mvimp_utils.file_op_helper import clean_folder
from mvimp_utils.location import *
import requests
import os
from tqdm import tqdm
import argparse


def config():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--api_key",
        "-key",
        type=str,
        help="The API key of DeepAI, please sign up first.",
    )
    return parser.parse_args()


def deoldify_saas(src: str, key: str, dst: str) -> None:
    file_list = os.listdir(src)
    for file in tqdm(file_list):
        r = requests.post(
            "https://api.deepai.org/api/colorizer",
            files={"image": open(os.path.join(src, file), "rb"),},
            headers={"api-key": key},
        )
        r = r.json()
        output_url = r["output_url"]
        r = requests.get(output_url)
        with open(os.path.join(dst, file), "wb") as img:
            img.write(r.content)


if __name__ == "__main__":
    args = config()

    deoldify_saas(src=input_data_dir, key=args.api_key, dst=output_data_dir)
    print("Process completed.")
    clean_folder(input_data_dir)
