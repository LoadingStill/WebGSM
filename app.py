from flask import Flask, render_template, request, jsonify
from game_data import game_pages  # Import the game_pages dictionary

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', game_pages=game_pages)

# Game list is generated at game_data.py
# To add a new game make the html page and needed scripts first then add game at game_data.py last before publishing.
@app.route('/games/<game_name>.html')
def game(game_name):
    if game_name in game_pages:
        return render_template(f'/games/{game_name}.html')
    else:
        return "Game not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
