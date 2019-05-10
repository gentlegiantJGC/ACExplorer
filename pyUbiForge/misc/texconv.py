from ctypes import CDLL, c_wchar_p, c_int
import threading
import os
import platform
if platform.architecture()[0] == '64bit':
	texconv_path = f'{os.path.dirname(__file__)}/../resources/texconv64.dll'
elif platform.architecture()[0] == '32bit':
	texconv_path = f'{os.path.dirname(__file__)}/../resources/texconv32.dll'
else:
	raise Exception('Unknown Architecture')

texconv = CDLL(texconv_path)


class ThreadBecauseQt(threading.Thread):
	def __init__(self, arg):
		threading.Thread.__init__(self)
		self.argv = arg.split(' ')

	def run(self):
		texconv.wmain(c_int(len(self.argv)), (c_wchar_p * len(self.argv))(*self.argv))


def convert_texture(arg: str):
	thread = ThreadBecauseQt(arg)
	thread.start()
