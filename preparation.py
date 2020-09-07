import shutil
from mvimp_utils.location import *
import argparse

# version 0907
external_links = {
    # AnimeGANv1
    "animeganv1-pretrain-model": "https://www.dropbox.com/s/063uot56vfreeli/0907-Haoyao-style.zip",
    "animeganv1-vgg-weights": "https://www.dropbox.com/s/qkmlp88zbizz24b/0907-vgg19.npy",
    # DAIN
    "dain-best-model": "https://www.dropbox.com/s/yw7qw5ygrvixinc/0907-best.pth",
    # photo_inpainting_3d
    "3d-photo-inpainting-color-model": "https://www.dropbox.com/s/xncj03jiafx7yep/0907-color-model.pth",
    "3d-photo-inpainting-depth-model": "https://www.dropbox.com/s/3qymi6xpnoj7b28/0907-depth-model.pth",
    "3d-photo-inpainting-edge-model": "https://www.dropbox.com/s/5g9d4pkw8vgptim/0907-edge-model.pth",
    "3d-photo-inpainting-MiDaS-model": "https://www.dropbox.com/s/4njb4djtd86sk4z/0907-model.pt",
    # deoldify
    "deoldify-stable-model": "https://www.dropbox.com/s/mwjep3vyqk5mkjc/ColorizeStable_gen.pth",
    "deoldify-artistic-model": "https://www.dropbox.com/s/zkehq1uwahhbc2o/ColorizeArtistic_gen.pth",
    # waifu2x_vulkan_ncnn
    "waifu2x-vulkan-ncnn-setup": "https://www.dropbox.com/s/hnyj19i258915lx/0907-vulkansdk-linux-x86_64-1.2.135.0.tar.gz",
}


def downloader(link: str, name: str) -> None:
    os.system(f"wget {link} -O {name}")


def config():
    parser = argparse.ArgumentParser(description="MVIMP configuration.")
    parser.add_argument(
        "--function",
        "-f",
        type=str,
        help="Function or functions your wanna prepare.",
    )
    return parser.parse_args()


def animeganv1_preparation():
    os.chdir(ANIMEGAN_PREFIX)

    pretrain_model_dir = "./checkpoint"
    pretrain_model_file = os.path.join(pretrain_model_dir, "Haoyao-style.zip")

    vgg_dir = "./vgg19_weight"
    vgg_file = os.path.join(vgg_dir, "vgg19.npy")

    os.makedirs(pretrain_model_dir, exist_ok=True)
    os.makedirs(vgg_dir, exist_ok=True)

    downloader(external_links["animeganv1-pretrain-model"], pretrain_model_file)
    downloader(external_links["animeganv1-pretrain-model"], vgg_file)
    os.system(f"unzip {pretrain_model_file} -d {pretrain_model_dir}")
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
    downloader(external_links["dain-best-model"], "best.pth")


def photo_inpainting_3d_preparation():
    os.chdir(Photo_3D)

    checkpoints_dir = os.path.join(Photo_3D, "checkpoints")
    images_dir = os.path.join(Photo_3D, "image")
    videos_dir = os.path.join(Photo_3D, "video")
    os.makedirs(checkpoints_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)
    os.makedirs(videos_dir, exist_ok=True)

    downloader(external_links["3d-photo-inpainting-color-model"], "color-model.pth")
    downloader(external_links["3d-photo-inpainting-depth-model"], "depth-model.pth")
    downloader(external_links["3d-photo-inpainting-edge-model"], "edge-model.pth")
    downloader(external_links["3d-photo-inpainting-MiDaS-model"], "model.pt")

    shutil.move("color-model.pth", "checkpoints")
    shutil.move("depth-model.pth", "checkpoints")
    shutil.move("edge-model.pth", "checkpoints")
    shutil.move("model.pt", "MiDaS")

    os.system(f"pip install -r requirements.txt")


def deoldify_preparation():
    os.chdir(DeOldify)

    models_dir = os.path.join(DeOldify, "models")
    os.makedirs(models_dir, exist_ok=True)

    downloader(external_links["deoldify-stable-model"], "ColorizeStable_gen.pth")
    downloader(external_links["deoldify-artistic-model"], "ColorizeArtistic_gen.pth")

    shutil.move("ColorizeStable_gen.pth", "models")
    shutil.move("ColorizeArtistic_gen.pth", "models")

    os.system(f"pip install -r colab_requirements.txt")


def waifu2x_vulkan_ncnn_preparation():
    os.chdir(waifu2x_vulkan)

    build_dir = os.path.join(waifu2x_vulkan, "build")
    os.makedirs(build_dir, exist_ok=True)

    downloader(external_links["waifu2x-vulkan-ncnn-setup"], "vulkansdk.tar.gz")
    os.system("tar -xvf vulkansdk.tar.gz")
    os.rename("1.2.135.0", "vulkansdk")
    os.remove("vulkansdk.tar.gz")
    os.environ["VULKAN_SDK"] = os.path.join(waifu2x_vulkan, "vulkansdk/x86_64")
    os.environ["PATH"] += os.pathsep + "$VULKAN_SDK/bin"
    os.environ["LD_LIBRARY_PATH"] += os.pathsep + "$VULKAN_SDK/lib"
    os.environ["VK_LAYER_PATH"] = "$VULKAN_SDK/etc/vulkan/explicit_layer.d"

    os.chdir(build_dir)
    os.system("cmake ../src")
    os.system("cmake --build .")

    os.system("cp -r ../models/* .")


if __name__ == "__main__":
    args = config()
    if not args.function:
        print(
            f"Only create Data folder at {input_data_dir} and {output_data_dir}.\n"
            f"Make sure you have selected correct function to prepare."
        )
        # raise ValueError("Please select correct function to prepare.")
    elif args.function == "animegan":
        animeganv1_preparation()
    elif args.function == "dain":
        dain_preparation()
    elif args.function == "photo3d":
        photo_inpainting_3d_preparation()
    elif args.function == "deoldify":
        deoldify_preparation()
    elif args.function == "waifu2x-vulkan":
        waifu2x_vulkan_ncnn_preparation()
    elif args.function == "all":
        animeganv1_preparation()
        dain_preparation()
        photo_inpainting_3d_preparation()
        deoldify_preparation()
        waifu2x_vulkan_ncnn_preparation()
