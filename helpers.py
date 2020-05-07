from os import path, listdir
from sys import platform

NAME_STR = "Hardsub Master"
VERSION_STR = "0.1"

def returnMKVs(files: list):
	return [path.basename(file) for file in files if path.basename(file).endswith('.mkv')]