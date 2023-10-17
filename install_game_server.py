import subprocess
import json
import random
import string


# Function to generate a random password
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

    # Function to install a game server


def install_game_server(game_name):
    # Define the game-specific folder path
    game_folder = f"./{game_name}"

    try:
        # Read game-specific account data from the account.json file
        account_file = f"{game_folder}/account.json"
        with open(account_file, 'r') as json_file:
            account_data = json.load(json_file)

        username = account_data["username"]
        password = account_data["password"]

        # Generate a random password if it's empty
        if not password:
            password = generate_random_password()
            account_data["password"] = password
            # Update the account.json file with the new password
            with open(account_file, 'w') as json_file:
                json.dump(account_data, json_file, indent=4)
    except FileNotFoundError:
        print(f"Game '{game_name}' is not supported or the account.json file doesn't exist.")
        return

    # Download linuxgsm.sh and run the installer
    subprocess.run(["wget", "-O", "linuxgsm.sh", "https://linuxgsm.sh"])
    subprocess.run(["chmod", "+x", "linuxgsm.sh"])
    subprocess.run(["bash", "linuxgsm.sh", game_name])

    # Run the installer
    subprocess.run([f"./{game_name}", "install"])