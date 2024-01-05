import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    'packages': ['os', 'zipfile', 'PyQt5.QtWidgets', 'PyQt5.QtGui'],
    'include_files': [],
    'excludes': [],
    'include_msvcr': True
}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'  # Usa questa opzione se vuoi nascondere la console su Windows

executables = [
    Executable('map_unlocker.pyw', base=base, target_name='unlocker.exe')
]

setup(
    name='stronghold map unlocker',
    version='1.0',
    description='unlocker di mappe per l\'editor di mappe',
    options={'build_exe': build_exe_options},
    executables=executables
)