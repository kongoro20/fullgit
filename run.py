import pyautogui
import time
import subprocess
import os
import sys
import signal

def handle_exit_signal(sig, frame):
    """Handle Ctrl+C by creating the exit signal."""
    print("Ctrl+C detected in run.py. Creating exit signal file...")
    with open("exit_signal.txt", "w") as f:
        f.write("exit")
    sys.exit(0)

# Register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, handle_exit_signal)

def check_exit_signal():
    """Check for the exit signal file."""
    if os.path.exists("exit_signal.txt"):
        print("Exit signal detected in run.py. Stopping subprocesses...")
        sys.exit(0)

def detect_web_button(script_name):
    """Run an external script to detect the web button and keep trying until successful."""
    while True:
        # Check for exit signal before starting subprocess
        check_exit_signal()

        # Start the external detection script
        process = subprocess.Popen(['python3', script_name])
        process.wait()  # Wait for it to finish

        if process.returncode == 0:  # Success code indicates the button was found
            print(f"Web button detected and clicked by {script_name}. Proceeding with tasks...")
            return  # Exit the loop and proceed to next tasks
        else:
            print(f"Web button not detected by {script_name}. Retrying...")
            time.sleep(1)
            pyautogui.click(99, 83)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(10)

def perform_additional_tasks():
    """Define tasks to perform after the web button is detected."""
    print("Performing additional tasks...")
    time.sleep(2) 
    print("All tasks completed.")

if __name__ == "__main__":
    # Step 1: Detect the web button via the detection script
    detect_web_button('runfound.py')

    # Step 2: Perform additional tasks after the web button is detected
    perform_additional_tasks()
