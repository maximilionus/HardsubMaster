# Hardsub Master
- [Hardsub Master](#hardsub-master)
	- [Main Information](#main-information)
	- [Usage](#usage)
	- [How to build](#how-to-build)
## Main Information
**Hardsub Master** - tool for... hardsubbing. Doing exactly what you expect from it - merges subs into video. Currently it works only with `.mkv` containers. Developed for personal usage.  
All releases are built for `win-x64`, so if you're using different platform you will have to build it by yourself or run from source *(python3 required for both actions)*.

| Requirements                                            | Version          |
| :------------------------------------------------------ | :--------------- |
| [`ffmpeg`](https://ffmpeg.org/) installed and in `PATH` | 20200504-5767a2e |

## Usage
- If subtitles are already inside the container then simply drag all `mkv` files to `HardsubMaster` executable and it will do the rest. Result will be saved to `./output/`

## How to build
1. Install `python3` *(3.8.2 was used by me)* and `pip` package manager.
2. Run `py -m pip install pipenv`.
3. Then run `pipenv install && pipenv run py setup.py build && pipenv --rm` in this project dir.
4. Build can be found in `./build/` directory.