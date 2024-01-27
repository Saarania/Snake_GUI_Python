from cx_Freeze import setup, Executable

# includes = ["pygame._numpysurfarray"]

options = {
    "build_exe": {
        "include_files": ["digitalAdventure.mp3"],
    }
}

setup(
    name="Snakexe",
    version="1.0",
    description="GUI python game",
    options=options,
    executables=[Executable("main.py", base="Win32GUI")],
)
