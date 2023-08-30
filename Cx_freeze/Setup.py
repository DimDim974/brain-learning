import sys
from cx_Freeze import setup, Executable

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None
<<<<<<< HEAD

setup(executables = [Executable("main.py", base=base)])
<<<<<<< HEAD
<<<<<<< HEAD
=======

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
>>>>>>> 95c6f61 ([TECH] Mise à jour du répertoire)
=======
>>>>>>> ccb8d61 ([TECH] Mise à jour de la config de CZ FREEZE.)
=======
setup(executables = [Executable("main.py", base=base,icon="icon.ico")])
>>>>>>> debe182 ([EVO] Détection de l'OS Windows + Gestion des erreurs)
