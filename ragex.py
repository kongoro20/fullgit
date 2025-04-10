import pyautogui
import subprocess
import time
import pyperclip
import re
import sys

# Regular expression for detecting email
EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

def clipboard_contains_email():
    try:
        content = pyperclip.paste()
        if "@" in content:
            match = re.search(EMAIL_REGEX, content)
            return bool(match)
        return False
    except Exception as e:
        print(f"Clipboard read error: {e}")
        return False

while True:
    if clipboard_contains_email():
        print(" Email address found in clipboard!")
        sys.exit(0)

    print("L No email found. Triggering actions...")
    pyautogui.click(98, 82)
    time.sleep(1)
    subprocess.run(["python3", "copy11.py"])
    time.sleep(1)
