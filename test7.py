import pyautogui
import time
import os
import subprocess
import random

# Function to click at a specific location
def click_at(x, y):
    pyautogui.click(x, y)
    print(f"Clicked at ({x}, {y})")

# Function to detect button using an external script
def detect_button_via_script(script_name):
    """Run an external script to detect a button and keep trying until it succeeds."""
    while True:  # Loop until the button is found
        # Start the external script
        process = subprocess.Popen(['python3', script_name])
        process.wait()  # Wait for it to finish

        if process.returncode == 0:  # Check if the button was found
            print(f"Button in {script_name} detected and clicked!")
            return
        else:
            print(f"Button in {script_name} not detected, retrying...")
            time.sleep(1.5)
# Initial delay
time.sleep(3)

# Read the previously generated .py filename from the file
with open("generated_filename.txt", "r") as f:
    random_py_file = f.read().strip()

print(f"Using previously stored filename '{random_py_file}'")
time.sleep(1)
pyautogui.click(1343, 169)
time.sleep(1)

# Type 'shell'
pyautogui.write('shell')
time.sleep(1)

# Press the Down arrow key
pyautogui.press('down')
time.sleep(1)

# Press Enter
pyautogui.press('enter')
time.sleep(1.5)
# Step 9: Click on the location (700, 587)
pyautogui.click(645, 541)
print("Clicked on (700, 587)")
time.sleep(1)
pyautogui.press('enter')
time.sleep(0.7)
# Step 10: Write the command 'python <random_py_file>' to run the previously generated .py file
pyautogui.write(f"python {random_py_file}")
print(f"Typed 'python {random_py_file}'")
time.sleep(1)

# Step 11: Press Enter to run the Python script
pyautogui.press('enter')
print("Pressed Enter")

# Button detection after Step 11
detect_button_via_script('download_button.py')  # Assuming 'download_button.py' handles button detection
time.sleep(7)
# Step 12: Click on the location (1324, 119)
pyautogui.click(26, 128)
print("Clicked on (1324, 119)")
time.sleep(2)
pyautogui.press('enter')
time.sleep(4)
subprocess.run(["python3", "windowtab.py"])
time.sleep(1)
pyautogui.click(random.randint(705, 826), random.randint(168, 200))
time.sleep(1)
# Clean up: Delete 'generated_filename.txt'
if os.path.exists('generated_filename.txt'):
    os.remove('generated_filename.txt')
    print("Deleted 'generated_filename.txt'")
