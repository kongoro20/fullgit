import pyautogui
import time
import os
import sys
import signal

def handle_exit_signal(sig, frame):
    """Handle Ctrl+C by creating the exit signal."""
    print("Ctrl+C detected in runfound.py. Creating exit signal file...")
    with open("exit_signal.txt", "w") as f:
        f.write("exit")
    sys.exit(0)

# Register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, handle_exit_signal)

def wait_for_web_button(image_path='run_button.png', confidence_level=0.8):
    """Continuously wait for the web button to appear and click it once found."""
    print(f"Waiting for {image_path} to appear...")

    while True:
        # Check for the exit signal
        if os.path.exists("exit_signal.txt"):
            print("Exit signal detected in runfound.py. Exiting...")
            sys.exit(0)

        # Check if the button is on the screen
        button_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence_level, grayscale=True)
        if button_location:
            time.sleep(1)
            print(f"{image_path} found at {button_location}. Clicking...")
            sys.exit(0)  # Exit with success once the button is found

        # Brief pause before checking again
        time.sleep(0.5)
        print(f"{image_path} not found, retrying...")

if __name__ == "__main__":
    wait_for_web_button()
