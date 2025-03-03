import pyautogui
import time
import subprocess
import random
import string
import pyperclip


def type_like_human(text):
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(0.05, 0.2))

def generate_random_password():
    length = random.randint(9, 12)
    characters = string.ascii_letters + string.digits + "@$./;!#"
    return ''.join(random.choice(characters) for _ in range(length))


def detect_web_button(script_name):
    """Run an external script to detect the web button and keep trying until successful."""
    while True:
        # Start the external detection script
        process = subprocess.Popen(['python3', script_name])
        process.wait()  # Wait for it to finish

        if process.returncode == 0:  # Success code indicates the button was found
            print(f"Web button detected and clicked by {script_name}. Proceeding with tasks...")
            return  # Exit the loop and proceed to next tasks
        else:
            print(f"Web button not detected by {script_name}. Retrying...")
            time.sleep(2)

def perform_additional_tasks():
    """Define tasks to perform after the web button is detected."""
    print("Performing additional tasks...")
    time.sleep(4) 
    subprocess.run(["python3", "emailo.py"])
    time.sleep(1)
    text = pyperclip.paste()
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.05, 0.15))
    time.sleep(1)
    pyautogui.press("tab")
    #subprocess.run(["python3", "password.py"])
    time.sleep(0.7)
    random_password = generate_random_password()
    type_like_human(random_password)
    time.sleep(1)
    print("All tasks completed.")

if __name__ == "__main__":
    # Step 1: Detect the web button via the detection script
    detect_web_button('get.py')

    # Step 2: Perform additional tasks after the web button is detected
    perform_additional_tasks()
    time.sleep(0.7)
    pyautogui.click(random.randint(584, 648), random.randint(462, 542))
    time.sleep(0.5)
    pyautogui.press('down')
    pyautogui.press('down')

