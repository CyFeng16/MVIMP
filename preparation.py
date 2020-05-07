import shutil
from mvimp_utils.location import *
import argparse


def config():
    parser = argparse.ArgumentParser(description="MVIMP configuration.")
    parser.add_argument(
        "--function", "-f", type=str, help="Function or functions your wanna prepare.",
    )
    return parser.parse_args()


def storage_preparation():
    if not os.path.exists(input_data_dir):
        os.makedirs(input_data_dir)
    if not os.path.exists(output_data_dir):
        os.makedirs(output_data_dir)


def anime_preparation():
    os.chdir(ANIMEGAN_PREFIX)

    pretrain_model_url = (
        "https://github.com/TachibanaYoshino/AnimeGAN/"
        "releases/download/Haoyao-style_V1.0/Haoyao-style.zip"
    )
    pretrain_model_dir = "./checkpoint"
    pretrain_model_file = os.path.join(pretrain_model_dir, "Haoyao-style.zip")

    vgg_url = "https://github.com/TachibanaYoshino/AnimeGAN/releases/download/vgg16%2F19.npy/vgg19.npy"
    vgg_dir = "./vgg19_weight"
    vgg_file = os.path.join(vgg_dir, "vgg19.npy")

    os.makedirs(pretrain_model_dir, exist_ok=True)
    os.makedirs(vgg_dir, exist_ok=True)

    os.system(f"wget -N {pretrain_model_url} -O {pretrain_model_file}")
    os.system(f"unzip {pretrain_model_file} -d {pretrain_model_dir}")
    os.system(f"wget {vgg_url} -O {vgg_file}")

    os.system(f"rm {pretrain_model_file}")


def dain_preparation():
    os.chdir(DAIN_PREFIX)

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
    images_dir = os.path.join(Photo_3D, "image")
    videos_dir = os.path.join(Photo_3D, "video")
    os.makedirs(checkpoints_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)
    os.makedirs(videos_dir, exist_ok=True)

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

    os.system(f"pip install -r requirements.txt")


if __name__ == "__main__":
    args = config()
    storage_preparation()
    if not args.function:
        raise ValueError("Please select correct function to prepare.")
    elif args.function == "animegan":
        anime_preparation()
    elif args.function == "dain":
        dain_preparation()
    elif args.function == "photo3d":
        photo_inpainting_3d_preparation()
    elif args.function == "all":
        anime_preparation()
        dain_preparation()
        photo_inpainting_3d_preparation()
