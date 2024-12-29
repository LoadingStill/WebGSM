import os
import json
import requests

# Get the absolute path to the current directory (static/images)
current_dir = os.path.dirname(__file__)
json_file = os.path.join(current_dir, 'image_urls.json')  # This ensures the correct path

# Check if the file exists
if not os.path.exists(json_file):
    print(f"File not found: {json_file}")
else:
    # Open and read the JSON file
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            print("Data loaded successfully")
            # Add your code to download the images
            for game, filename, url in data:
                # Download the image
                response = requests.get(url)
                with open(os.path.join(current_dir, filename), 'wb') as img_file:
                    img_file.write(response.content)
                    print(f"Downloaded image and saved as {filename}")
    except FileNotFoundError:
        print(f"File not found: {json_file}")
    except json.JSONDecodeError:
        print("Error decoding JSON")
