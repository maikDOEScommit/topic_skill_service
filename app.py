import os    # Für Dateipfade und Verzeichnisoperationen
from data_manager import JsonDataManager  # Importieren der JsonDataManager-Klasse

# Flask-Komponenten importieren
from flask import Flask, jsonify  # Flask für Webserver, jsonify für JSON-Antworten

# Flask-App initialisieren
app = Flask(__name__)
data_manager = JsonDataManager()  # Instanz der JsonDataManager-Klasse erstellen

# Verzeichnisse und Dateipfade festlegen
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')          # Pfad zum 'data'-Verzeichnis
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json')                 # Pfad zur JSON-Datei mit Topics

# Root-Route: Gibt einfachen Begrüßungstext zurück
@app.route('/')
def hello_world():
    return 'Hello from Topic and Skill Service!'


# Route für /topics → gibt Inhalte der JSON-Datei als JSON-Response zurück
@app.route('/topics', methods=['GET'])
def get_topics():
    topics = data_manager.read_data(TOPICS_FILE)
    return jsonify(topics)

# Wenn dieses Skript direkt gestartet wird, Server lokal auf Port 5000 starten
if __name__ == '__main__':
    app.run(debug=True, port=5000)
