import pyautogui
import time
import random
import string

time.sleep(3)

try:
    tab_button_location = pyautogui.locateCenterOnScreen('windowtab_button.png', confidence=0.8)
    if tab_button_location is not None:
        time.sleep(1)
        print("Tab button detected, clicking at (1342, 125)...")
        
        time.sleep(1)
    else:
        print("Tab button not detected, proceeding to Step 1...")
except Exception as e:
    print(f"Error detecting tab button: {e}")
    print("Proceeding to Step 1...")
    time.sleep(1)
    pyautogui.click(random.randint(256, 274), random.randint(111, 130)); time.sleep(0.8); pyautogui.press('tab'); time.sleep(0.7); pyautogui.press('enter'); time.sleep(1)
# Step 1: Previous tasks

