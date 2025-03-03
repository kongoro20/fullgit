import pyautogui
import time
import subprocess
import os  # For forced exit
import sys
import signal  # For process cleanup

def cleanup():
    """Function to clean up and kill any lingering processes."""
    print("Cleaning up before exiting...")
    # You can optionally add code to kill subprocesses or background processes here.
    # For example, if you had a subprocess running asynchronously, you could terminate it:
    # subprocess.run(["kill", "<PID>"]) 
    
    # Add any pyautogui cleanup or other cleanup here if necessary

try:
    # Try to locate the shutdown button on the screen
    shutdown_button_location = pyautogui.locateCenterOnScreen('shutdown_button.png', confidence=0.8)
    
    if shutdown_button_location:
        print("Shutdown button detected! Performing actions...")

        time.sleep(1)  # Wait for 1 second
        pyautogui.click(x=1358, y=9)  # Click at (1358,9)

        time.sleep(2)  # Wait for 2 seconds

        # Path to the script (relative or absolute)
        script_path = "./script1.sh"
        print(f"Running script from: {os.path.abspath(script_path)}")

        # Check if the file exists to debug path issues
        if not os.path.exists(script_path):
            print(f"Error: {script_path} does not exist!")
        else:
            print(f"{script_path} exists, running script...")

            # Run the script
            result = subprocess.run(["bash", script_path], check=True)
            print("script1.sh has finished.")

        # Call cleanup before exit
        cleanup()

        # Exit the Python script after running script1.sh
        os._exit(0)  # Fully exit after running the script (immediate exit)

    else:
        print("Shutdown button not found. Exiting script.")
        cleanup()  # Perform any cleanup if needed
        os._exit(0)  # Exit if shutdown button is not found (immediate exit)

except Exception as e:
    print(f"Error detecting shutdown button: {e}")
    print("Exiting without errors.")
    cleanup()  # Perform any cleanup if needed
    os._exit(0)  # Exit safely even if an error occurs
