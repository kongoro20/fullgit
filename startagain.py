import pyautogui
import time

# Step 1: Sleep for 1 second
time.sleep(1)

# Step 2: Click on (295,42)
pyautogui.click(295, 42)
time.sleep(1)

# Step 3: Click on (252,41)
pyautogui.click(252, 41)
time.sleep(1)

# Step 4: Click on (435,87)
pyautogui.click(435, 87)
time.sleep(0.5)

# Step 5: Type "www.replit.com"
pyautogui.write("www.replit.com", interval=0.1)  # Simulates human-like typing
time.sleep(0.5)

# Step 6: Press Enter
pyautogui.press("enter")
time.sleep(4)
