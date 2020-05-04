import sys
import shutil
from location import *


def storage_preparation():
    if not os.path.exists(input_data_dir):
        os.makedirs(input_data_dir)
    if not os.path.exists(output_data_dir):
        os.makedirs(output_data_dir)


def anime_preparation():
    os.chdir(ANIMEGAN_PREFIX)
    pretrain_model_url = "https://github.com/TachibanaYoshino/AnimeGAN/releases/download/Haoyao-style_V1.0/Haoyao-style.zip"
    pretrain_model_file = "./checkpoint/Haoyao-style.zip"
    pretrain_model_dir = "./checkpoint/AnimeGAN_Hayao_lsgan_300_300_1_3_10"
    vgg_url = "https://github.com/TachibanaYoshino/AnimeGAN/releases/download/vgg16%2F19.npy/vgg19.npy"
    vgg_dir = "./vgg19_weight"
    vgg_file = os.path.join(vgg_dir, "vgg19.npy")

    os.system(f"rm -rf {pretrain_model_dir}")
    os.system(f"rm -rf {vgg_dir}")

    os.makedirs(f"{pretrain_model_dir}")
    os.makedirs(f"{vgg_dir}")

    os.system(f"wget -N {pretrain_model_url} -O {pretrain_model_file}")
    os.system(f"unzip {pretrain_model_file} -d {pretrain_model_dir}")
    os.system(f"wget {vgg_url} -O {vgg_file}")

    os.system(f"rm {pretrain_model_file}")


def dain_preparation():
    my_package_dir = os.path.join(DAIN_PREFIX, "my_package")
    nvidia_pwcnet_dir = os.path.join(
        DAIN_PREFIX, "PWCNet/correlation_package_pytorch1_0"
    )
    model_weights_dir = os.path.join(DAIN_PREFIX, "model_weights")

    os.chdir(my_package_dir)
    os.system(f"sh {os.path.join(my_package_dir, 'build.sh')}")
    os.chdir(nvidia_pwcnet_dir)
    os.system(f"sh {os.path.join(nvidia_pwcnet_dir, 'build.sh')}")

    os.makedirs(model_weights_dir)
    os.chdir(model_weights_dir)
    os.system("wget http://vllab1.ucmerced.edu/~wenbobao/DAIN/best.pth")

    os.system("pip install Pillow scipy==1.1.0")


def photo_inpainting_3d_preparation():
    os.chdir(Photo_3D)
    checkpoints_dir = os.path.join(Photo_3D, "checkpoints")
    os.makedirs(checkpoints_dir, exist_ok=True)
    model_weights = {
        "color-model": "https://filebox.ece.vt.edu/~jbhuang/project/3DPhoto/model/color-model.pth",
        "depth-model": "https://filebox.ece.vt.edu/~jbhuang/project/3DPhoto/model/depth-model.pth",
        "edge-model": "https://filebox.ece.vt.edu/~jbhuang/project/3DPhoto/model/edge-model.pth",
        "MiDaS-model": "https://filebox.ece.vt.edu/~jbhuang/project/3DPhoto/model/model.pt",
    }
    os.system(
        f"wget {model_weights['color-model']} "
        f"{model_weights['depth-model']} "
        f"{model_weights['edge-model']} "
        f"{model_weights['MiDaS-model']}"
    )
    shutil.move("color-model.pth", "checkpoints")
    shutil.move("depth-model.pth", "checkpoints")
    shutil.move("edge-model.pth", "checkpoints")
    shutil.move("model.pt", "MiDaS")

    os.system(f"pip install Cython decorator pyyaml")
    os.system(f"pip install -r requirements.txt")


def main(argv):
    if argv[1] == "animegan":
        anime_preparation()
    elif argv[1] == "dain":
        dain_preparation()
    elif argv[1] == "3dphoto":
        photo_inpainting_3d_preparation()
    elif argv[1] == "all":
        anime_preparation()
        dain_preparation()
        photo_inpainting_3d_preparation()
    else:
        raise ValueError("Please select correct function to prepare.")


if __name__ == "__main__":
    storage_preparation()
    main(sys.argv)
