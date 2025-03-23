import pyautogui
import time
import subprocess
import random
import string
import sys
import pyperclip

def type_like_human(text):
    """Simulate human-like typing behavior."""
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(0.05, 0.2))

def generate_random_password():
    """Generate a random password."""
    length = random.randint(9, 12)
    characters = string.ascii_letters + string.digits + "@$./;!#"
    return ''.join(random.choice(characters) for _ in range(length))

# Simulate navigating and interacting with a webpage
pyautogui.click(307, 82)
time.sleep(1)

type_like_human('replit.com')
time.sleep(1)
pyautogui.press('enter')
time.sleep(12)

pyautogui.click(random.randint(114, 343), random.randint(246, 347))
time.sleep(random.uniform(1, 2))

num_presses = random.randint(5, 7)
for _ in range(num_presses):
    pyautogui.press("down")
    time.sleep(random.uniform(0.3, 0.4))

for _ in range(num_presses):
    pyautogui.press("up")
    time.sleep(random.uniform(0.3, 0.4))

time.sleep(1)
pyautogui.click(random.randint(1209, 1255), random.randint(182, 198))

time.sleep(2)
time.sleep(8)
subprocess.run(["python3", "getsignup.py"])
time.sleep(0.5)
subprocess.run(["python3", "create.py"])
time.sleep(14)

def detect_web_button(script_name):
    """Run an external script to detect the web button with up to 15 attempts."""
    attempt = 0
    max_attempts = 15

    while attempt < max_attempts:
        print(f"Detection attempt {attempt + 1}/{max_attempts}...")
        process = subprocess.Popen(['python3', script_name])
        process.wait()  # Wait for the detection script to finish

        if process.returncode == 0:  # Button detected
            print("Web button detected successfully.")
            return True  
        else:
            print("Web button not detected. Retrying...")
            time.sleep(1)
            attempt += 1
            time.sleep(1)

    print("Max detection attempts reached. Proceeding with fallback action...")
    return False 

def generate_random_name():
    """Generate a random name."""
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aoiu"
    
    length = random.randint(6, 8)
    name = ""

    for i in range(length // 2):  
        name += random.choice(consonants)  
        name += random.choice(vowels)  

    return name

def perform_additional_tasks():
    """Tasks to perform after detecting the button."""
    print("Performing additional tasks...")
    time.sleep(1)
    subprocess.run(['python3', 'steps.py'])

    pyautogui.click(477, 42)
    time.sleep(1)
    pyautogui.click(94, 82)
    time.sleep(1.5)
    pyautogui.press("enter")
    time.sleep(3)

if __name__ == "__main__":
    max_cycles = 4
    cycle = 0
    button_detected = False

    while cycle < max_cycles:
        print(f"Starting detection cycle {cycle + 1}/{max_cycles}...")

        # Run the pass_detector.py script to check for the button
        button_detected = detect_web_button('pass_detector.py')

        if button_detected:
            print(f"Button detected in cycle {cycle + 1}. Proceeding to additional tasks.")
            perform_additional_tasks()
            break
        else:
            print(f"Button not detected in cycle {cycle + 1}. Performing fallback click.")
            subprocess.run(['python3', 'retry0.py'])
        
        cycle += 1

    if not button_detected:
        print(f"All {max_cycles} cycles completed without detecting the button.")
        
        # Create stop flag to prevent repl2.py from running
        with open("stop_repl2.flag", "w") as f:
            f.write("stop")

        time.sleep(0.5)
        pyautogui.click(1357, 11)
        time.sleep(1.5)
        sys.exit(1)  # Ensure script exits with an error code so script1.sh also exits
