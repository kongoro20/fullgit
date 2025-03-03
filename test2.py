import pyautogui
import time
import random
import string
import os

# Function to generate a random 5-character string for .sh filename
def generate_random_filename(extension):
    letters = string.ascii_lowercase
    random_name = ''.join(random.choice(letters) for _ in range(5)) + extension
    return random_name

# Sleep for 1 second before the next action
time.sleep(3)

# Step 9: Click on the location (376, 171)

# Step 10: Click on the location (208, 209)
pyautogui.click(211, 172)
print("Clicked on (208, 209)")
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)

# Step 11: Write a random name with 5 alphabetic characters and '.sh' extension
random_sh_file = generate_random_filename('.sh')

# Save the .sh filename to a file for later use
with open('random_sh_file.txt', 'w') as f:
    f.write(random_sh_file)

pyautogui.write(random_sh_file)
print(f"Typed random name '{random_sh_file}'")
time.sleep(1)

# Step 12: Press Enter key
pyautogui.press('enter')
print("Pressed Enter")
time.sleep(1)

# Step 13: Run the command to copy the content of profile.sh to the clipboard
os.system('xclip -sel clip < profile.sh')
print("Ran command: xclip -sel clip < profile.sh")
time.sleep(2)
pyautogui.click(562, 346)
time.sleep(1)
# Step 14: Press Ctrl+V to paste the clipboard contents
pyautogui.hotkey('ctrl', 'v')
print("Pressed Ctrl+V to paste")
time.sleep(4)

# Step 15: Click on the location (677, 170)
pyautogui.click(434, 169)
time.sleep(1)
pyautogui.click(434, 169)
time.sleep(1)
# Step 16: Click on the location (208, 206)
pyautogui.click(211, 172)
print("Clicked on (208, 209)")
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)
# Step 17: Generate a random name with 5 alphabetic characters and '.py' extension
random_py_file = generate_random_filename('.py')
pyautogui.write(random_py_file)
print(f"Typed random name '{random_py_file}'")

# Store the generated .py filename in a file for later use
with open("generated_filename.txt", "w") as f:
    f.write(random_py_file)

print(f"Stored '{random_py_file}' in generated_filename.txt")
time.sleep(1)

# Step 18: Press Enter key
pyautogui.press('enter')
print("Pressed Enter")
time.sleep(2)

# Step 19: Run the command xclip -sel clip < upload.py
os.system('xclip -sel clip < upload.py')
print("Ran command: xclip -sel clip < upload.py")
time.sleep(2)
pyautogui.click(562, 346)
time.sleep(1)
# Step 20: Press Ctrl+V to paste the clipboard contents
pyautogui.hotkey('ctrl', 'v')
print("Pressed Ctrl+V to paste")
time.sleep(4)
pyautogui.click(427, 170)
time.sleep(1)
pyautogui.click(434, 169)
time.sleep(1)
pyautogui.click(211, 172)
print("Clicked on (208, 209)")
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('code.txt')
time.sleep(1)
pyautogui.press('enter')
print("Pressed Enter")
time.sleep(2)
pyautogui.click(562, 346)
time.sleep(2)
pyautogui.write('88SAqRcXT4hXnxMuBSFJFDUCLRNWLz0irDYG')
time.sleep(4)

# Step 21: Click on the location (677, 170)
pyautogui.click(427, 170)
print("Clicked on (677, 170)")
time.sleep(1)
pyautogui.click(434, 169)
time.sleep(1)

print("Script execution completed.")
