<p align="center">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/CyFeng16/MVIMP" />
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/CyFeng16/MVIMP" />
    <img alt="GitHub License" src="https://img.shields.io/github/license/cyfeng16/MVIMP" />
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg" />
</p>

[English](/README.md) | 简体中文 | [Español](docs/README_es.md)

# MVIMP

`MVIMP`(**M**ixed **V**ideo and **I**mage **M**anipulation **P**rogram)名字的灵感来自于`GIMP`(**G**NU **I**mage **M**anipulation **P**rogram),也希望更多的人可以尝试使用它w

目前MVIMP中添加了如下三个第三方功能,代码目录及各文件功能如下:
- `third_party`: 存放第三方repo,本打算使用submodule的模式,不过因为各个代码库代码风格不同无法做到统一,所以就保留LISENCE做minimize的二次开发
- `mvimp_utils`: 存放处理文件和视频的单独功能模块,用于辅助推理
- `preparation.py`: 所有的准备工作集成在一起
- `inference_animegan.py`: 统一输入输出接口,辅助 AnimeGAN 的推理
- `inference_dain.py`: 统一输入输出接口,辅助 DAIN 的推理
- `inference_photo3d.py`: 统一输入输出接口,辅助 3d-photo-inpainting 的推理
- `inference_deoldify.py`: 统一输入输出接口,辅助 DeOldify 的推理

第三方功能的输入输出定义如下:

