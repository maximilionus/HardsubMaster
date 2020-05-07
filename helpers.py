from os import path, listdir, system
from sys import platform

NAME_STR = "Hardsub Master"
BUILD_STR = "07052020-2249"
TITLE_STR = f"title {NAME_STR} by @maximilionus (build {BUILD_STR})"

def returnMKVs(files: list):
	return [path.basename(file) for file in files if path.basename(file).endswith('.mkv')]