import pyautogui
import time
import subprocess
import random
import string
import pyperclip


time.sleep(1.5)
subprocess.run(["bash", "profile1.sh"])
time.sleep(2)
pyautogui.click(478, 44)
time.sleep(1)
pyautogui.click(362, 84)
time.sleep(0.5)
pyautogui.write("www.priyo.email")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(7)

# Run the Python script named copy.py
subprocess.run(["python3", "consent.py"])
time.sleep(1)
subprocess.run(["python3", "copy11.py"])
time.sleep(1)
pyautogui.click(287, 45)
time.sleep(1.8)
pyautogui.click(374, 82)
time.sleep(1)

