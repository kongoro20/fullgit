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

pyautogui.click(1358, 12)
time.sleep(1.5)

# Run the Python script named copy.py
subprocess.run(["python3", "tempmail.py"])
time.sleep(1)
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

time.sleep(15)

def detect_web_button(script_name):
    """Run an external script to detect the web button with up to 10 attempts."""
    attempt = 0
    max_attempts = 10

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


def type_like_human(text):
    """Simulate human-like typing behavior."""
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(0.05, 0.2))


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
    """Define tasks to perform after the web button is detected."""
    print("Performing additional tasks...")
    time.sleep(1)
    pyautogui.click(561, 33)
    time.sleep(1)
    pyautogui.click(random.randint(895, 1028), random.randint(295, 337))
    time.sleep(0.8)
    pyautogui.press("down")
    time.sleep(0.5)
    pyautogui.press("down")
    time.sleep(0.5)
    # Perform a random click within a rectangular area (330, 281) to (625, 291)
    pyautogui.click(random.randint(330, 625), random.randint(281, 291))
    time.sleep(0.5)
    pyautogui.click(random.randint(332, 615), random.randint(280, 291))
    time.sleep(0.5)
    # Type a random name with human-like typing behavior
    random_name = generate_random_name()
    type_like_human(random_name)
    time.sleep(1)

    # Perform a random click within various rectangular areas
    pyautogui.click(random.randint(710, 990), random.randint(280, 288))
    time.sleep(1)

    random_name = generate_random_name()
    type_like_human(random_name)
    time.sleep(1)
    

    pyautogui.click(random.randint(514, 1020), random.randint(361, 375))
    time.sleep(1)

    pyautogui.click(random.randint(340, 1015), random.randint(462, 474))
    time.sleep(1)

    pyautogui.click(random.randint(961, 1030), random.randint(511, 525))
    time.sleep(5)

    pyautogui.click(random.randint(346, 479), random.randint(522, 491))
    time.sleep(2.5)

    # Click on specific points
    pyautogui.click(476, 42)
    time.sleep(1)
    pyautogui.click(97, 84)
    time.sleep(1.5)
    pyautogui.press("enter")
    time.sleep(3)


if __name__ == "__main__":
    # Total cycles of detection and fallback
    max_cycles = 1
    cycle = 0

    while cycle < max_cycles:
        print(f"Starting detection cycle {cycle + 1}/{max_cycles}...")

        # Step 1: Detect the web button
        button_detected = detect_web_button('pass_detector.py')

        if button_detected:
            # If the button is detected, exit the cycle and perform additional tasks
            print(f"Button detected during cycle {cycle + 1}. Proceeding to additional tasks.")
            perform_additional_tasks()
            break  # Exit the while loop if button is detected
        else:
            # Perform fallback click if the button is not detected after all attempts
            print(f"Button not detected during cycle {cycle + 1}. Performing fallback click.")
            subprocess.run(['python3', 'complete1.py'])

        # Increment the cycle counter
        cycle += 1

    # If the script finishes all cycles without detecting the button
    if cycle == max_cycles:
        print(f"All {max_cycles} cycles completed without detecting the button.")
