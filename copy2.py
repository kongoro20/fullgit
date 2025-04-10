import pyautogui
import time
import os
import subprocess
# Load the saved email from file
with open("save_email.txt", "r") as f:
    saved_email = f.read().strip()

# Function to simulate human-like typing
def human_typing(text):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(0.05)

time.sleep(1.5)
pyautogui.click(1340, 218)
time.sleep(1)
pyautogui.click(1113, 316)
time.sleep(1)
pyautogui.click(894, 326)
time.sleep(1)

# Type the saved email like a human
human_typing(saved_email)
time.sleep(1)

pyautogui.press('enter')
time.sleep(1.5)
pyautogui.click(478, 179)
time.sleep(1)

# Click at position (288, 181)
pyautogui.click(288, 181)
time.sleep(1)


