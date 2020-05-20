import cv2
import os


def fps_info(src: str) -> float:
    """video fps lookup"""
    video = cv2.VideoCapture(src)
    # Find OpenCV version
    major_ver, _, _ = cv2.__version__.split(".")
    if int(major_ver) < 3:
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    else:
        fps = video.get(cv2.CAP_PROP_FPS)
    video.release()

    return "%.2f" % fps


def frames_info(src: str) -> int:
    """video total frames lookup"""
    video = cv2.VideoCapture(src)
    frame_count = 0
    while True:
        ret, frame = video.read()
        if ret is False:
            break
        frame_count = frame_count + 1
    return frame_count


def video_extract(src: str, dst: str, thread: int) -> None:
    """pre-processing video to png"""
    cmd = (
        f"ffmpeg -hide_banner -loglevel warning "
        f"-threads {thread} "
        f"-i {src} "
        f"{dst}/%8d.png"
    )
    print(cmd)
    os.system(cmd)
    print("The video-image extracting job is done.")


def video_fusion(src: str, dst: str, fps: float, thread: int) -> None:
    """post-processing png to video"""
    cmd = (
        f"ffmpeg -hide_banner -loglevel warning "
        f"-threads {thread} "
        f"-r {fps} "
        f"-f image2 -i {src} "
        f"-y -c:v libx264 -preset slow -crf 8 {dst}"
    )
    print(cmd)
    os.system(cmd)
    print("The image-video fusion job is done.")
