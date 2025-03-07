import pyautogui
import time
import os
import signal
import subprocess
import sys

def handle_exit_signal(sig, frame):
    """Handle Ctrl+C (SIGINT) by creating an exit signal."""
    print("Ctrl+C detected. Creating exit signal file...")
    with open("exit_signal.txt", "w") as f:
        f.write("exit")
    sys.exit(0)

# Register the signal handler for Ctrl+C (SIGINT)
signal.signal(signal.SIGINT, handle_exit_signal)

def wait_for_exit(script_name):
    """Wait until the specified script exits gracefully."""
    print(f"Waiting for {script_name} to exit...")
    while True:
        time.sleep(1)
        if not is_script_running(script_name):
            print(f"{script_name} has exited.")
            break

def is_script_running(script_name):
    """Check if a script is still running by searching the process list."""
    try:
        output = subprocess.check_output(["pgrep", "-f", script_name], text=True)
        return bool(output.strip())  # Returns True if process found
    except subprocess.CalledProcessError:
        return False  # No process found

def send_exit_signal():
    """Create an exit signal for all scripts to detect and exit."""
    with open("exit_signal.txt", "w") as f:
        f.write("exit")
    print("Exit signal file created.")

def restart_play_sh():
    """Restart run.sh after ensuring all previous scripts have stopped."""
    print("Ensuring all scripts have stopped before restarting run.sh...")

    # Wait for scripts to exit in order
    wait_for_exit("test1.py")
    wait_for_exit("start.sh")
    wait_for_exit("run.sh")
    wait_for_exit("play.sh")

    # Remove exit signal so scripts can restart fresh
    if os.path.exists("exit_signal.txt"):
        os.remove("exit_signal.txt")

    time.sleep(1)
    print("Restarting play.sh...")
    os.execvp("bash", ["bash", "play.sh"])  # Replace current process with run.sh

try:
    # Try to locate the shutdown button on the screen
    shutdown_button_location = pyautogui.locateCenterOnScreen('shutdown_button.png', confidence=0.8)

    if shutdown_button_location:
        print("Shutdown button detected! Performing actions...")

        time.sleep(1)
        pyautogui.click(x=1358, y=9)
        time.sleep(1)
        pyautogui.click(x=1358, y=9)
        time.sleep(0.5)  # Wait for 0.5 seconds before proceeding

        # Send exit signal to gracefully stop all running scripts
        send_exit_signal()

        # Give time for scripts to detect exit signal and exit
        time.sleep(2)

        # Restart run.sh after ensuring all scripts have stopped
        restart_play_sh()

    else:
        print("Shutdown button not found. Exiting script.")

except Exception as e:
    print(f"Error detecting shutdown button: {e}")