|   模型   |   输入  |   输出  |    是否并行    |
|:--------:|:-------:|:-------:|:--------------:|
| [AnimeGAN](README_zh-Hans.md#animegan) | 图片(s) | 图片(s) |     可并行     |
|   [DAIN](README_zh-Hans.md#dain)   |   视频  |   视频  |    不可并行    |
|  [Photo3D](README_zh-Hans.md#photo3d) | 图片(s) |   视频  | 可并行(不推荐) |
| [DeOldify](README_zh-Hans.md#deoldify) | 图片(s) | 图片(s) |     可并行     |

## AnimeGAN

AnimeGAN的原始仓库位于 [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN), 作为《 AnimeGAN：一种用于照片动画的新型轻量级GAN》论文的开放源代码，它使用GAN框架将真实世界的照片转换为动漫图像。

### 系统需求

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

### 使用方法

1. `本地运行`

    ```shell
    # Step 1: 准备工作
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f animegan 
    # Step 2: 把需要处理的图片(s)放入 ./Data/Input/
    # Step 3: 运行如下命令进行推理
    python3 inference_animegan.py
    ```

2. `Colab云端运行`

    我们也可以选择在 playground 模式下在Colab上运行:

    https://colab.research.google.com/drive/1bpwUFcr5i38_P3a0r3Qm9Dvkl-MS_Y1y?usp=sharing

## Photo3D

Photo3D的原始仓库位于 [vt-vl-lab/3d-photo-inpainting](https://github.com/vt-vl-lab/3d-photo-inpainting),Photo3D输入单个RGB-D输入图像并将其转换为3D照片(视频)的方法。

### 系统需求

|  Dependency  |           Version          |
|:------------:|:--------------------------:|
|    PyTroch   |            1.5.0           |
| CUDA Toolkit | 10.1(tested locally/colab) |
|    Python    |         3.6.8(3.6+)        |

其他的python依赖需求写在requirements.txt中,运行`preparation.py`时将自动添加。

### 使用方法

1. `本地运行`

    ```shell
    # Step 1: 准备工作
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f photo3d
    # Step 2: 把需要处理的图片放入 ./Data/Input/
    # Step 3: 运行如下命令进行推理
    python3 inference_photo3d.py -f 40 -n 240 -l 960
    ```

2. `Colab云端运行`

    我们也可以选择在 playground 模式下在Colab上运行:

    https://colab.research.google.com/drive/1VAFCN8Wh4DAY_HDcwI-miNIBomx_MZc5?usp=sharing

    需要注意的是,Photo3D所需的运行时内存随着`longer_side_len`(输出视频最大长/宽)的参数增加而显著增加,如果是Colab Pro用户建议开启`高内存`的运行时,并尽量一次推理一张图片.

### 参数说明

| 参数名称          | 参数缩写 | 默认值 | 参数描述                  |
|-------------------|----------|--------|---------------------------|
| --fps             | -f       | 40     | 设置输出视频的FPS.        |
| --frames          | -n       | 240    | 设置输出视频的帧数.       |
| --longer_side_len | -l       | 960    | 设置输出视频的最长边边长. |

## DAIN

DAIN的原始仓库位于 [baowenbo/DAIN](https://github.com/baowenbo/DAIN),DAIN通过检测深度感知流投影层来合成中间流,进行视频帧内插.

当前版本的DAIN可以流畅运行1080p视频的插帧.

### 系统需求

|  Dependency  |                        Version                        |
|:------------:|:-----------------------------------------------------:|
|    PyTroch   |                         1.4.0                         |
| CUDA Toolkit |               10.0(tested locally/colab)              |
|    Python    |                      3.6.8(3.6+)                      |
|      GCC     | 7.5(Compiling PyTorch 1.4.0 extension files (.c/.cu)) |

需要注意当前版本的DAIN不支持PyTorch1.5.0版本,所以我们在本地和云端运行环境中都需要手动安装 torch-1.4.0+cu100 和 torchvision-0.5.0+cu100. 参见[issue](https://github.com/baowenbo/DAIN/issues/44#issuecomment-624025613).

```shell
# 安装 PyTorch 1.4.0(CUDA 10.0)
pip install torch==1.4.0+cu100 torchvision==0.5.0+cu100 -f https://download.pytorch.org/whl/torch_stable.html
# 设置系统软链接指向 CUDA 10.0(CUDA需要提前安装)
sudo ln -snf /usr/local/cuda-10.0 /usr/local/cuda
```

### 使用方法

1. `本地运行`

    ```shell
    # Step 1: 准备工作
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f dain
    # Step 2: 将需要插帧的视频文件放在 ./Data/Input/ 下
    # Step 3: 运行如下命令进行推理
    python3 inference_dain.py -input your_input.mp4 -ts 0.5 -hr
    ```

2. `Colab云端运行`

    我们也可以选择在 playground 模式下在Colab上运行:

    https://colab.research.google.com/drive/1pIPHQAu7z4Z3LXztCUXiDyBaIlOqy4Me?usp=sharing

### 参数说明

| 参数名称          | 参数缩写 | 默认值                                 | 参数描述                                                                                                               |
|-------------------|----------|----------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| --input_video     | -input   | /                                      | 设置输入视频名称.                                                                                                      |
| --time_step       | -ts      | 0.5                                    | 设置插帧倍数,0.5对应2X,0.25对应4X,0.125对应8X.                                                                         |
| --high_resolution | -hr      | store_true<br>(不加为False/出现即True) | 默认False.<br>对于视频格式为720p+的视频而言V100的显存不足以运行DAIN,<br>设置True将一帧拆分为4块分别处理以减少显存占用. |

## DeOldify

DeOldify 的原始仓库位于 [jantic/DeOldify](https://github.com/jantic/DeOldify),DeOldify是一个基于深度学习的项目，用于对旧图像和视频进行着色和还原.

我们将DeOldify模型的推理功能（艺术性和稳定性，无视频）与我们的MVIMP存储库集成在一起，并保持输入和输出接口的一致性。

### 系统需求

|  Dependency  |           Version          |
|:------------:|:--------------------------:|
|    PyTroch   |            1.5.0           |
| CUDA Toolkit | 10.1(tested locally/colab) |
|    Python    |         3.6.8(3.6+)        |

其他的python依赖需求写在requirements.txt中,运行`preparation.py`时将自动添加。

### 使用方法

1. `本地运行`

    ```shell
    # Step 1: 准备工作
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f deoldify
    # Step 2: 运行如下命令进行推理
    python3 inference_deoldify.py -st
    ```

2. `Colab云端运行`

    我们也可以选择在 playground 模式下在Colab上运行:

    https://colab.research.google.com/drive/156StQ1WdErl-_213pCQV-ysX2FT_vtjm?usp=sharing

### 参数说明

|     参数名称    | 参数缩写 |                 默认值                 |                                              参数描述                                             |
|:---------------:|:--------:|:--------------------------------------:|:-------------------------------------------------------------------------------------------------:|
| --artistic      | -art     | store_true<br>(不加为False/出现即True) | 艺术模型在有趣的细节和鲜艳度方面实现了图像着色的最高质量结果。                                    |
| --stable        | -st      | store_true<br>(不加为False/出现即True) | 稳定的模型可以通过风景和人像获得最佳效果。                                                        |
| --render_factor | -factor  | 35                                     | 在7到40之间，尝试更多次以获得更好的性能。                                                         |
| --watermarked   | -mark    | store_true<br>(不加为False/出现即True) | 我尊重原始作者的精神，即添加水印来区分AI作品，<br>但将其设置为False可能在生产环境中使用更为方便。 |
