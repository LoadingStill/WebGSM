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


@app.route('/install_factorio', methods=['POST'])
def install_factorio():
    game = request.form.get('game')

    if game == 'factorio':
        try:
            subprocess.run(['chmod', '+x', 'games/factorio/installFactorio.sh'], check=True)
            result = subprocess.run(['games/factorio/installFactorio.sh'], check=True, text=True, capture_output=True)
            output = result.stdout
            return f"Factorio installation started. Output: {output}"
        except subprocess.CalledProcessError as e:
            return f"Error: {e.returncode}, {e.output.decode()}"
    else:
        return "Invalid game specified."


def get_cpu_usage():
    return psutil.cpu_percent(interval=.25)


@app.route('/get_cpu_usage')
def get_cpu_usage_route():
    cpu_usage = get_cpu_usage()
    return jsonify({'cpu_usage': cpu_usage})


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
