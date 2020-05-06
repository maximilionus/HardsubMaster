from os import path

NAME_STR = "Hardsub Master"
VERSION_STR = "0.1"

def returnMKVs(files: list):
	return (file for file in files if path.basename(file).endswith('.mkv'))