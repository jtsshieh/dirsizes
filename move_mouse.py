import ctypes
import time
import random

while True:
    ctypes.windll.user32.SetCursorPos(random.randrange(0, 1000), random.randrange(0, 1000))
    time.sleep(random.randrange(0, 10))

