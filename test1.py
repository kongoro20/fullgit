import pyautogui
import time
import random
import subprocess
# Sleep for 3 seconds to give you time before the script starts
time.sleep(3)

# Step 1: Click on the first specified location (1342, 157)
pyautogui.click(1343, 126)
print("Clicked on (1342, 157)")
time.sleep(2)
pyautogui.click(1059, 213)
time.sleep(1.5)
subprocess.run(["python3", "windowtab.py"])
time.sleep(1)
pyautogui.click(random.randint(705, 826), random.randint(168, 200))
time.sleep(1)
subprocess.run(["python3", "retry.py"])
time.sleep(1)
# Step 2: Randomly click on one of these locations: (30,297), (50,297), (61,297), (76,297), (100,299), (120,301), (143,299), (175,299), (93,299)
random_location_1 = random.choice([(23, 258), (36, 259), (46, 257), (54, 257), (64, 258), (75, 257), (90, 256), (104, 256), (131, 257)])
pyautogui.click(random_location_1)
print(f"Clicked randomly on {random_location_1}")
time.sleep(3)

# Step 3: Randomly click on one of these locations: (1230,201), (1240,199), (1253,202), (1264,201), (1277,201), (1265,202)
random_location_2 = random.choice([(1230, 201), (1240, 199), (1253, 202), (1264, 201), (1277, 201), (1265, 202)])
pyautogui.click(random_location_2)
print(f"Clicked randomly on {random_location_2}")
time.sleep(2)
random_location_22 = random.choice([(496, 294), (514, 294), (527, 293), (525, 295), (544, 294), (566, 294), (582,295), (598, 293), (609, 297), (545, 300)])
pyautogui.click(random_location_22)
print(f"Clicked randomly on {random_location_22}")
time.sleep(2)
random_location_33 = random.choice([(329, 376), (353, 376), (377, 378), (412, 381), (447, 378), (466, 376), (513,383), (564, 385), (516, 376), (601, 378), (660, 379), (702, 378)])

pyautogui.click(random_location_33)
print(f"Clicked randomly on {random_location_33}")
time.sleep(2)

# Step 4: Type "bash" using the keyboard
pyautogui.write('bash')
print("Typed 'bash'")
time.sleep(2)
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

# Step 5: Press the down arrow key once
#for _ in range(8):
   # pyautogui.press('down')
    #time.sleep(1)
# Step 6: Press the Enter key
#pyautogui.press('enter')
#time.sleep(2)

# Step 7: Randomly click on one of these locations: 
for _ in range(3):
    pyautogui.press('tab')
    time.sleep(1)

# Press "Enter" key
pyautogui.press('enter')
time.sleep(12)
pyautogui.click(822, 195)
print("Clicked on (934, 339)")
time.sleep(2)
subprocess.run(["python3", "run.py"])
time.sleep(1)
# Step 8: Click on the final specified location (934, 339)
pyautogui.click(147, 169)
time.sleep(2)
pyautogui.click(27, 172)
# TODO: Add more tasks or updates to this step later
