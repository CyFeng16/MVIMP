import shutil
import tensorflow as tf
from mvimp_utils.file_op_helper import file_transfer, clean_folder
from mvimp_utils.location import *


if __name__ == "__main__":
    # switch to AnimeGAN folder
    os.chdir(ANIMEGAN_PREFIX)

    print(f"Current TensorFlow version is {tf.__version__}")
    checkpoint_dir = "./checkpoint"

    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    os.environ["TF_ENABLE_GPU_GARBAGE_COLLECTION"] = "true"
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
    os.system(
        f"python3 test.py "
        f"--checkpoint_dir {checkpoint_dir} "
        f"--test_dir {input_data_dir} "
        f"--style_name H"
    )

    ori_output_data_dir = os.path.join(ANIMEGAN_PREFIX, "results/H")
    file_transfer(src=ori_output_data_dir, dst=output_data_dir)

    # clean cache and input folders
    shutil.rmtree(os.path.join(ANIMEGAN_PREFIX, "results"))
    clean_folder(input_data_dir)
