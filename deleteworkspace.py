import pyautogui
import time
import random
import subprocess

# Sleep for 3 seconds before starting
time.sleep(3)

# Click on location (59,131)
pyautogui.click(300, 131)

# Sleep for 3 seconds
time.sleep(4)
subprocess.run(["python3", "windowtab.py"])
time.sleep(1)
pyautogui.click(random.randint(705, 826), random.randint(168, 200))
time.sleep(1)

# Randomly click on these locations (set 1)
locations_set_1 = [
    (23, 258), (36, 259), (46, 257), (54, 257), (64, 258), (75, 257), (90, 256), (104, 256), (131, 257)
]
pyautogui.click(random.choice(locations_set_1))

# Sleep for 2 seconds
time.sleep(2)

# Randomly click on these locations (set 2)
x_min, y_min = 661, 333
x_max, y_max = 940, 352

# Generate random coordinates within the rectangle
random_x = random.randint(x_min, x_max)
random_y = random.randint(y_min, y_max)

# Perform a natural-looking click
pyautogui.moveTo(random_x, random_y, duration=random.uniform(0.5, 1.5))  # Move mouse naturally
pyautogui.click()

# Wait for a random duration between 3 and 4 seconds
time.sleep(random.uniform(3, 4))

x_min, y_min = 1169, 190
x_max, y_max = 1198, 209

# Generate random coordinates within the rectangle
random_x = random.randint(x_min, x_max)
random_y = random.randint(y_min, y_max)

# Perform a natural-looking click
pyautogui.moveTo(random_x, random_y, duration=random.uniform(0.5, 1.5))  # Move mouse naturally
pyautogui.click()
time.sleep(1)
for _ in range(6):
    pyautogui.press('tab')
    time.sleep(0.5)

pyautogui.press('enter')
time.sleep(1)

pyautogui.press('up')
time.sleep(0.5)

pyautogui.press('enter')
time.sleep(1.5)
# Randomly click on these locations (set 3)
# locations_set_3 = [
    # (1187, 395), (1204, 393), (1212, 393), (1225, 395), (1233, 396),
    # (1245, 398), (1248, 393), (1259, 397), (1267, 395), (1219, 396)
# ]
# pyautogui.click(random.choice(locations_set_3))

# Sleep for 2 seconds
time.sleep(2)
subprocess.run(["python3", "replfound.py"])
# Click on location (300,130)
pyautogui.click(300, 130)

# Sleep for 3 seconds
time.sleep(3)
