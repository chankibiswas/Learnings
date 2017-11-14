from cx_Freeze import setup, Executable

setup(name='Dummy',
      version='0.1',
      description='Demo',
      executables = [Executable("UserInput.py")])
