import sys
from os import path, mkdir, system
import subprocess
from termcolor import cprint
import helpers as h

def burn_subtitles(mkv_file: str, output_dir: str, subtitlesFile: str):
	subprocess.call(f'ffmpeg -i "{mkv_file}" -c:v libx264 -crf 18 -c:a copy -b:a 128k -vf subtitles={subtitlesFile} {path.join(output_dir, mkv_file)}')
	cprint(f'>> {mkv_file} << DONE', color='green', attrs=['reverse'])

if sys.platform == 'win32': system("color"); system(f"title {h.NAME_STR} (version {h.VERSION_STR})")
if len(sys.argv) == 1: cprint('Not enough files', color='red', attrs=['reverse']); input('PRESS ENTER TO EXIT'); sys.exit()

mkv_files = h.returnMKVs(sys.argv[1:])
for mkv_file in mkv_files:
	output_dir = './output'
	if not path.exists(output_dir): mkdir(output_dir)
	burn_subtitles(mkv_file=mkv_file, output_dir=output_dir, subtitlesFile=sys.argv[sys.argv.index('--subtitles') + 1] if '--subtitles' in sys.argv else mkv_file)

cprint(f'{len(mkv_files)} files processed', color='yellow', attrs=['reverse'])
input('PRESS ENTER TO EXIT')