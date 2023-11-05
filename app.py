from flask import Flask, render_template, request, jsonify
import subprocess
import os
import psutil
import time


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/games/cs2')
def cs2_page():
    return render_template('games/cs2.html')


@app.route('/games/factorio')
def factorio_page():
    return render_template('games/factorio.html')


def get_cpu_usage():
    return psutil.cpu_percent(interval=.25)


@app.route('/static/js/cpu_usage.js')
def serve_cpu_usage_js():
    return send_file('static/js/cpu_usage.js')


@app.route('/run-script', methods=['POST'])
def run_script():
    script_path = os.path.join(os.path.dirname(__file__), 'gamesFolder', 'factorio', 'factorioInstall.sh')
    try:
        # Run the shell script and capture the output
        output = subprocess.check_output([script_path], stderr=subprocess.STDOUT, shell=True)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode('utf-8')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
