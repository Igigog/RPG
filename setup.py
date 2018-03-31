import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': 'atexit'
    }
}

executables = [
    Executable('core.py', base=base)
]

setup(name='RPG',
      version='0.1',
      description='MWAHAHAHAHA',
      options=options,
      executables=executables
)