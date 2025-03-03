import pyautogui
import time

# Sleep for 2 seconds initially
time.sleep(12)

# Press the Tab key 3 times with 0.5-second intervals
for _ in range(2):
    pyautogui.press('tab')
    time.sleep(0.5)

# Press the Right Arrow key
pyautogui.press('right')
time.sleep(0.5)

# Press the Enter key
pyautogui.press('enter')
time.sleep(1.5)
pyautogui.click(1340, 218)
time.sleep(1)
pyautogui.click(1113, 316)
time.sleep(1)
pyautogui.click(894, 326)
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1.5)
pyautogui.click(478, 179)
time.sleep(1)

# Click at position (288, 181)
pyautogui.click(288, 181)
time.sleep(1)

