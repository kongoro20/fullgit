import pyautogui
import time
import os

# Step 1: Sleep for 3 seconds before starting
time.sleep(3)

# Paths to the images of the verification buttons
verif_button_image = 'okko_button.png'
verif1_button_image = 'yeso_button.png'

# Maximum number of detection attempts
max_attempts = 1000

# Check if both image files exist
if not os.path.isfile(verif_button_image):
    print(f"Error: The image file '{verif_button_image}' does not exist.")
if not os.path.isfile(verif1_button_image):
    print(f"Error: The image file '{verif1_button_image}' does not exist.")

# Loop for a maximum number of attempts
for attempt in range(max_attempts):
    print(f"Attempt {attempt + 1} of {max_attempts}: Attempting to detect verification buttons...")

    # Sleep before each detection attempt
    time.sleep(2)

    # Try to detect the first verification button
    button_location = None
    try:
        print(f"Trying to detect: {verif_button_image}")
        button_location = pyautogui.locateOnScreen(verif_button_image, confidence=0.8)
    except Exception as e:
        print(f"Error while detecting '{verif_button_image}': {e}")

    if button_location:
        print(f"'{verif_button_image}' detected at {button_location}, clicking...")
        time.sleep(1)
        pyautogui.click(button_location)
        print(f"'{verif_button_image}' clicked!")
        break

    # Try to detect the second verification button
    try:
        print(f"Trying to detect: {verif1_button_image}")
        button_location = pyautogui.locateOnScreen(verif1_button_image, confidence=0.92)
    except Exception as e:
        print(f"Error while detecting '{verif1_button_image}': {e}")

    if button_location:
        print(f"'{verif1_button_image}' detected at {button_location}, clicking...")
        time.sleep(1)
        pyautogui.click(button_location)
        print(f"'{verif1_button_image}' clicked!")
        break

    print(f"Neither '{verif_button_image}' nor '{verif1_button_image}' detected. Pressing Down Arrow key...")
    

else:
    print("Maximum detection attempts reached. Exiting...")
