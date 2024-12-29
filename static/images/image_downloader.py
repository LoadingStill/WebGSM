import os
import json
import requests

# Path to the JSON file containing the game data
json_file = 'image_urls.json'

# Folder where images will be saved
save_folder = './static/images'

# Ensure the save folder exists
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Function to download and save the image
def download_image(image_url, save_path):
    try:
        # Send a GET request to the image URL
        response = requests.get(image_url)
        # Check if the request was successful
        if response.status_code == 200:
            # Open the file in write-binary mode and save the content
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded image and saved as {save_path}")
        else:
            print(f"Failed to download {image_url}, status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {image_url}: {e}")

# Load the JSON file containing the image URLs
with open(json_file, 'r') as file:
    game_data = json.load(file)

# Iterate over each entry in the JSON data
for game in game_data:
    game_name, rename_to, image_url = game
    save_path = os.path.join(save_folder, rename_to)
    download_image(image_url, save_path)
