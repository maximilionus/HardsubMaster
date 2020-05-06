import sys
from os import path, mkdir, system
from subprocess import Popen
from termcolor import cprint
import helpers as h

def Hardsub(mkv_file: str, output_dir):
	hardsub_subprocess = Popen(f"ffmpeg -i {mkv_file} -vf subtitles={mkv_file} {path.join(output_dir, mkv_file)}")
	hardsub_subprocess.wait()
	cprint(f'>> {mkv_file} << DONE', color='green', attrs=['reverse'])

if sys.platform == 'win32': system("color"); system(f"title {h.NAME_STR}")
if len(sys.argv) == 1: cprint('Not enough files', color='red', attrs=['reverse']); input('PRESS ENTER TO EXIT'); sys.exit()

mkv_files = sys.argv[1:]

for mkv_file in mkv_files:
	output_dir = path.abspath(path.join(path.dirname(mkv_file), 'output'))
	if not path.exists(output_dir): mkdir(output_dir)
	Hardsub(path.basename(mkv_file), output_dir)

cprint(f'{len(mkv_files)} files processed', color='yellow', attrs=['reverse'])
input('PRESS ENTER TO EXIT')