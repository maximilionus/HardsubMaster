# Hardsub Master
- [Hardsub Master](#hardsub-master)
	- [Main Information](#main-information)
	- [Usage](#usage)
	- [How to build](#how-to-build)
	- [Advanced Information](#advanced-information)
		- [Configuration file](#configuration-file)
			- [About](#about)
			- [Default Values](#default-values)

## Main Information
**Hardsub Master** - Tool for... hardsubbing. Does exactly what you expect from it - merges subs into video. Currently it works only with `.mkv` containers. Developed for personal usage.  
All releases are built for `win-x64` and already <ins>contains</ins> `ffmpeg x64` binary inside of them, so if you're using different platform you will have to build sources *(python3 required)* and install `ffmpeg` by yourself.

## Usage
- Make sure that name of your file is as short and simple as possible. Something like `test1.mkv`.
- If subtitles are already inside the container then simply drag all `mkv` files to `HardsubMaster` executable and it will do the rest. Result will be saved to `./output/`

## How to build
1. Install `python3` *(3.8.2 was used by me)* and `pip` package manager.
2. Run `py -m pip install pipenv`.
3. Then run `pipenv install && pipenv run py setup.py build && pipenv --rm` in this project dir.
4. Build can be found in `./build/` directory.

## Advanced Information
### Configuration file
#### About
Configuration file *(.json)* automaticly generates in app directory on first launch. It contains very sensitive information like absolute paths to files and dirs, so if you're moving *Hardsub Master* to another directory - be sure to delete `config.json` file before launching it.

#### Default Values

|Value|Description| Values |
| :-- | :-- | :-- |
| `ffmpeg_path` | Path to ffmpeg executable | > `"ffmpeg"` - if you have ffmpeg installed and accessible from terminal.<br>> `"{path}"` - If `ffmpeg` executable found in `./ffmpeg/` dir and platform is `windows` |

---

Releases of this software for `Windows x64` uses build of <a href=http://ffmpeg.org>FFmpeg</a> licensed under the <a href=http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html>LGPLv2.1</a> and its source can be downloaded <a href=https://ffmpeg.org/download.html>here</a>