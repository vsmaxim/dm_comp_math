from os.path import expanduser
import os
from cx_Freeze import setup, Executable

usr = expanduser('~')

os.environ['TCL_LIBRARY'] = usr + "\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = usr + "\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

setup(
name = 'comp_math',
description = 'Computer Math system',
executables = [Executable("menu.py")]
	)
