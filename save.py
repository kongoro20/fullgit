import requests
import subprocess
import time

# Server URL
SERVER_URL = "https://sandbox-a34641e86fbb45e696da6f908e95f21e-ethereum-8070.prod-sandbox.chainide.com/get_item"

def get_item():
    while True:
        try:
            # Request an item from the server
            response = requests.get(SERVER_URL)
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

            data = response.json()
            if "assigned_item" in data:
                item = data["assigned_item"]
                print(f"Received item: {item}")
                
                # Copy item to clipboard using xclip
                subprocess.run(['xclip', '-selection', 'clipboard'], input=item.encode())
                print("Item copied to clipboard.")
                break  # Exit loop once item is successfully retrieved
            else:
                print(f"Error: {data.get('error', 'Unknown error')}")
        except (requests.RequestException, ValueError) as e:
            print(f"Request failed: {e}. Retrying in 2 seconds...")
            time.sleep(2)  # Wait before retrying

if __name__ == "__main__":
    get_item()
