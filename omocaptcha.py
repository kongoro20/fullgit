import pyautogui
import time
import pyperclip  # For clipboard handling

time.sleep(2)
# Function to write clipboard content
def write_clipboard_content():
    clipboard_content = pyperclip.paste()  # Retrieve the clipboard content
    if clipboard_content:  # Check if clipboard is not empty
        for char in clipboard_content:
            pyautogui.typewrite(char)  # Simulate typing each character
            time.sleep(0.05)  # Small delay to mimic human typing
    else:
        print("Clipboard is empty. Please copy something before running the script.")

# Function to perform the sequence of actions
def perform_actions():
    # Click at (390, 455)
    pyautogui.click(390, 455)
    time.sleep(1)

    # Press down arrow twice with short sleep in between
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)

    # Click at (749, 600)
    pyautogui.click(749, 600)
    time.sleep(4)

    # Click at (1277, 484)
    pyautogui.click(1277, 484)
    time.sleep(2)

    # Click at (1314, 372)
    pyautogui.click(1314, 372)
    time.sleep(2)

    # Click at (1312, 218)
    pyautogui.click(1312, 218)
    time.sleep(1)

    # Click at (1297, 315)
    pyautogui.click(1297, 315)
    time.sleep(1)

    # Click at (1010, 382)
    pyautogui.click(1010, 382)
    time.sleep(1)

    # Click at (1305, 218)
    pyautogui.click(1305, 218)
    time.sleep(1)

    # Click at (1132, 396)
    pyautogui.click(1074, 419)
    time.sleep(1)

    # Press Ctrl + A
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(2)

    # Write clipboard content
    write_clipboard_content()
    time.sleep(3)

    # Click at (1308, 221)
    pyautogui.click(1308, 221)
    time.sleep(2)

    # Click at (291, 179)
    pyautogui.click(291, 179)
    time.sleep(1)

    # Click at (252, 178)
    pyautogui.click(252, 178)
    time.sleep(2)

# Run the sequence
if __name__ == "__main__":
    perform_actions()
