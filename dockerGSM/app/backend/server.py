from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/api/docker/<action>', methods=['POST'])
def manage_docker(action):
    try:
        if action == 'start':
            # Example: Run a container
            subprocess.run(['docker', 'run', '-d', '--name', 'example', 'nginx'], check=True)
            return jsonify({"message": "Container started!"})
        elif action == 'stop':
            # Example: Stop a container
            subprocess.run(['docker', 'stop', 'example'], check=True)
            subprocess.run(['docker', 'rm', 'example'], check=True)
            return jsonify({"message": "Container stopped and removed!"})
        else:
            return jsonify({"message": "Invalid action"}), 400
    except subprocess.CalledProcessError as e:
        return jsonify({"message": f"Error: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
