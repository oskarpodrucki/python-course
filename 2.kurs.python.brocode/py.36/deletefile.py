import os
import  shutil

path = "test.txt"

try:
    os.remove(path)
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("you do not have permission to delete the file")
except OSError:
    print("that folder contains files")
else:
    print(path+" was deleted")