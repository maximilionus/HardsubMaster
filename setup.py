import sys
from cx_Freeze import setup, Executable
import helpers as h

build_exe_options = {
	"packages": ["os", "subprocess", "termcolor"],
	"excludes": ["tkinter", "asyncio", "distutils", "email", "html", "http", "logging", "test", "unittest", "urllib"],
	"include_files": ["./LICENSE"]
}

base = None

setup(  name = h.NAME_STR,
		version = h.VERSION_STR,
		options = {"build_exe": build_exe_options},
		executables = [Executable("main.py", base=base, targetName=h.NAME_STR.replace(' ', ''))])