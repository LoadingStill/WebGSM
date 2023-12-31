from flask import Flask, render_template, request, jsonify
import subprocess
import os
import psutil
import json
# import paramiko #For SSH
# from flask_socketio import SocketIO #For live updates in SSH


app = Flask(__name__)


@app.route('/')
def home():
    # Read the content of the JSON files for each game
    with open('games/arma3/server_info.json') as arma3_json_file:
        arma3_installed = json.load(arma3_json_file).get("Installed") is False

    with open('games/cs2/server_info.json') as cs2_json_file:
        cs2_installed = json.load(cs2_json_file).get("Installed") is False

    with open('games/factorio/server_info.json') as factorio_json_file:
        factorio_installed = json.load(factorio_json_file).get("Installed") is False

    with open('games/dst/server_info.json') as factorio_json_file:
        dst_installed = json.load(factorio_json_file).get("Installed") is False

    with open('games/eco/server_info.json') as factorio_json_file:
        eco_installed = json.load(factorio_json_file).get("Installed") is False

    with open('games/minecraftjava/server_info.json') as minecraftjava_json_file:
        minecraftjava_installed = json.load(minecraftjava_json_file).get("Installed") is False

    # Pass these variables to the 'home.html' template
    return render_template('home.html', arma3_installed=arma3_installed, cs2_installed=cs2_installed,
                           factorio_installed=factorio_installed, dst_installed=dst_installed,
                           eco_installed=eco_installed, minecraftjava_installed=minecraftjava_installed)


@app.route('/games/cs2')
def cs2_page():
    return render_template('games/cs2.html')


@app.route('/games/factorio')
def factorio_page():
    return render_template('games/factorio.html')


@app.route('/games/minecraftjava')
def minecraftjava_page():
    return render_template('games/minecraftjava.html', title='Minecraft Java Edition')


@app.route('/install_minecraftjava', methods=['POST'])
def install_minecraftjava():
    try:
        # Use sudo to run the script with elevated privileges
        subprocess.run(['sudo', 'bash', '/var/www/webgsm/games/minecraftjava/installMinecraftJava.sh'], check=True)
        return jsonify({'success': True, 'message': 'Installation successful'})
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'message': f'Error: {e}'})


@app.route('/games/eco')
def eco_page():
    return render_template('games/eco.html')


@app.route('/games/dst')
def dst_page():
    return render_template('games/dst.html')


@app.route('/games/arma3')
def arma3_page():
    return render_template('games/arma3.html')


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
