
import os

print(os.getcwd())

import time

os.mkdir("TestFolder")

time.sleep(5)

os.rename("TestFolder","TestFolder2")

time.sleep(4)

os.rmdir("TestFolder2")
