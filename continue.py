import pyautogui
import time
import random
import subprocess
# Hold Shift and press Down Arrow twice with 0.3s delay between presses
pyautogui.keyDown('shift')
for _ in range(2):
    pyautogui.press('down')
    time.sleep(0.6)
pyautogui.keyUp('shift')

# Sleep for 1 second
time.sleep(1.7)

# Press Ctrl + C to copy
pyautogui.hotkey('ctrl', 'c')

# Sleep for 0.5 second
time.sleep(0.7)

# Click at (515, 180)
pyautogui.click(515, 180)

# Sleep for 1 second
time.sleep(1.5)

# Press Ctrl + V to paste
pyautogui.hotkey('ctrl', 'v')

# Sleep for 0.5 second
time.sleep(1)

# Press Ctrl + A to select all text
pyautogui.hotkey('ctrl', 'a')

# Sleep for 0.5 second
time.sleep(1)

# Press Ctrl + C to copy
pyautogui.hotkey('ctrl', 'c')

# Sleep for 0.5 second
time.sleep(1)

# Click at (701, 178)
pyautogui.click(701, 178)

# Sleep for 1 second
time.sleep(1)
pyautogui.click(512, 179)
time.sleep(1)
# Press Ctrl + V to paste
pyautogui.hotkey('ctrl', 'v')

# Sleep for 0.8 second
time.sleep(1)

# Hold Shift and press Left Arrow 8 times with 0.3s delay between presses
pyautogui.keyDown('shift')
for _ in range(8):
    pyautogui.press('left')
    time.sleep(0.7)
pyautogui.keyUp('shift')

# Press Ctrl + C to copy
pyautogui.hotkey('ctrl', 'c')

# Sleep for 0.5 second
time.sleep(1)

# Click at (701, 178)
pyautogui.click(701, 178)

# Sleep for 1 second
time.sleep(1)
pyautogui.click(362, 179)
time.sleep(1)

# Define the rectangular area corners
top_left_x, top_left_y = 808, 456
bottom_right_x, bottom_right_y = 840, 491

# Generate random x and y coordinates within the rectangle
random_x = random.randint(top_left_x, bottom_right_x)
random_y = random.randint(top_left_y, bottom_right_y)

# Move the mouse smoothly to the random position to mimic human behavior
pyautogui.moveTo(random_x, random_y, duration=random.uniform(0.5, 1.2))

# Perform the click
pyautogui.click()

# Wait for a random time between 10 and 12 seconds
time.sleep(random.uniform(1, 2))
pyautogui.hotkey('ctrl', 'v')
time.sleep(random.uniform(10, 12))

time.sleep(1)
def random_click_in_rectangle(top_left, bottom_right):
    """Perform a random click within a given rectangular area."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.moveTo(x, y, duration=random.uniform(0.2, 0.6))
    pyautogui.click()

# Step 1: Perform random click in the first rectangle
random_click_in_rectangle((44, 302), (290, 532))
time.sleep(random.uniform(0.5, 1))

# Step 2: Press down arrow 7 to 9 times with random short delay
for _ in range(random.randint(7, 9)):
    pyautogui.press('down')
    time.sleep(random.uniform(0.5, 0.8))

# Step 3: Perform random click in the second rectangle
random_click_in_rectangle((576, 342), (774, 356))
time.sleep(random.uniform(10, 14))
subprocess.run(["python3", "addtask.py"])
# Step 4: Click on specific points with 2-second delays
pyautogui.click(1353, 146)
time.sleep(2)

pyautogui.click(1323, 122)
time.sleep(5)
pyautogui.click(886, 168)
time.sleep(2)
