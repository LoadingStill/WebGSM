from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/games/cs2.html')
def cs2():
    return render_template('/games/cs2.html')  # Ensure this template exists in the templates folder

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
