import pyautogui
import time
import random

time.sleep(2)
# Helper functions
def random_click_in_area(top_left, bottom_right):
    """Perform a random click within a specified rectangular area."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.click(x, y)
    return x, y  # Return the coordinates for reuse

def human_typing(text):
    """Simulate human-like typing."""
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.05, 0.15))

# Function to perform the third part of the script
def perform_third_part():
    """Perform the third part of the script."""
    # Proceed to the next actions
    random_click_in_area((760, 587), (842, 603))  # Random click
    time.sleep(random.uniform(12, 14))

    pyautogui.click(290, 178)  # Click at (290, 178)
    time.sleep(1)
    pyautogui.click(248, 178)  # Click at (248, 178)
    time.sleep(1)

    human_typing("www.outlook.com")  # Type URL
    time.sleep(0.5)
    pyautogui.press('enter')  # Press Enter
    time.sleep(10)
    pyautogui.click(1343, 221)

# Step 2: Sleep for 1 second
    time.sleep(1)

# Step 3: Press Down Arrow 14 times with 0.5-second delay
    for _ in range(14):
        pyautogui.press('down')
        time.sleep(0.5)

# Step 4: Press Enter twice with 0.5-second delay
    for _ in range(2):
        pyautogui.press('enter')
        time.sleep(0.5)

# Step 5: Click again at (1343, 221)
    pyautogui.click(1343, 221)
# Run the script
if __name__ == "__main__":
    perform_third_part()
