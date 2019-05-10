import os
import platform
if platform.system() == 'Windows':
	texconv_path = f'{os.path.dirname(__file__)}/../resources/texconv.exe'
else:
	raise Exception('Unknown Architecture')


def convert_texture(arg: str):
	os.system(f'{texconv_path} {arg}')
