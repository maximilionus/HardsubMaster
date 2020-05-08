from os import path, listdir, system, getcwd, chdir
from sys import platform, argv
import json

NAME_STR = "Hardsub Master"
BUILD_STR = "08052020-0353"
TITLE_STR = f"title {NAME_STR} by @maximilionus (build {BUILD_STR})"
EXECUTABLE_LOCATION = path.dirname(argv[0])

def returnMKVs(files: list):
	return [f for f in files if path.basename(f).endswith('.mkv')]

class HMDirHandler:
	def __init__(self):
		if not getcwd() == EXECUTABLE_LOCATION: chdir(EXECUTABLE_LOCATION)
		self._executable_path = EXECUTABLE_LOCATION
		self._filedir_path = ''

	def switchDir(self, value: int):
		"""
		Switch work directory.

		Arguments:
			value {int} -- 0 - switch to executable path, 1 - switch to file path.
		"""
		if value == 0: chdir(self._executable_path)
		elif value == 1 : chdir(self._filedir_path)

	def updateFileDir(self, path: str):
		self._filedir_path = path

class HMConfig:
	def __init__(self):
		CONFIG_DEFAULT = {
			"ffmpeg_path": path.abspath("./ffmpeg/ffmpeg.exe") if (path.exists('./ffmpeg/ffmpeg.exe') and platform == 'win32') else "ffmpeg"
		}
		if not self.exists():
			with open('./config.json', 'wt') as f:
				json.dump(CONFIG_DEFAULT, f, indent=4)
		with open('./config.json', 'rt') as f:
			self._config = json.load(f)

	def getFFmpegPath(self) -> str:
		return path.normpath(self._config["ffmpeg_path"])

	@staticmethod
	def exists():
		return path.exists('./config.json')