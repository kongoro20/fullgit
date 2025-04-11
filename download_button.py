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
            time.sleep(2)

def perform_additional_tasks():
    """Define tasks to perform after the web button is detected."""
    print("Performing additional tasks...")
    time.sleep(8)
    pyautogui.click(26, 128)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(4)
    subprocess.run(["python3", "windowtab.py"])
    time.sleep(1)
    pyautogui.click(random.randint(705, 826), random.randint(168, 200))
    time.sleep(1)
    # Clean up: Delete 'generated_filename.txt'
    if os.path.exists('generated_filename.txt'):
        os.remove('generated_filename.txt')
        print("Deleted 'generated_filename.txt'")
    time.sleep(1)    

if __name__ == "__main__":
    # Step 1: Detect the web button via the detection script
    detect_web_button('downlink.py')

    # Step 2: Perform additional tasks after the web button is detected
    perform_additional_tasks()
