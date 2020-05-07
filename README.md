# MVIMP

Mixed Video and Image Manipulation Program

Make AI easier to use, embrace out of the box AI ability to manipulate multimedia(video and photo for now).

## AnimeGAN

Original repository: [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN)

This is the Open source of the paper <AnimeGAN: a novel lightweight GAN for photo animation>, which uses the GAN framwork to transform real-world photos into anime images.

Requirements:
- TensorFLow 1.15.2
- CUDA 10.0(tested locally) / 10.1(colab)
- Python 3.6.8(3.6+/3.7+/3.8+)
- opencv
- tqdm
- numpy
- glob
- argparse

Usage:

```shell
# Step 1: Prepare
git clone https://github.com/CyFeng16/MVIMP.git
cd MVIMP
python3 preparation.py -f animegan 
# Step 2: Put your photos into ./Data/Input/
# Step 3: Infernece
python3 inference_animegan.py
```

Colab: Or you can try Colab in playground mode.

https://colab.research.google.com/drive/1bpwUFcr5i38_P3a0r3Qm9Dvkl-MS_Y1y?usp=sharing

## Photo3D

Original repository: [vt-vl-lab/3d-photo-inpainting](https://github.com/vt-vl-lab/3d-photo-inpainting)

a method for converting a single RGB-D input image into a 3D photo, i.e., a multi-layer representation for novel view synthesis that contains hallucinated color and depth structures in regions occluded in the original view. 

Requirements:
- PyTroch 1.15.2
- CUDA 10.0(tested locally) / 10.1(colab)
- Python 3.6.8(3.6+/3.7+/3.8+)
- opencv
- tqdm
- numpy
- glob
- argparse



https://colab.research.google.com/drive/1VAFCN8Wh4DAY_HDcwI-miNIBomx_MZc5?usp=sharing