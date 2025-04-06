import pyautogui
import time
import os

# Wait before starting the detection
time.sleep(3)

# Image file paths
verif_button_image = 'ok_button.png'
verif1_button_image = 'okko_button.png'
verif2_button_image = 'yeso_button.png'

# All button images to check
button_images = [verif_button_image, verif1_button_image, verif2_button_image]

# Maximum attempts
max_attempts = 100000

# Verify that all image files exist
for img in button_images:
    if not os.path.isfile(img):
        print(f"Error: The image file '{img}' does not exist.")

# Start detection loop
for attempt in range(max_attempts):
    print(f"\nAttempt {attempt + 1} of {max_attempts}...")

    # Wait before each detection attempt
    time.sleep(2)

    for img_path in button_images:
        try:
            print(f"Looking for: {img_path}")
            location = pyautogui.locateOnScreen(img_path, confidence=0.75)
            if location:
                print(f"Found '{img_path}' at {location}, clicking...")
                time.sleep(1)
                pyautogui.click(location)
                print(f"Clicked '{img_path}' successfully.")
                exit(0)  # Exit after successful click
        except Exception as e:
            print(f"Error detecting '{img_path}': {e}")

    print("No button detected. Pressing Down Arrow key...")
    pyautogui.press("down")

else:
    print("Maximum attempts reached. Exiting...")
