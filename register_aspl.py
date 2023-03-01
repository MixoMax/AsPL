import winreg
import os
import sys

#copy run_aspl.py to C:\Python39\Scripts

os.chdir("C:/")
try:
    os.chdir("Python39")
except:
    os.mkdir("Python39")
    os.chdir("Python39")

try:
    os.chdir("Scripts")
except:
    os.mkdir("Scripts")


#change back to the directory of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.system("copy run_aspl.py C:\Python39\Scripts")

print("run_aspl.py copied to C:\Python39\Scripts")


# Set the path to your run_aspl.py script
RUN_ASPL_PATH = "C:/Python39/Scripts/run_aspl.py"

# Set the path to your Python executable
PYTHON_PATH = str(os.path.dirname(sys.executable)) + "/python.exe"

print(PYTHON_PATH)

# Define the file extension and program path
file_ext = '.aspl'
prog_path = f'{PYTHON_PATH} "{RUN_ASPL_PATH}" "%1"'

# Open the registry key
with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, file_ext) as key:
    # Set the default value to the file extension
    winreg.SetValueEx(key, '', 0, winreg.REG_SZ, file_ext)
    # Create a subkey for the shell command
    with winreg.CreateKey(key, 'shell') as shell_key:
        # Create a subkey for the "open" command
        with winreg.CreateKey(shell_key, 'open') as open_key:
            # Create a subkey for the command to run
            with winreg.CreateKey(open_key, 'command') as command_key:
                # Set the default value to the command to run
                winreg.SetValueEx(command_key, '', 0, winreg.REG_SZ, prog_path)

print(f'{file_ext} file association added to the registry.')
