import sys
import tensorflow as tf
from file_op_helper import file_transfer, clean_folder
from location import *


def main(argv):
    if len(argv) == 1:
        default_style_name = "H"
    else:
        if argv[1] in ["S", "H"]:
            default_style_name = argv[1]
        else:
            raise ValueError(f"{argv[1]} is not a correct style name")

    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    os.environ["TF_ENABLE_GPU_GARBAGE_COLLECTION"] = "true"
    os.system(
        f"python3 test.py "
        f"--checkpoint_dir {checkpoint_dir} "
        f"--test_dir {input_data_dir} "
        f"--style_name {default_style_name}"
    )

    ori_output_data_dir = os.path.join(ANIMEGAN_PREFIX, "results/" + default_style_name)
    file_transfer(src=ori_output_data_dir, dst=output_data_dir)
    clean_folder(input_data_dir)


if __name__ == "__main__":
    os.chdir(ANIMEGAN_PREFIX)
    print(f"Current TensorFlow version is {tf.__version__}")
    checkpoint_dir = "checkpoint/AnimeGAN_Hayao_lsgan_300_300_1_3_10"
    main(sys.argv)
