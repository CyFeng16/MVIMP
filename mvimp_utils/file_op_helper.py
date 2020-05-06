import os
import shutil


def file_transfer(src: str, dst: str) -> None:
    file_list = os.listdir(src)
    for i in range(len(file_list)):
        shutil.copy(os.path.join(src, file_list[i]), dst)
    # shutil.rmtree(src)


def file_order(src: str, dst: str) -> None:
    frames_list = sorted(os.listdir(src))
    for i in range(len(frames_list)):
        shutil.copy(
            os.path.join(src, frames_list[i]), os.path.join(dst, f"{i + 1:010d}.png"),
        )
        os.remove(os.path.join(src, frames_list[i]))


def clean_folder(src: str) -> None:
    if os.path.exists(src):
        shutil.rmtree(src)
    os.makedirs(src)
