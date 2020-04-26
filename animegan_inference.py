import os
import sys
import tensorflow as tf
import shutil


def file_transfer(src, dst):
    file_list = os.listdir(src)
    for i in range(len(file_list)):
        shutil.copy(os.path.join(src, file_list[i]), dst)

    shutil.rmtree(src)


def main(argv):
    default_style_name = ""
    if len(argv) == 1:
        default_style_name = "H"

    else:
        if argv[1] in ["S", "H"]:
            default_style_name = argv[1]
        else:
            raise ValueError(f"{argv[1]} is not a correct style name")

    os.system(
        f"CUDA_VISIBLE_DEVICES=0 python3 test.py "
        f"--checkpoint_dir {checkpoint_dir} "
        f"--test_dir {input_data_dir} "
        f"--style_name {default_style_name}"
    )

    ori_output_data_dir = os.path.join(ANIMEGAN_PREFIX, "results/" + default_style_name)
    file_transfer(src=ori_output_data_dir, dst=output_data_dir)


if __name__ == "__main__":
    LOC = os.getcwd()
    if LOC.split("/")[-1] != "MVIMP":
        raise ValueError("Please change directory to the root of MVIMP.")
    ANIMEGAN_PREFIX = os.path.join(LOC, "AnimeGAN")
    os.chdir(ANIMEGAN_PREFIX)

    print(f"Current TensorFlow version is {tf.__version__}")

    checkpoint_dir = "checkpoint/AnimeGAN_Hayao_lsgan_300_300_1_3_10"
    input_data_dir = os.path.join(LOC, "Data/Input")
    output_data_dir = os.path.join(LOC, "Data/Output")

    main(sys.argv)
