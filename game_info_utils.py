import json


def get_game_info(game_id):
    with open(f'games/{game_id}/server_info.json') as json_file:
        game_data = json.load(json_file)
        return {
            "name": game_id,
            "installed": not game_data.get("Installed", True)  # Invert the value
        }
    