
<p align="center">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/CyFeng16/MVIMP" />
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/CyFeng16/MVIMP" />
    <img alt="GitHub License" src="https://img.shields.io/github/license/cyfeng16/MVIMP" />
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg" />
</p>

[English](/README.md) | [简体中文](README_zh-Hans.md) | Español

# MVIMP

**M**ixed **V**ideo and **I**mage **M**anipulation **P**rogram
*(Programa de manipulación de imágenes y videos variados)*

Entrenar un modelo de IA de buen rendimiento, es solo una parte de la historia, el hacerlo fácil de usar para otras personas, es otra. Por lo tanto, este repositorio intenta abarcar la capacidad de la IA para manipular multimedia, también, ¡Deseo que te diviertas!

| Modelo |  Entrada | Salida |        Paralelo?        |
|:--------:|:------:|:------:|:----------------------:|
| [AnimeGAN](README_es.md#animegan) | Imagenes | Imagenes |          Si          |
|   [DAIN](README_es.md#dain)   |  Video |  Video |          No         |
|  [Photo3D](README_es.md#photo3d) | Imágenes | Video | Si (No se recomienda) |
| [DeOldify](README_es.md#deoldify) | Imágenes | Imágenes |          Si          |

## AnimeGAN

Repositorio original: [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN)

Esto es el programa de Codigo abierto basado en el *paper* <AnimeGAN: a novel lightweight GAN for photo animation> (*AnimeGAN: un ligero y novedoso GAN para animación fotográfica*), el cual usa el *framework* GAN para transformar imágenes reales en imágenes de anime.

|  Dependencia  |               Versión             |
|:------------:|:----------------------------------:|
|  TensorFLow  |               1.15.2               |
| CUDA Toolkit | 10.0(Probado localmente) / 10.1(Colab) |
|    Python    |             3.6.8(3.6+)            |
|    opencv    |                  -                 |
|     tqdm     |                  -                 |
|     numpy    |                  -                 |
|     glob     |                  -                 |
|   argparse   |                  -                 |

**Uso**:

1. `Localmente`

    ```shell
    # Paso 1: Preparar
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f animegan
    # Paso 2: Ingresa tus fotos en ./Data/Input/
    # Paso 3: Ejecuta el comando para razonar/inferir
    python3 inference_animegan.py
    ```

2. `Colab`

    O puedes optar por ejecutarlo en Colab mediante el siguiente link (Playground mode):

    https://colab.research.google.com/drive/1bpwUFcr5i38_P3a0r3Qm9Dvkl-MS_Y1y?usp=sharing

## Photo3D

Repositorio original: [vt-vl-lab/3d-photo-inpainting](https://github.com/vt-vl-lab/3d-photo-inpainting)

El método para convertir una simple imagen RGB-D como entrada, en una imagen 3D (La salida es un video); es decir... Una representación de varias capas para una novedosa vista en síntesis que contienen estructuras llenas de color y profundidad en regiones ocultas en la imagen original.

|  Dependencia  |           Versión         |
|:------------:|:--------------------------:|
|    PyTroch   |            1.5.0           |
| CUDA Toolkit | 10.1 (Probado localmente/Colab) |
|    Python    |         3.6.8(3.6+)        |

Otras dependencias de Python están listadas en `requirements.txt`, y serán instaladas automáticamente mientras se ejecute `preparation.py`.

**Uso**:

1. `Localmente`

    ```shell
    # Paso 1: Preparar
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f photo3d
    # Paso 2: Ingresa tu imagen en ./Data/Input/
    # Paso 3: Ejecuta el comando para razonar/inferir
    python3 inference_photo3d.py -f 40 -n 240 -l 960
    ```

2. `Colab`

    O puedes optar por ejecutarlo en Colab mediante el siguiente link (Playground mode):

    https://colab.research.google.com/drive/1VAFCN8Wh4DAY_HDcwI-miNIBomx_MZc5?usp=sharing

    P.S. La memoria ocupada durante la operación es masiva (Crece con el argumento `-l`)

    La rutina `Higher memory` (Mayor memoria), ayuda si tu eres un usuario de Colab Pro.

3. Descripción de los parámetros

    | Parámetro            | Abreviación | Default (Por defecto) | Descripción                                              |
    |-------------------|-------|---------|----------------------------------------------------------|
    | --fps             | -f    | 40      | Los FPS para el video de salida.                                 |
    | --frames          | -n    | 240     | El numero de frames que tendrá en total el video.                    |
    | --longer_side_len | -l    | 960     | El lado más largo del video de salida (Ya sea alto o ancho). |

## DAIN

Repositorio original: [baowenbo/DAIN](https://github.com/baowenbo/DAIN)

DAIN (Depth-Aware video frame INterpolation) (Interpolación de fotogramas en videos por aprendizaje profundo? No hay traducción exacta), detecta de manera explicita la oclusión, explorando el *depth cue* (No hay traducción). Desarrolla una capa de proyección de flujo consciente de profundidad, para sintetizar flujos intermedios, en la que se muestran con preferencia los objetos mas cercanos.

|  Dependencia  |                        Versión                        |
|:------------:|:-----------------------------------------------------:|
|    PyTroch   |                         1.4.0                         |
| CUDA Toolkit |               10.0 (Probado localmente/Colab)              |
|    Python    |                      3.6.8(3.6+)                      |
|      GCC     | 7.5 (Para compilar PyTorch 1.4.0, en archivos con extensión .c/.cu) |

P.S. Asegúrate de que tu entorno virtual tenga torch-1.4.0+cu100 y torchvision-0.50+cu100
Puedes usar los siguientes [comandos](https://github.com/baowenbo/DAIN/issues/44#issuecomment-624025613):

```shell
# Instala PyTorch 1.4.0 con CUDA 10.0
pip install torch==1.4.0+cu100 torchvision==0.5.0+cu100 -f https://download.pytorch.org/whl/torch_stable.html
pip install scipy==1.1.0
# Despues define un 'softlink' a Cuda 10.0
sudo ln -snf /usr/local/cuda-10.0 /usr/local/cuda
# Despues de eso, puedes completar la compilación.
```

**Uso**:

1. `Localmente`

    ```shell
    # Paso 1: Preparar
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f dain
    # Paso 2: Ingresa un video (SOLO UNO) en ./Data/Input/
    # Paso 3: Ejecuta el comando para razonar/inferir
    python3 inference_dain.py -input your_input.mp4 -ts 0.5 -hr False
    ```

2. `Colab`

    O puedes optar por ejecutarlo en Colab mediante el siguiente link (Playground mode):

    https://colab.research.google.com/drive/1pIPHQAu7z4Z3LXztCUXiDyBaIlOqy4Me?usp=sharing

3. Descripción de los parámetros

    | Parámetro            | Abreviación | Default (Por defecto) | Descripción                                                                                                                                 |
    |-------------------|--------|------------|---------------------------------------------------------------------------------------------------------------------------------------------|
    | --input_video     | -input | /          | El nombre del video de entrada.                                                                                                                       |
    | --time_step       | -ts    | 0.5        | Define el multiplicador de frames.<br>0.5 corresponde a 2X;<br>0.25 corresponde a 4X;<br>0.125 corresponde a 8X.                                  |
    | --high_resolution | -hr    | store_true | Por defecto esta en falso (action:store_true).<br>Actívalo cuando quieras manejar videos en HD o FHD.<br>El proceso para dividir los cuadros, reduce el uso de memoria en la GPU. |

## DeOldify

Repositorio original: [jantic/DeOldify](https://github.com/jantic/DeOldify)

DeOldify es un proyecto basado en Aprendizaje Profundo para dar color y restaurar imágenes y videos.

~~Actualmente estamos intentando usar la forma mas fácil para dar color usando DeOldify, el cual es usar el servicio de SaaS proporcionado por DeepAI(**Por ahora**). Necesitaras registrarte en DeepAI.~~

Actualmente estamos integrando las capacidades de inferencia del modelo de DeOldify (Artístico y Estable; no en video) con el repositorio, manteniendo las interfaces de entrada y salida consistente.

|  Dependencia  |           Versión          |
|:------------:|:--------------------------:|
|    PyTroch   |            1.5.0           |
| CUDA Toolkit | 10.1 (Probado localmente/Colab) |
|    Python    |         3.6.8(3.6+)        |

Otras dependencias de Python están listadas en `colab_requirements.txt`, y serán instaladas automáticamente mientras se ejecute `preparation.py`.

**Uso**:

1. `Localmente`

    ```shell
    # Paso 1: Preparar
    git clone https://github.com/CyFeng16/MVIMP.git
    cd MVIMP
    python3 preparation.py -f deoldify
    # Paso 2: Ejecuta el comando para razonar/inferir
    python3 inference_deoldify.py -st
    ```

2. `Colab`

    O puedes optar por ejecutarlo en Colab mediante el siguiente link (Playground mode):

    https://colab.research.google.com/drive/156StQ1WdErl-_213pCQV-ysX2FT_vtjm?usp=sharing

3. Descripción de los parámetros

    | Parámetro            | Abreviación | Default (Por defecto) | Descripción                                                                                                                                                                     |
    |-----------------|---------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | --artistic      | -art    | store_true | El modelo artístico, logra un resultado de mayor calidad en la coloración en la imagen, <br>en términos de interesantes detalles y vibración (Vividez?).                                                  |
    | --stable        | -st     | store_true | El modelo estable, logra los mejores resultados en paisajes y retratos.                                                                                                           |
    | --render_factor | -factor | 35         | Entre 7 y 40, intenta varias veces para el mejor funcionamiento.                                                                                                                        |
    | --watermarked   | -mark   | store_true | Respetamos el trabajo del autor original añadiendo un marca de agua, marcando el trabajo como creado con IA, <br>pero tal vez sea mas conveniente cambiarlo a 'False' para usarlo en un entorno de producción. |

# TODO
- [x] Documentación en chino
- [x] DeOldify para dar color y restaurar imágenes y videos antiguos
- [x] tqdm en lugar de un 'print loop'
- [x] DeOldify original tanto en local como en Colab
- [ ]  Despliegue de Dockerize.
- [ ] https://roxanneluo.github.io/Consistent-Video-Depth-Estimation/
- [ ] MMSR para super-resolución en imágenes y video.

Eres bienvenido a discutir características futuras en [este 'issue'](https://github.com/CyFeng16/MVIMP/issues/2).

# Reconocimiento

El código esta basado en [TachibanaYoshino/AnimeGAN](https://github.com/TachibanaYoshino/AnimeGAN), [vt-vl-lab/3d-photo-inpainting](https://github.com/vt-vl-lab/3d-photo-inpainting), [baowenbo/DAIN](https://github.com/baowenbo/DAIN) y [jantic/DeOldify](https://github.com/jantic/DeOldify). Gracias a los contribuidores de esos proyectos.
