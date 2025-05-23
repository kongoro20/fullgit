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
            pyautogui.click(251, 180)
            time.sleep(1)
            pyautogui.click(285, 176)
            time.sleep(1)
            pyautogui.click(252, 178)
            time.sleep(1)
            subprocess.run(["python3", "repeat1.py"])
            time.sleep(1)

def perform_additional_tasks():
    """Define tasks to perform after the web button is detected."""
    print("Performing additional tasks...")
    time.sleep(1)

if __name__ == "__main__":
    # Step 1: Detect the web button via the detection script
    detect_web_button('trak2.py')

    # Step 2: Perform additional tasks after the web button is detected
    perform_additional_tasks()
