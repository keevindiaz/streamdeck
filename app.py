from flask import Flask, send_from_directory, request, jsonify
import subprocess
import speedtest
import os

app = Flask(__name__, static_folder='frontend')

# 🏠 Página principal
@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

# 📁 Archivos estáticos
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('frontend', path)

# ⚙️ Ejecutar comandos (solo en local)
@app.route('/command')
def command():
    if os.getenv("RENDER"):
        return 'Comando no disponible en servidor', 403

    cmd = request.args.get('cmd')
    actions = {
        'chrome': 'start chrome',
        'spotify': 'start spotify',
        'obs': 'start obs64',
        'folder': 'explorer.exe',
        'notepad': 'notepad.exe',
        'settings': 'start ms-settings:',
        'lock': 'rundll32.exe user32.dll,LockWorkStation',
        'restart': 'shutdown /r /t 0'
    }
    if cmd in actions:
        subprocess.Popen(actions[cmd], shell=True)
        return f'Comando ejecutado: {cmd}'
    return 'Comando no reconocido', 400

# 📶 Velocidad de red
@app.route('/speed')
def speed():
    st = speedtest.Speedtest()
    download = round(st.download() / 1_000_000, 2)
    return jsonify({'download': download})

# 🧠 Estado del entorno
@app.route('/status')
def status():
    env = "Render" if os.getenv("RENDER") else "Local"
    return jsonify({'entorno': env})

# 🔁 Compatibilidad local
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
