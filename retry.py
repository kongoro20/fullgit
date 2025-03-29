import pyautogui
import time
import sys

try:
    # Attempt to locate the shutdown button image
    shutdown_button_location = pyautogui.locateCenterOnScreen('shutdown_button.png', confidence=0.8)

    if shutdown_button_location is None:
        print("Shutdown button not found. Proceeding normally...")  # Print a message if button not found
        sys.exit(0)  # Exit normally without failure

    else:
        print("Shutdown button found. Executing fallback actions...")
        time.sleep(1)
        pyautogui.click(x=1358, y=9)
        time.sleep(1)
        pyautogui.click(x=1358, y=9)
        time.sleep(0.5)
        sys.exit(1)  # Exit with failure if button is found

except pyautogui.ImageNotFoundException:
    # If an exception is raised, it means the button is not found
    print("Shutdown button not found (ImageNotFoundException). Proceeding normally...")
    sys.exit(0)  # Exit normally without failure
