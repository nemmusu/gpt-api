import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["gpt", "argparse","configparser", "openai", "PyQt5.QtCore", "PyQt5.QtWidgets"],
    "include_msvcr": True,
    "include_files": [
        ("config.ini"),  # Includi il file di configurazione
        # Aggiungi eventuali altri file necessari
    ],
}

setup(
    name="GUI ChatGPT",
    version="1.0",
    description="Interfaccia per utilizzare ChatGPT tramite chiave API",
    options={"build_exe": build_exe_options},
    executables=[Executable("gui.pyw", base="Win32GUI")],
)
