import pyautogui
import time
import subprocess

time.sleep(4)
pyautogui.click(97, 83)
time.sleep(3)
subprocess.run(["python3", "getsignup.py"])
time.sleep(0.5)
subprocess.run(["python3", "create.py"])
time.sleep(14)


