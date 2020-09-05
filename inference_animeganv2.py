import shutil
import tensorflow as tf
from mvimp_utils.file_op_helper import file_transfer, clean_folder
from mvimp_utils.location import *
import argparse


def config():
    parser = argparse.ArgumentParser(description="Inference AnimeGANv2.")
    parser.add_argument(
        "--style",
        "-s",
        type=str,
        default='Hayao',
        choices=["Hayao", "Shinkai", "Paprika"],
        help="what style you want to get",
    )
    return parser.parse_args()


if __name__ == "__main__":
    # switch to AnimeGANv2 folder
    os.chdir(ANIMEGANv2_PREFIX)

    print(f"Current TensorFlow version is {tf.__version__}")
    args = config()
    generator_weights = {
        "Hayao": "./checkpoint/generator_Hayao_weight",
        "Shinkai": "./checkpoint/generator_Shinkai_weight",
        "Paprika": "./checkpoint/generator_Paprika_weight",
    }
    checkpoint_dir = generator_weights[args.style]

    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    os.environ["TF_ENABLE_GPU_GARBAGE_COLLECTION"] = "true"
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
    os.system(
        f"python3 test.py "
        f"--checkpoint_dir {checkpoint_dir} "
        f"--test_dir {input_data_dir} "
        f"--style_name inference"
    )

    ori_output_data_dir = os.path.join(ANIMEGANv2_PREFIX, "results/inference")
    file_transfer(src=ori_output_data_dir, dst=output_data_dir)

    # clean cache and input folders
    shutil.rmtree(os.path.join(ANIMEGANv2_PREFIX, "results"))
    clean_folder(input_data_dir)
