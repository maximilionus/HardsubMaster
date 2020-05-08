import sys, os
import subprocess
from termcolor import cprint, colored
import helpers as h

def burn_subtitles(mkv_file_path: str, output_dir: str, ffmpeg_path: str):
	mkv_file = os.path.basename(mkv_file_path)
	subprocess.call(f'{ffmpeg_path} -i "{mkv_file}" -c:v libx264 -crf 18 -c:a copy -b:a 128k -vf subtitles={mkv_file} {os.path.join(output_dir, mkv_file)}')
	cprint(f'>> {mkv_file} << DONE', color='green', attrs=['reverse'])

# Init
hmdir = h.HMDirHandler()
hmconfig = h.HMConfig()

if sys.platform == 'win32': os.system("color"); os.system(h.TITLE_STR)
if len(sys.argv) == 1: cprint('Not enough files', color='red', attrs=['reverse']); input('PRESS ENTER TO EXIT'); sys.exit()

# Begin merging
mkv_files_paths = h.returnMKVs(sys.argv[1:])
for mkv_file_path in mkv_files_paths:
	hmdir.updateFileDir(os.path.dirname(mkv_file_path))
	hmdir.switchDir(1)
	output_dir = './output'
	if not os.path.exists(output_dir): os.mkdir(output_dir)
	burn_subtitles(mkv_file_path=mkv_file_path, output_dir=output_dir, ffmpeg_path=hmconfig.getFFmpegPath())

cprint(f'{len(mkv_files_paths)} files processed', color='green')
input('\a' + colored('PRESS ENTER TO EXIT', color='green', attrs=['reverse']))