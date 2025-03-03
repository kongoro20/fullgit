import pyautogui
import time
import os
import subprocess
import sys  # Add sys module for exiting with status

time.sleep(3)

# Load the previously generated .sh filename
with open('random_sh_file.txt', 'r') as f:
    random_sh_filename = f.read().strip()

print(f"Restored .sh filename: {random_sh_filename}")

# Step 34: Click on the location (502, 168)
print("Clicked on (502, 168)")

# Step 35: Write "shell" and press Enter
pyautogui.write('shell')
print("Typed 'shell'")
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)

# Step 36: Click on the location (736, 246)
pyautogui.click(736, 246)
print("Clicked on (736, 246)")

# Step 37: Write "bash <random_sh_filename>" and press Enter
pyautogui.write(f'bash {random_sh_filename}')
print(f"Typed 'bash {random_sh_filename}'")
time.sleep(1)
pyautogui.press('enter')
print("Pressed Enter")
time.sleep(10)

# Step 38: Click on the location (599, 165)
pyautogui.click(345, 167)
print("Clicked on (599, 165)")
time.sleep(1)

# Step 39: Write "output" and press Enter
pyautogui.write('output')
print("Typed 'output'")
time.sleep(1)
pyautogui.press('enter')
print("Pressed Enter")
time.sleep(13)

# Check for the VNC button and exit with status 100 if found
try:
    if pyautogui.locateCenterOnScreen('vnc_button.png', confidence=0.8, grayscale=True):
        print("VNC button found. Exiting...")
        pyautogui.click(25, 131)
        time.sleep(2.5)
        pyautogui.press('enter')
        time.sleep(3)
        subprocess.run(['python3', 'deleteworkspace.py'])
        sys.exit(100)  # Exit with status 100 to indicate VNC was found
except pyautogui.ImageNotFoundException:
    print("Image not found, continuing with the script...")

# Step 40: Click on the location (764, 226)
pyautogui.click(501, 270)
print("Clicked on (521, 267)")
time.sleep(1)

# Step 41: Write "tmailor.com" and press Enter
pyautogui.write('https://addons.mozilla.org/en-US/firefox/addon/omocaptcha-auto-solve-captcha/')
print("Typed 'datalore.jetbrains.com'")
pyautogui.press('enter')
print("Pressed Enter")
time.sleep(2)

# Step 42: Click on the location (1319, 172)
pyautogui.click(1340, 168)
time.sleep(1)
pyautogui.write('maximize')
time.sleep(1)
pyautogui.press('enter')
time.sleep(4)
pyautogui.click(479, 179)
time.sleep(2)

if os.path.exists('random_sh_file.txt'):
    os.remove('random_sh_file.txt')
    print("Deleted 'random_sh_file.txt'")

print("Script execution completed.")
