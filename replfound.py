import pyautogui
import time

# Path to the button image
button_image = 'repldelete_button.png'

# Function to search and click the button if found
def search_and_click_button():
    try:
        # Search for the button image on the screen
        button_location = pyautogui.locateOnScreen(button_image, confidence=0.8)
        
        if button_location:
            print("Button found!")
            
            # Get the center of the button to click
            button_point = pyautogui.center(button_location)
            
            # Click on the button
            pyautogui.click(button_point)
            
            # Sleep for 2 seconds after the click
            time.sleep(2)
        else:
            print("Button not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to search and click
search_and_click_button()
