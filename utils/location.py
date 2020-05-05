"""Location for all available function."""
import os

LOC = os.getcwd()
if LOC.split("/")[-1] != "MVIMP":
    raise ValueError("Please change directory to the root of MVIMP.")

ANIMEGAN_PREFIX = os.path.join(LOC, "AnimeGAN")
DAIN_PREFIX = os.path.join(LOC, "DAIN")
Photo_3D = os.path.join(LOC, "3d-photo-inpainting")

input_data_dir = os.path.join(LOC, "Data/Input")
output_data_dir = os.path.join(LOC, "Data/Output")
