from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python36-32\tcl\tk8.6'

executables = [Executable("Main.py", base="Console")]

build_exe_options = {
    "packages": ["wx", "Video", "Variables", 'numpy.core._methods', 'numpy.lib.format', "idna", "moviepy"]}

setup(
    name="Combinar videos",
    version="1.0",
    py_modules=["wx"],
    options={"build_exe": build_exe_options},
    executables=executables,
)
