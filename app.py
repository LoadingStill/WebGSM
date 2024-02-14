from flask import Flask, render_template, request, jsonify
import subprocess
import os
import psutil
import json
# import paramiko #For SSH
# from flask_socketio import SocketIO #For live updates in SSH


app = Flask(__name__)



# Configuration
GAMES_DIR = 'games'

def read_game_info(game_name):
    file_path = os.path.join(GAMES_DIR, game_name, 'server_info.json')
    with open(file_path) as json_file:
        return json.load(json_file).get("Installed") is False

@app.route('/')
def home():
    games = {
        'arma3': read_game_info('arma3'),
        'cs2': read_game_info('cs2'),
        'factorio': read_game_info('factorio'),
        'dst': read_game_info('dst'),
        'eco': read_game_info('eco'),
        'minecraftjava': read_game_info('minecraftjava')
    }
    return render_template('home.html', games=games)



@app.route('/install_minecraftjava', methods=['POST'])
def install_minecraftjava():
    try:
        # Use sudo to run the script with elevated privileges
        subprocess.run(['sudo', 'bash', '/var/www/webgsm/games/minecraftjava/installMinecraftJava.sh'], check=True)
        return jsonify({'success': True, 'message': 'Installation successful'})
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'message': f'Error: {e}'})


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


@app.route('/get_cpu_usage')
def get_cpu_usage_route():
    cpu_usage = get_cpu_usage()
    return jsonify({'cpu_usage': cpu_usage})


def get_ram_usage():
    return psutil.virtual_memory().percent


@app.route('/get_ram_usage')
def get_ram_usage_route():
    ram_usage = get_ram_usage()
    return jsonify({'ram_usage': ram_usage})


def get_disk_usage():
    return psutil.disk_usage('/').percent


@app.route('/get_disk_usage')
def get_disk_usage_route():
    disk_usage = get_disk_usage()
    return jsonify({'disk_usage': disk_usage})


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
