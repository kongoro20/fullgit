import pyautogui
import time
import random

# Helper functions
def random_click_in_area(top_left, bottom_right):
    """Perform a random click within a specified rectangular area."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.click(x, y)

def random_wait(min_time, max_time):
    """Wait for a random amount of time between min_time and max_time seconds."""
    time.sleep(random.uniform(min_time, max_time))

def press_down_arrow_randomly(min_presses, max_presses, delay=0.5):
    """Press the down arrow key a random number of times with a short delay in between."""
    num_presses = random.randint(min_presses, max_presses)
    for _ in range(num_presses):
        pyautogui.press('down')
        time.sleep(delay)

# Function to perform the specified actions
def perform_next_part():
    """Perform the actions for the next part of the script."""
    # Perform a random click in the first area
    random_click_in_area((706, 364), (839, 518))  # Random click
    random_wait(0.5, 1)  # Random wait

    # Press down arrow a random number of times
    press_down_arrow_randomly(8, 10, delay=0.5)

    # Perform a random click in the second area
    random_click_in_area((729, 564), (805, 576))  # Random click
    random_wait(4, 5)  # Random wait

# Run the script
if __name__ == "__main__":
    perform_next_part()
