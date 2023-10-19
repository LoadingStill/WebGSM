from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # You can add any additional logic here if needed.
    return render_template('home.html')


@app.route('/games/cs2')
def csgo2_page():
    return render_template('games/cs2.html')


@app.route('/games/factorio')
def factorio_page():
    return render_template('games/factorio.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
