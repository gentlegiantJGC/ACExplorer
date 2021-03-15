import os
import platform

if platform.system() == "Windows":
    texconv_path = os.path.join(os.path.dirname(__file__), "texconv.exe")
else:
    raise Exception("Unknown Architecture")


def convert_texture(arg: str):
    os.system(f"{texconv_path} {arg}")
