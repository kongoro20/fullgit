import pyautogui
import time
import subprocess
import random
import string
import pyperclip




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


time.sleep(1)
pyautogui.click(561, 33)
time.sleep(1)
pyautogui.click(random.randint(895, 1028), random.randint(295, 337))
time.sleep(0.8)
    # Perform a random click within a rectangular area (330, 281) to (625, 291)
pyautogui.click(random.randint(333, 632), random.randint(397, 401))
time.sleep(0.5)
pyautogui.click(random.randint(333, 632), random.randint(397, 401))
time.sleep(0.5)
    # Type a random name with human-like typing behavior
random_name = generate_random_name()
type_like_human(random_name)
time.sleep(1)

    # Perform a random click within various rectangular areas
pyautogui.click(random.randint(704, 1018), random.randint(396, 403))
time.sleep(1)

random_name = generate_random_name()
type_like_human(random_name)
time.sleep(1)


pyautogui.click(random.randint(833, 1017), random.randint(480, 517))
time.sleep(1)
pyautogui.click(random.randint(958, 1033), random.randint(556, 570))
time.sleep(4)


pyautogui.click(random.randint(348, 523), random.randint(560, 576))
time.sleep(3)

pyautogui.click(random.randint(931, 1023), random.randint(599, 605))
time.sleep(3)

