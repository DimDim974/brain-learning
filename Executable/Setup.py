import sys
from cx_Freeze import setup, Executable

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(executables = [Executable("main.py", base=base)])




#Renseignez ici la liste complète des packages utilisés par votre application
packages = ["idna","tkinter","hashlib","os","sqlite3"]#
options = {
    'build_exe': {    
        'packages':packages,
    },
}
#Adaptez les valeurs des variables "name", "version", "description" à votre programme.
setup(
    name = "Brain_Learning",
    options = options,
    version = "1.0",
    description = 'Brain Learning',
    executables = [Executable("main.py", base=base)]
)