import os
import tensorflow as tf

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

    os.system(
        f"CUDA_VISIBLE_DEVICES=0 python3 test.py --checkpoint_dir {checkpoint_dir} --test_dir {input_data_dir} --style_name H"
    )
