from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import subprocess
from game_data import game_pages

app = Flask(__name__)

# Absolute path to the image_downloader.py script in the Docker container
image_downloader_path = os.path.join(os.path.dirname(__file__), 'static', 'images', 'image_downloader.py')

@app.route('/')
def home():
    return render_template('home.html', game_pages=game_pages)

@app.route('/start-download')
def start_download():
    try:
        # Ensure that the script exists before running
        if os.path.exists(image_downloader_path):
            subprocess.run(['python', image_downloader_path], check=True)
            return jsonify({"message": "Download started!"}), 200
        else:
            return jsonify({"message": "Image downloader script not found!"}), 404
    except subprocess.CalledProcessError as e:
        return jsonify({"message": f"Error: {e}"}), 500

# Game name and page portion.
@app.route('/games/<game_name>.html')
def game(game_name):
    if game_name in game_pages:
        return render_template(f'/games/{game_name}.html')
    else:
        return "Game not found", 404


# Game Install Portion - Alpha
@app.route('/install_game', methods=['POST'])
def install_game():
    game_name = request.json.get('game_name')
    if not game_name:
        return jsonify({"error": "Game name is required"}), 400

    docker_compose_file = f'docker-gameserver/dockercompose/docker-compose-{game_name}.yml'
    try:
        subprocess.run(['docker-compose', '-f', docker_compose_file, 'up', '-d'], check=True)
        return jsonify({"status": "Game installed successfully"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Error occurred: {str(e)}"}), 500



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
