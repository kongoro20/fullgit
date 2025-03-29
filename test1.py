import pyautogui
import time
import random
import subprocess
import os
import signal
import sys

# Function to handle Ctrl+C (SIGINT)
def handle_exit_signal(sig, frame):
    """Handle Ctrl+C by creating the exit signal."""
    print("Ctrl+C detected. Creating exit signal file...")
    with open("exit_signal.txt", "w") as f:
        f.write("exit")
    sys.exit(0)

# Register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, handle_exit_signal)

# Function to check for exit signal (exit_signal.txt)
def check_exit_signal():
    """Check if the exit signal file exists."""
    if os.path.exists("exit_signal.txt"):
        print("Exit signal detected! Terminating test1.py...")
        sys.exit(0)

# Function to run a subprocess and check for exit signal while waiting
def run_subprocess(command):
    process = subprocess.Popen(command)
    
    # Loop to continuously check exit signal while the subprocess is running
    while process.poll() is None:  # `poll()` returns None if the process is still running
        check_exit_signal()
        time.sleep(0.5)  # Check every 0.5 seconds

    return process.returncode  # Return exit code of the subprocess

# Sleep for 3 seconds before starting
time.sleep(3)
check_exit_signal()

# Step 1: Click on the first specified location
pyautogui.click(1343, 126)
print("Clicked on (1343, 126)")
time.sleep(2)
check_exit_signal()
pyautogui.click(1059, 213)
time.sleep(1.5)

# Run windowtab.py while continuously checking for exit signal
run_subprocess(["python3", "windowtab.py"])
time.sleep(1)
check_exit_signal()
pyautogui.click(random.randint(705, 826), random.randint(168, 200))
time.sleep(1)

# Step 2: Randomly click on one of these locations
random_location_1 = random.choice([(23, 258), (36, 259), (46, 257), (54, 257), (64, 258), (75, 257), (90, 256), (104, 256), (131, 257)])
pyautogui.click(random_location_1)
print(f"Clicked randomly on {random_location_1}")
time.sleep(3)
check_exit_signal()

# Step 3: Randomly click on another set of locations
random_location_2 = random.choice([(1230, 201), (1240, 199), (1253, 202), (1264, 201), (1277, 201), (1265, 202)])
pyautogui.click(random_location_2)
print(f"Clicked randomly on {random_location_2}")
time.sleep(2)
check_exit_signal()

random_location_22 = random.choice([(496, 294), (514, 294), (527, 293), (525, 295), (544, 294), (566, 294), (582, 295), (598, 293), (609, 297), (545, 300)])
pyautogui.click(random_location_22)
print(f"Clicked randomly on {random_location_22}")
time.sleep(2)
check_exit_signal()

random_location_33 = random.choice([(329, 376), (353, 376), (377, 378), (412, 381), (447, 378), (466, 376), (513, 383), (564, 385), (516, 376), (601, 378), (660, 379), (702, 378)])
pyautogui.click(random_location_33)
print(f"Clicked randomly on {random_location_33}")
time.sleep(2)
check_exit_signal()

# Step 4: Type "bash" using the keyboard
pyautogui.write('bash')
print("Typed 'bash'")
time.sleep(2)
check_exit_signal()

pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.press('delete')
time.sleep(1)
pyautogui.write('bash')
time.sleep(1.5)
pyautogui.press('down')
time.sleep(1)
pyautogui.press('enter')
print("Pressed Enter")
time.sleep(2)
check_exit_signal()

# Step 7: Navigate using "Tab" key and press Enter
for _ in range(4):
    pyautogui.press('tab')
    time.sleep(1)
    check_exit_signal()

pyautogui.press('enter')
time.sleep(12)
check_exit_signal()

pyautogui.click(822, 195)
print("Clicked on (822, 195)")
time.sleep(2)
check_exit_signal()

# Run run.py while continuously checking for exit signal
run_subprocess(["python3", "run.py"])
time.sleep(1)
check_exit_signal()

# Step 8: Final clicks
pyautogui.click(147, 169)
time.sleep(2)
check_exit_signal()

pyautogui.click(27, 172)
time.sleep(2)
check_exit_signal()

print("test1.py completed successfully.")
