import pyautogui
import time
import random
import string
import subprocess
time.sleep(2)

def human_typing(text):
    """Simulate human-like typing."""
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.05, 0.15))

def random_click_in_area(top_left, bottom_right):
    """Perform a random click within a rectangular area."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.click(x, y)

def generate_random_name(length=6):
    """Generate a random name with alternating consonant and vowel."""
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase) - set(vowels))
    name = ""
    for _ in range(length):
        name += random.choice(consonants) + random.choice(vowels)
    return name[:length]

def generate_random_password(length=9):
    """Generate a random password with mixed characters."""
    chars = string.ascii_letters + string.digits + ",;!:@."
    return ''.join(random.choices(chars, k=length))

# Main function
def perform_actions():
    # Write "www.outlook.com"
    human_typing("www.outlook.com")
    time.sleep(0.5)

    # Press Enter
    pyautogui.press('enter')
    time.sleep(4)
    try:
       tab_button_location = pyautogui.locateCenterOnScreen('update_button.png', confidence=0.8)
       if tab_button_location is not None:
           print("Tab button detected, clicking at (1342, 125)...")
           pyautogui.click(1339, 265)
           time.sleep(2)
           pyautogui.click(95, 221)
           time.sleep(4)
       else:
           print("Tab button not detected, proceeding to Step 1...")
    except Exception as e:
        print(f"Error detecting tab button: {e}")
        print("Proceeding to Step 1...")
    time.sleep(10)
    subprocess.run(["python3", "look1.py"])
    # Random clicks in one of two rectangular areas
    area1 = ((61, 347), (307, 540))
    area2 = ((913, 330), (1273, 544))
    chosen_area = random.choice([area1, area2])
    for _ in range(random.randint(1, 4)):
        random_click_in_area(*chosen_area)
        time.sleep(random.uniform(1, 2))

    # Press Down arrow twice with short sleep
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)

    # Random click in specific area
    random_click_in_area((229, 531), (338, 555))
    time.sleep(random.uniform(9, 11))
    subprocess.run(["python3", "look2.py"]) 
    # Click at (251, 180)
    pyautogui.click(251, 180)
    time.sleep(1)
    pyautogui.click(285, 176)
    time.sleep(1)
    pyautogui.click(252, 178)
    time.sleep(1)
    subprocess.run(["python3", "repeat.py"])
    time.sleep(1)
    # Random click in specific areas
    random_click_in_area((732, 498), (834, 512))
    time.sleep(random.uniform(1, 1.5))
    random_click_in_area((737, 536), (825, 567))
    time.sleep(random.uniform(0.5, 1))
    random_click_in_area((514, 502), (692, 510))
    time.sleep(random.uniform(0.5, 1))

    # Write a random name (6-8 characters)
    random_name = generate_random_name(random.randint(6, 8)) + str(random.randint(10, 99))
    human_typing(random_name)
    time.sleep(1)

    # Random click in specific area
    random_click_in_area((760, 572), (849, 590))
    time.sleep(random.uniform(5, 7))

    # Write a random password (9-11 characters)
    random_password = generate_random_password(random.randint(9, 11))
    human_typing(random_password)
    time.sleep(random.uniform(2, 3))
    # Random click in specific area
    random_click_in_area((1003, 292), (1281, 533))
    time.sleep(random.uniform(1, 1.5))

    # Press Down arrow 5-7 times with short sleep
    for _ in range(random.randint(5, 7)):
        pyautogui.press('down')
        time.sleep(random.uniform(0.5, 0.8))

    # Random click in specific area
    random_click_in_area((760, 501), (848, 518))
    time.sleep(random.uniform(4, 5))
    pyautogui.click(647, 473)
    time.sleep(1)
    # Random click in specific area
    random_click_in_area((512, 391), (839, 402))
    time.sleep(random.uniform(1, 2))

    # Write another random name (6-8 characters)
    random_name = generate_random_name(random.randint(6, 8))
    human_typing(random_name)
    time.sleep(random.uniform(0.5, 1))

    # Random click in specific area
    random_click_in_area((516, 445), (831, 450))
    time.sleep(random.uniform(1, 2))

    # Write another random name (6-8 characters)
    random_name = generate_random_name(random.randint(6, 8))
    human_typing(random_name)
    time.sleep(random.uniform(0.5, 1))

    # Random click in specific area
    random_click_in_area((759, 501), (849, 518))
    time.sleep(random.uniform(1, 2))

# Run the sequence
if __name__ == "__main__":
    perform_actions()
