import pyautogui
import time
import subprocess

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
            time.sleep(1)
            pyautogui.press("down")
            time.sleep(0.5)      

def perform_additional_tasks():
    """Define tasks to perform after the web button is detected."""
    print("Performing additional tasks...")
    time.sleep(2)
    subprocess.run(["python3", "suitverif.py"])
    time.sleep(4)
    pyautogui.click(478, 42)
    time.sleep(1)
    pyautogui.click(289, 40)
    time.sleep(1)
    pyautogui.write("www.replit.com")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(8)
    try:
        tab_button_location = pyautogui.locateCenterOnScreen('pass_button.png', confidence=0.8)
        if tab_button_location is not None:
            print("Tab button detected, clicking at (1342, 125)...")
            subprocess.run(["python3", "steps.py"])
            time.sleep(2)
        else:
            print("Tab button not detected, proceeding to Step 1...")
    except Exception as e:
        print(f"Error detecting tab button: {e}")  # Fixed indentation here
        print("Proceeding to Step 1...")
    time.sleep(1)
    pyautogui.click(99, 81)
    time.sleep(4)
    pyautogui.click(253, 41)
    time.sleep(1)
    print("All tasks completed.")

if __name__ == "__main__":
    # Step 1: Detect the web button via the detection script
    pyautogui.click(93, 80)
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(4.5)
    detect_web_button('verif3.py')

    # Step 2: Perform additional tasks after the web button is detected
    perform_additional_tasks()
