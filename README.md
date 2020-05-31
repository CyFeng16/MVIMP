<p align="center">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/CyFeng16/MVIMP" />
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/CyFeng16/MVIMP" />
    <img alt="GitHub License" src="https://img.shields.io/github/license/cyfeng16/MVIMP" />
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg" />
</p>

English | [简体中文](docs/README_zh-Hans.md) | [Español](docs/README_es.md)

# MVIMP

The name `MVIMP` (**M**ixed **V**ideo and **I**mage **M**anipulation **P**rogram) was inspired by the name` GIMP` (**G**NU **I**mage **M**anipulation **P**rogram), which hope it can help more people.

I realize that training a good-performance AI model is kind of just one side of the story, make it easy to use for others is the other thing. Thus, this repository built to embrace out-of-the-box AI ability to manipulate multimedia. Last but not least, **wish you have fun**!

|                          Model                         |  Input | Output |        Parallel        |                                                       Colab Link                                                      |
|:------------------------------------------------------:|:------:|:------:|:----------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| [AnimeGAN](https://github.com/CyFeng16/MVIMP#animegan) | Images | Images |          True          |       [link](https://colab.research.google.com/github/CyFeng16/MVIMP/blob/master/docs/MVIMP_AnimeGAN_Demo.ipynb)      |
|     [DAIN](https://github.com/CyFeng16/MVIMP#dain)     |  Video |  Video |          False         |         [link](https://colab.research.google.com/github/CyFeng16/MVIMP/blob/master/docs/MVIMP_DAIN_Demo.ipynb)        |
| [DeOldify](https://github.com/CyFeng16/MVIMP#deoldify) | Images | Images |          True          |       [link](https://colab.research.google.com/github/CyFeng16/MVIMP/blob/master/docs/MVIMP_DeOldify_Demo.ipynb)      |
|  [Photo3D](https://github.com/CyFeng16/MVIMP#photo3d)  | Images | Videos | True(not recommmended) |       [link](https://colab.research.google.com/github/CyFeng16/MVIMP/blob/master/docs/MVIMP_Photo3D_Demo.ipynb)       |
|  [Waifu2x](https://github.com/CyFeng16/MVIMP#waifu2x)  | Images | Images |          True          | [link](https://colab.research.google.com/github/CyFeng16/MVIMP/blob/master/docs/MVIMP_Waifu2x_ncnn_Vulkan_Demo.ipynb) |

## AnimeGAN

![](https://cdn.jsdelivr.net/gh/CyFeng16/MVIMP/docs/assets/animegan.png.webp)

Original repository: [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN)

This is the Open source of the paper <AnimeGAN: a novel lightweight GAN for photo animation>, which uses the GAN framwork to transform real-world photos into anime images.

|  Dependency  |               Version              |
|:------------:|:----------------------------------:|
|  TensorFLow  |               1.15.2               |
| CUDA Toolkit | 10.0(tested locally) / 10.1(colab) |
|    Python    |             3.6.8(3.6+)            |

**Usage**:

1. `Colab`

    You can open our jupyter notebook through [colab link](https://colab.research.google.com/github/CyFeng16/MVIMP/blob/master/docs/MVIMP_AnimeGAN_Demo.ipynb).

2. `Local`

    ```shell
    # Step 1: Prepare
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f animegan 
    # Step 2: Put your photos into ./Data/Input/
    # Step 3: Infernece
    python3 inference_animegan.py
    ```

## DAIN

![](docs/assets/dain.gif)

Original repository: [baowenbo/DAIN](https://github.com/baowenbo/DAIN)

Depth-Aware video frame INterpolation (DAIN) model explicitly detect the occlusion by exploring the depth cue. We develop a depth-aware flow projection layer to synthesize intermediate flows that preferably sample closer objects than farther ones. 

This method achieves SOTA performance on the Middlebury dataset. Video are provided [here](https://www.youtube.com/watch?v=-f8f0igQi5I).

The current version of DAIN (in this repo) can smoothly run 1080p video frame insertion even on GTX-1080 GPU card, as long as you turn `-hr` on (see `Description of Parameters` below).

|  Dependency  |                        Version                        |
|:------------:|:-----------------------------------------------------:|
|    PyTroch   |                         1.0.0                         |
| CUDA Toolkit |               9.0(colab tested)              |
|    Python    |                      3.6.8(3.6+)                      |
|      GCC     | 4.9(Compiling PyTorch 1.0.0 extension files (.c/.cu)) |

P.S. Make sure your virtual env has torch-1.0.0 and torchvision-0.2.1 with CUDA-9.0 .
~~You can use the following [command](https://github.com/baowenbo/DAIN/issues/44#issuecomment-624025613):~~
You can find out dependencies issue at #5  and #16 .

**Usage**:

1. `Colab`

    You can open our jupyter notebook through [colab link](https://colab.research.google.com/github/CyFeng16/MVIMP/blob/master/docs/MVIMP_DAIN_Demo.ipynb).


2. `Local`

    ```shell
    # Step 1: Prepare
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f dain
    # Step 2: Put a single video file into ./Data/Input/
    # Step 3: Infernece
    python3 inference_dain.py -input your_input.mp4 -ts 0.5 -hr
    ```

3. Description of Parameters

    | params            | abbr.  | Default    | Description                                                                                                                                 |
    |-------------------|--------|------------|---------------------------------------------------------------------------------------------------------------------------------------------|
    | --input_video     | -input | /          | The input video name.                                                                                                                       |
    | --time_step       | -ts    | 0.5        | Set the frame multiplier.<br>0.5 corresponds to 2X;<br>0.25 corresponds to 4X;<br>0.125 corresponds to 8X.                                  |
    | --high_resolution | -hr    | store_true | Default is False(action:store_true).<br>Turn it on when you handling FHD videos,<br>A frame-splitting process will reduce GPU memory usage. |

## DeOldify

![](https://cdn.jsdelivr.net/gh/CyFeng16/MVIMP/docs/assets/deoldify.png.webp)

Original repository: [jantic/DeOldify](https://github.com/jantic/DeOldify)

DeOldify is a Deep Learning based project for colorizing and restoring old images and video! 

We are now integrating the inference capabilities of the DeOldify model (both Artistic and Stable, no Video) with our MVIMP repository, and keeping the input and output interfaces consistent.

|  Dependency  |           Version          |
|:------------:|:--------------------------:|
|    PyTroch   |            1.5.0           |
| CUDA Toolkit | 10.1(tested locally/colab) |
|    Python    |         3.6.8(3.6+)        |

Other Python dependencies listed in `colab_requirements.txt`, and will be auto installed while running `preparation.py`.

**Usage**:

1. `Colab`

    You can open our jupyter notebook through [colab link](https://colab.research.google.com/github/CyFeng16/MVIMP/blob/master/docs/MVIMP_DeOldify_Demo.ipynb).

2. `Local`

    ```shell
    # Step 1: Prepare
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f deoldify
    # Step 2: Infernece
    python3 -W ignore inference_deoldify.py -art
    ```

3. Description of Parameters

    | params          | abbr.   | Default    | Description                                                                                                                                                                     |
    |-----------------|---------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | --artistic      | -art    | store_true | The artistic model achieves the highest quality results in image coloration, <br>in terms of interesting details and vibrance.                                                  |
    | --stable        | -st     | store_true | Stable model achieves the best results with landscapes and portraits.                                                                                                           |
    | --render_factor | -factor | 35         | Between 7 and 40, try more times for better performance.                                                                                                                        |
    | --watermarked   | -mark   | store_true | I respect the spirit of the original author adding a watermark to distinguish AI works, <br>but setting it to False may be more convenient for use in a production environment. |

## Photo3D

![](https://cdn.jsdelivr.net/gh/CyFeng16/MVIMP/docs/assets/photo3d.jpeg.webp)

Original repository: [vt-vl-lab/3d-photo-inpainting](https://github.com/vt-vl-lab/3d-photo-inpainting)

The method for converting a single RGB-D input image into a 3D photo, i.e., a multi-layer representation for novel view synthesis that contains hallucinated color and depth structures in regions occluded in the original view. 

|  Dependency  |           Version          |
|:------------:|:--------------------------:|
|    PyTroch   |            1.5.0           |
| CUDA Toolkit | 10.1(tested locally/colab) |
|    Python    |         3.6.8(3.6+)        |

Other Python dependencies listed in `requirements.txt`, and will be auto installed while running `preparation.py`.

**Usage**:

1. `Colab`

    You can open our jupyter notebook through [colab link](https://colab.research.google.com/github/CyFeng16/MVIMP/blob/master/docs/MVIMP_Photo3D_Demo.ipynb).

    P.S. Massive memory is occupied during operation(grows with `-l`). 
    
    `Higher memory` runtime helps if you are Colab Pro user.

2. `Local`

    ```shell
    # Step 1: Prepare
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f photo3d
    # Step 2: Put your photos into ./Data/Input/
    # Step 3: Infernece
    python3 inference_photo3d.py -f 40 -n 240 -l 960
    ```

3. Description of Parameters

    | params            | abbr. | Default | Description                                              |
    |-------------------|-------|---------|----------------------------------------------------------|
    | --fps             | -f    | 40      | The FPS of output video.                                 |
    | --frames          | -n    | 240     | The number of frames of output video.                    |
    | --longer_side_len | -l    | 960     | The longer side of output video(either height or width). |

## Waifu2x

![](https://cdn.jsdelivr.net/gh/CyFeng16/MVIMP/docs/assets/waifu2x.png.webp)

Original repository: [nihui/waifu2x-ncnn-vulkan](https://github.com/nihui/waifu2x-ncnn-vulkan)

waifu2x-ncnn-vulkan is a ncnn implementation of waifu2x, which could runs fast on Intel/AMD/Nvidia with Vulkan API.

We are now integrating the inference capabilities of the waifu2x model ("cunet", "photo" and "animeart") with our MVIMP repository, and keeping the input and output interfaces consistent.

|  Dependency  |           Version          |
|:------------:|:--------------------------:|
| CUDA Toolkit | 10.1(tested locally/colab) |
|    Python    |         3.6.8(3.6+)        |

**Usage**:

1. `Colab`

    You can open our jupyter notebook through [colab link](https://colab.research.google.com/github/CyFeng16/MVIMP/blob/master/docs/MVIMP_Waifu2x_ncnn_Vulkan_Demo.ipynb).

2. `Local`

    ```shell
    # Step 1: Prepare
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f waifu2x-vulkan
    # Step 2: Infernece
    python3 inference_waifu2x-vulkan.py -s 2 -n 0
    ```

3. Description of Parameters

    | params     | abbr. | Default                     | Description                                                                                                                                                                               |
    |------------|-------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | --scale    | -s    | 2                           | upscale ratio (1/2, default=2)                                                                                                                                                            |
    | --noise    | -n    | 0                           | denoise level (-1/0/1/2/3, default=0)                                                                                                                                                     |
    | --tilesize | -t    | 400                         | Tile size. Between 32 and 19327352831, no appreciable effect.                                                                                                                             |
    | --model    | -m    | cunet                       | Model to use. You can choose in "cunet", "photo" and "animeart".                                                                                                                          |
    | --tta      | -x    | store_true<br>(True if set) | TTA mode able to reduce several types of artifacts but it's 8x slower than the non-TTA mode.<br>See for [details](https://github.com/nagadomi/waifu2x/issues/148#issuecomment-255754265). |

# TODO
- [ ] Dockerized deployment.
- [ ] https://roxanneluo.github.io/Consistent-Video-Depth-Estimation/
- [ ] Image and video super-resolution(still selecting candidates.)
- [ ] https://lllyasviel.github.io/PaintingLight/

You are welcomed to discuss future features in [this issue](https://github.com/CyFeng16/MVIMP/issues/2).

# Acknowledgment

This code is based on the [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN), [vt-vl-lab/3d-photo-inpainting](https://github.com/vt-vl-lab/3d-photo-inpainting), [baowenbo/DAIN](https://github.com/baowenbo/DAIN), [jantic/DeOldify](https://github.com/jantic/DeOldify) and [nihui/waifu2x-ncnn-vulkan](https://github.com/nihui/waifu2x-ncnn-vulkan). Thanks to the contributors of those project.

@EtianAM provides our Spanish guide.
@BrokenSilence improves DAIN's performance.
