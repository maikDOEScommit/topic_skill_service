# Importiert Modul für JSON-Dateien
import json

# Importiert das Modul für Dateisystem-Operationen (z. B. Existenz prüfen, Ordner erstellen)
import os


# Definiert Klasse zum Verwalten von JSON-Daten
class JsonDataManager:

    # Konstruktor der Klasse (wird beim Erstellen eines Objekts aufgerufen)
    def __init__(self):
        pass  # Der Konstruktor macht aktuell nichts...

    # Methode zum Lesen von Daten aus einer JSON-Datei
    def read_data(self, filepath):
        # Überprüft, ob die Datei existiert
        if not os.path.exists(filepath):
            return []  # Wenn nicht, wird leere Liste zurückgegeben

        try:
            # Öffnet Datei im Lesemodus mit UTF-8-Encoding
            with open(filepath, 'r', encoding='utf-8') as file:
                return json.load(file)  # Parst und gibt den Inhalt der Datei als Python-Objekt zurück
        except json.JSONDecodeError:
            # Wenn Fehler bei der JSON-Syntax auftritt
            print(f"Fehler beim Dekodieren der JSON-Datei: {filepath}. Bitte JSON-Syntax überprüfen!")
            return []
        except Exception as e:
            # Allgemeiner Fehlerfang für alle anderen Probleme
            print(f"Ein unerwarteter Fehler ist aufgetreten beim Lesen von {filepath}: {e}")
            return []
