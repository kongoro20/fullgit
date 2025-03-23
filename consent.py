import pyautogui
import time
import subprocess
import random
import string



def detect_web_button(script_name):
    """Run an external script to detect the web button with up to 10 attempts."""
    attempt = 0
    max_attempts = 15

    while attempt < max_attempts:
        print(f"Detection attempt {attempt + 1}/{max_attempts}...")
        process = subprocess.Popen(['python3', script_name])
        process.wait()  # Wait for the detection script to finish

        if process.returncode == 0:  # Success code indicates the button was found
            print("Web button detected successfully.")
            return True  # Exit the loop and return success
        else:
            print("Web button not detected. Retrying...")
            attempt += 1
            time.sleep(2)  # Wait before the next attempt

    print("Max detection attempts reached. Proceeding with fallback action...")
    return False  # Return failure after all attempts



def perform_additional_tasks():
    """Define tasks to perform after the web button is detected."""
    print("Performing additional tasks...")
    time.sleep(2)
    
    

if __name__ == "__main__":
    # Total cycles of detection and fallback
    max_cycles = 2
    cycle = 0

    while cycle < max_cycles:
        print(f"Starting detection cycle {cycle + 1}/{max_cycles}...")

        # Step 1: Detect the web button
        button_detected = detect_web_button('foundo1.py')

        if button_detected:
            # If the button is detected, exit the cycle and perform additional tasks
            print(f"Button detected during cycle {cycle + 1}. Proceeding to additional tasks.")
            perform_additional_tasks()
            break  # Exit the while loop if button is detected
        else:
            # Perform fallback click if the button is not detected after all attempts
            print(f"Button not detected during cycle {cycle + 1}. Performing fallback click.")
            time.sleep(1)
            

        # Increment the cycle counter
        cycle += 1

    # If the script finishes all cycles without detecting the button
    if cycle == max_cycles:
        print(f"All {max_cycles} cycles completed without detecting the button.")
