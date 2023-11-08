from flask import Flask, render_template, request, jsonify
import subprocess
import os
import psutil
import json


app = Flask(__name__)


@app.route('/')
def home():
    # Read the content of the JSON files for each game
    with open('games/arma3/server_info.json') as arma3_json_file:
        arma3_installed = json.load(arma3_json_file).get("Installed") == False

    with open('games/cs2/server_info.json') as cs2_json_file:
        cs2_installed = json.load(cs2_json_file).get("Installed") == False

    with open('games/factorio/server_info.json') as factorio_json_file:
        factorio_installed = json.load(factorio_json_file).get("Installed") == False

    with open('games/dst/server_info.json') as factorio_json_file:
        dst_installed = json.load(factorio_json_file).get("Installed") == False

    with open('games/eco/server_info.json') as factorio_json_file:
        eco_installed = json.load(factorio_json_file).get("Installed") == False

    with open('games/minecraftJava/server_info.json') as minecraftJava_json_file:
        minecraftJava_installed = json.load(minecraftJava_json_file).get("Installed") == False

    # Pass these variables to the 'home.html' template
    return render_template('home.html', arma3_installed=arma3_installed, cs2_installed=cs2_installed,
                           factorio_installed=factorio_installed, dst_installed=dst_installed,
                           eco_installed=eco_installed, minecraftJava_installed=minecraftJava_installed)


@app.route('/games/cs2')
def cs2_page():
    return render_template('games/cs2.html')


@app.route('/games/factorio')
def factorio_page():
    return render_template('games/factorio.html')


@app.route('/games/minecraftJava')
def minecraftJava_page():
    return render_template('games/minecraftJava.html', title='Minecraft Java Edition')


@app.route('/install_factorio', methods=['POST'])
def install_factorio():
    game = request.form.get('game')

    if game == 'factorio':
        try:
            subprocess.run(['chmod', '+x', 'games/factorio/installFactorio.sh'], check=True)
            subprocess.run(['games/factorio/installFactorio.sh'], check=True)
            return "Factorio installation started."
        except subprocess.CalledProcessError as e:
            return f"Error: {e.returncode}, {e.output.decode()}"
    else:
        return "Invalid game specified."


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


def get_network_percent():
    return psutil.network_percent(interval=1)


@app.route('/get_network_percent')
def get_network_percent_route():
    network_percent = get_network_percent()
    return jsonify({'network_percent': network_percent})


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
