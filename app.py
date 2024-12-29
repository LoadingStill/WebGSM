from flask import Flask, render_template

app = Flask(__name__)

# List of game names (without the .html extension)
game_pages = ['cs2', 'arma3', 'dst', 'factorio', 'eco', 'minecraftJava']

@app.route('/')
def home():
    return render_template('home.html', game_pages=game_pages)

@app.route('/games/<game_name>.html')
def game(game_name):
    if game_name in game_pages:
        return render_template(f'/games/{game_name}.html')
    else:
        return "Game not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
