import pyautogui
import random
import time
import string
import sys
import subprocess


time.sleep(2)

def generate_password():
    # Ensure at least one character from each category
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice("@.,;!:")

    # Fill the rest of the password randomly to meet the length requirement
    all_chars = string.ascii_letters + string.digits + "@.,;!:"
    remaining_chars = random.choices(all_chars, k=random.randint(5, 8))

    # Combine and shuffle to randomize the order
    password = list(lower + upper + digit + special + ''.join(remaining_chars))
    random.shuffle(password)

    return ''.join(password)

def random_click_in_rectangle(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.moveTo(x, y, duration=random.uniform(0.2, 0.6))
    pyautogui.click()

def random_human_typing(text):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.05, 0.15))

def random_string(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

time.sleep(1)
with open("save_email.txt", "r") as f:
    saved_email = f.read().strip()

time.sleep(0.7)

# Step 1: Type website and press Enter
random_human_typing("www.github.com")
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(15)
subprocess.run(["python3", "git1.py"])
time.sleep(1)
# New Step: Detect the tab button using 'copilot_button.png'
try:
    tab_button_location = pyautogui.locateCenterOnScreen('copilot_button.png', confidence=0.8)
    if tab_button_location is not None:
        print("Copilot button detected, clicking at (1309, 264)...")
        pyautogui.click(1309, 264)
        time.sleep(2)
    else:
        print("Tab button not detected, proceeding to Step 1...")
except Exception as e:
    print(f"Error detecting tab button: {e}")
    print("Proceeding to Step 1...")

time.sleep(1)

# Step 2: Random clicks in one of two rectangles
rect1 = [(97, 344), (242, 562)]
rect2 = [(734, 329), (1240, 509)]
chosen_rect = random.choice([rect1, rect2])
clicks = random.randint(1, 4)
for _ in range(clicks):
    random_click_in_rectangle(chosen_rect[0], chosen_rect[1])
    time.sleep(random.uniform(1, 2))

# Step 3: Click in specific rectangle
random_click_in_rectangle((1264, 270), (1328, 288))
time.sleep(random.uniform(12, 14))
subprocess.run(["python3", "git2.py"])
time.sleep(1)
# Step 4: Click in another rectangle
random_click_in_rectangle((334, 265), (635, 499))
time.sleep(random.uniform(1, 2))

# Step 5: Press down arrow 3 times with delay
for _ in range(3):
    pyautogui.press('down')
    time.sleep(random.uniform(0.1, 0.3))

# Step 6: Click and write clipboard content
random_click_in_rectangle((818, 252), (1213, 260))
time.sleep(random.uniform(0.5, 1))
random_human_typing(saved_email)
time.sleep(random.uniform(0.5, 1))

# Step 7: Click and write random password
random_click_in_rectangle((813, 327), (1218, 348))
time.sleep(random.uniform(0.5, 1))
random_password = generate_password()
random_human_typing(random_password)
time.sleep(random.uniform(1, 2))

# Step 8: Click and write random name
random_click_in_rectangle((811, 446), (1228, 464))
time.sleep(random.uniform(0.5, 1))
name = ''.join(
    random.choice(string.ascii_lowercase) + random.choice('aeiou') for _ in range(random.randint(3, 4))
) + str(random.randint(10, 99))
random_human_typing(name)
time.sleep(random.uniform(2, 3))

random_click_in_rectangle((708, 468), (767, 541))
time.sleep(0.6)
for _ in range(4):
    pyautogui.press('down')
    time.sleep(random.uniform(0.1, 0.3))

time.sleep(0.7)

# Step 9: Final click and wait
random_click_in_rectangle((825, 504), (1215, 526))
time.sleep(random.uniform(3.5, 4.5))
random_click_in_rectangle((1296, 402), (1333, 490))
time.sleep(1)

# --------- NEW BUTTON DETECTION SCRIPT ---------
failed_attempts = 0
max_attempts = 10  # Exit after 10 consecutive failures

while True:
    time.sleep(1)

    try:
        button_location = pyautogui.locateCenterOnScreen('pass_button.png', confidence=0.8, grayscale=True)
        if button_location:
            random_click_in_rectangle((825, 504), (1215, 526))
            time.sleep(2)
            failed_attempts = 0  # Reset failure count when button is found
        else:
            failed_attempts += 1  # Increment failure count

    except pyautogui.ImageNotFoundException:
        failed_attempts += 1  # Increment failure count if image is not found

    if failed_attempts >= max_attempts:
        print("Button not found for 10 consecutive attempts. Exiting.")
        sys.exit()  # Fully exit after 10 consecutive failures
