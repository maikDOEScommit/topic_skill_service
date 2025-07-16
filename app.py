# Standardbibliotheken importieren
import json  # Für das Lesen und Schreiben von JSON-Dateien
import os    # Für Dateipfade und Verzeichnisoperationen

# Flask-Komponenten importieren
from flask import Flask, jsonify  # Flask für Webserver, jsonify für JSON-Antworten

# Flask-App initialisieren
app = Flask(__name__)

# Verzeichnisse und Dateipfade festlegen
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')          # Pfad zum 'data'-Verzeichnis
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json')                 # Pfad zur JSON-Datei mit Topics

# Root-Route: Gibt einfachen Begrüßungstext zurück
@app.route('/')
def hello_world():
    return 'Hello from Topic and Skill Service!'

# Hilfsfunktion zum Einlesen von JSON-Dateien
def read_json_file(filepath):
    # Wenn Datei nicht existiert, leere Liste zurückgeben
    if not os.path.exists(filepath):
        return []
    
    # Datei lesen und JSON-Inhalt zurückgeben
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    # JSON-Fehler behandeln
    except json.JSONDecodeError:
        print(f"Fehler beim Dekodieren der JSON-Datei: {filepath}. Bitte JSON-Syntax überprüfen!")
        return []
    # Alle anderen Fehler abfangen
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten beim Lesen von {filepath}: {e}")
        return []

# Route für /topics → gibt Inhalte der JSON-Datei als JSON-Response zurück
@app.route('/topics', methods=['GET'])
def get_topics():
    topics = read_json_file(TOPICS_FILE)
    return jsonify(topics)

# Wenn dieses Skript direkt gestartet wird, Server lokal auf Port 5000 starten
if __name__ == '__main__':
    app.run(debug=True, port=5000)
