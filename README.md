<p align="center">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/CyFeng16/MVIMP" />
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/CyFeng16/MVIMP" />
    <img alt="GitHub License" src="https://img.shields.io/github/license/cyfeng16/MVIMP" />
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg" />
</p>

English | [简体中文](docs/README_zh-Hans.md)

# MVIMP

**M**ixed **V**ideo and **I**mage **M**anipulation **P**rogram

I realize that training a good-performance AI model is kind of just one side of the story, make it easy to use for others is the other thing. So, this repository tries to embrace out-of-the-box AI ability to manipulate multimedia, also, I wish you have fun!

| Parallel |  Input | Output |        Parallel        |
|:--------:|:------:|:------:|:----------------------:|
| [AnimeGAN](https://github.com/CyFeng16/MVIMP#animegan) | Images | Images |          True          |
|   [DAIN](https://github.com/CyFeng16/MVIMP#dain)   |  Video |  Video |          False         |
|  [Photo3D](https://github.com/CyFeng16/MVIMP#photo3d) | Images | Videos | True(not recommmended) |
| [DeOldify](https://github.com/CyFeng16/MVIMP#deoldify) | Images | Images |          True          |

## AnimeGAN

Original repository: [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN)

This is the Open source of the paper <AnimeGAN: a novel lightweight GAN for photo animation>, which uses the GAN framwork to transform real-world photos into anime images.

|  Dependency  |               Version              |
|:------------:|:----------------------------------:|
|  TensorFLow  |               1.15.2               |
| CUDA Toolkit | 10.0(tested locally) / 10.1(colab) |
|    Python    |             3.6.8(3.6+)            |
|    opencv    |                  -                 |
|     tqdm     |                  -                 |
|     numpy    |                  -                 |
|     glob     |                  -                 |
|   argparse   |                  -                 |

**Usage**:

1. `Local`

    ```shell
    # Step 1: Prepare
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f animegan 
    # Step 2: Put your photos into ./Data/Input/
    # Step 3: Infernece
    python3 inference_animegan.py
    ```

2. `Colab`

    Or you can try following shared colab in playground mode:

    https://colab.research.google.com/drive/1bpwUFcr5i38_P3a0r3Qm9Dvkl-MS_Y1y?usp=sharing

## Photo3D

Original repository: [vt-vl-lab/3d-photo-inpainting](https://github.com/vt-vl-lab/3d-photo-inpainting)

The method for converting a single RGB-D input image into a 3D photo, i.e., a multi-layer representation for novel view synthesis that contains hallucinated color and depth structures in regions occluded in the original view. 

|  Dependency  |           Version          |
|:------------:|:--------------------------:|
|    PyTroch   |            1.5.0           |
| CUDA Toolkit | 10.1(tested locally/colab) |
|    Python    |         3.6.8(3.6+)        |

Other Python dependencies listed in `requirements.txt`, and will be auto installed while running `preparation.py`.

**Usage**:

1. `Local`

    ```shell
    # Step 1: Prepare
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f photo3d
    # Step 2: Put your photos into ./Data/Input/
    # Step 3: Infernece
    python3 inference_photo3d.py -f 40 -n 240 -l 960
    ```

2. `Colab`

    Or you can try following shared colab in playground mode:

    https://colab.research.google.com/drive/1VAFCN8Wh4DAY_HDcwI-miNIBomx_MZc5?usp=sharing

    P.S. Massive memory is occupied during operation(grows with `-l`). 
    
    `Higher memory` runtime helps if you are Colab Pro user.

3. Description of Parameters

    | params            | abbr. | Default | Description                                              |
    |-------------------|-------|---------|----------------------------------------------------------|
    | --fps             | -f    | 40      | The FPS of output video.                                 |
    | --frames          | -n    | 240     | The number of frames of output video.                    |
    | --longer_side_len | -l    | 960     | The longer side of output video(either height or width). |

## DAIN

Original repository: [baowenbo/DAIN](https://github.com/baowenbo/DAIN)

Depth-Aware video frame INterpolation (DAIN) model explicitly detect the occlusion by exploring the depth cue. We develop a depth-aware flow projection layer to synthesize intermediate flows that preferably sample closer objects than farther ones. 

|  Dependency  |                        Version                        |
|:------------:|:-----------------------------------------------------:|
|    PyTroch   |                         1.4.0                         |
| CUDA Toolkit |               10.0(tested locally/colab)              |
|    Python    |                      3.6.8(3.6+)                      |
|      GCC     | 7.5(Compiling PyTorch 1.4.0 extension files (.c/.cu)) |

P.S. Make sure your virtual env has torch-1.4.0+cu100 and torchvision-0.5.0+cu100.
You can use the following [command](https://github.com/baowenbo/DAIN/issues/44#issuecomment-624025613):

```shell
# Install PyTorch 1.4.0 with CUDA 10.0
pip install torch==1.4.0+cu100 torchvision==0.5.0+cu100 -f https://download.pytorch.org/whl/torch_stable.html
pip install scipy==1.1.0
# Then set the softlink to CUDA 10.0
sudo ln -snf /usr/local/cuda-10.0 /usr/local/cuda
# After that we can perform a complete compilation.
```

**Usage**:

1. `Local`

    ```shell
    # Step 1: Prepare
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f dain
    # Step 2: Put a single video file into ./Data/Input/
    # Step 3: Infernece
    python3 inference_dain.py -input your_input.mp4 -ts 0.5 -hr False
    ```

2. `Colab`

    Or you can try following shared colab in playground mode:

    https://colab.research.google.com/drive/1pIPHQAu7z4Z3LXztCUXiDyBaIlOqy4Me?usp=sharing

3. Description of Parameters

    | params            | abbr.  | Default    | Description                                                                                                                                 |
    |-------------------|--------|------------|---------------------------------------------------------------------------------------------------------------------------------------------|
    | --input_video     | -input | /          | The input video name.                                                                                                                       |
    | --time_step       | -ts    | 0.5        | Set the frame multiplier.<br>0.5 corresponds to 2X;<br>0.25 corresponds to 4X;<br>0.125 corresponds to 8X.                                  |
    | --high_resolution | -hr    | store_true | Default is False(action:store_true).<br>Turn it on when you handling FHD videos,<br>A frame-splitting process will reduce GPU memory usage. |

## DeOldify

Original repository: [jantic/DeOldify](https://github.com/jantic/DeOldify)

DeOldify is a Deep Learning based project for colorizing and restoring old images and video! 

~~We currently try the easiest way to colorize images using DeOldify, which is using SaaS service provided by DeepAI(**For Now**). You must sign up DeepAI.~~

We are now integrating the inference capabilities of the DeOldify model (both Artistic and Stable, no Video) with our MVIMP repository, and keeping the input and output interfaces consistent.

|  Dependency  |           Version          |
|:------------:|:--------------------------:|
|    PyTroch   |            1.5.0           |
| CUDA Toolkit | 10.1(tested locally/colab) |
|    Python    |         3.6.8(3.6+)        |

Other Python dependencies listed in `colab_requirements.txt`, and will be auto installed while running `preparation.py`.

**Usage**:

1. `Local`

    ```shell
    # Step 1: Prepare
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f deoldify
    # Step 2: Infernece
    python3 inference_deoldify.py -st
    ```

2. `Colab`

    Or you can try following shared colab in playground mode:

    https://colab.research.google.com/drive/156StQ1WdErl-_213pCQV-ysX2FT_vtjm?usp=sharing

3. Description of Parameters

    | params          | abbr.   | Default    | Description                                                                                                                                                                     |
    |-----------------|---------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | --artistic      | -art    | store_true | The artistic model achieves the highest quality results in image coloration, <br>in terms of interesting details and vibrance.                                                  |
    | --stable        | -st     | store_true | Stable model achieves the best results with landscapes and portraits.                                                                                                           |
    | --render_factor | -factor | 35         | Between 7 and 40, try more times for better performance.                                                                                                                        |
    | --watermarked   | -mark   | store_true | I respect the spirit of the original author adding a watermark to distinguish AI works, <br>but setting it to False may be more convenient for use in a production environment. |

# TODO
- [x] Chinese Document
- [x] DeOldify for colorizing and restoring old images and videos
- [x] tqdm instead of print loop
- [x] Original DeOldify local as well as Colab
- [ ] Dockerized deployment.
- [ ] https://roxanneluo.github.io/Consistent-Video-Depth-Estimation/
- [ ] MMSR for image and video super-resolution

You are welcomed to discuss future features in [this issue](https://github.com/CyFeng16/MVIMP/issues/2).

# Acknowledgment

This code is based on the [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN), [vt-vl-lab/3d-photo-inpainting](https://github.com/vt-vl-lab/3d-photo-inpainting), [baowenbo/DAIN](https://github.com/baowenbo/DAIN) and [jantic/DeOldify](https://github.com/jantic/DeOldify). Thanks to the contributors of those project.