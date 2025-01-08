import requests
import random
import json
import time
import threading

# Dateien mit der Wortliste und User-Agent-Liste
wortliste_datei = 'diceware-dereko.txt'
useragents_datei = 'useragents.json'

# Lese die User-Agent-Liste aus der JSON-Datei
with open(useragents_datei, 'r', encoding='utf-8') as file:
    user_agents_data = json.load(file)
    user_agents = [entry['ua'] for entry in user_agents_data]

# Lese die Wortliste aus der Datei und extrahiere nur die Wörter
with open(wortliste_datei, 'r', encoding='utf-8') as file:
    wortliste = [line.split('\t')[1] for line in file.read().splitlines()]

def zufaellige_suche():
    while not stoppen:
        # Wähle zufällig zwei Wörter aus
        wort1 = random.choice(wortliste)
        wort2 = random.choice(wortliste)

        # Erstelle die Suchanfrage
        suche = f"{wort1} {wort2}"

        # Wähle zufällig Google oder Wikipedia
        suchmaschine = random.choice(['google', 'wikipedia'])

        if suchmaschine == 'google':
            url = f"https://www.google.com/search?q={suche}"
        else:
            url = f"https://en.wikipedia.org/wiki/{suche.replace(' ', '_')}"

        # Wähle zufällig einen User-Agent aus der Liste
        user_agent = random.choice(user_agents)

        # Setze den User-Agent-Header
        headers = {
            'User-Agent': user_agent
        }

        # Führe die Anfrage aus und deaktiviere die Zertifikatsüberprüfung
        try:
            response = requests.get(url, headers=headers, verify=False)
            # Überprüfe den Statuscode der Antwort
            if response.status_code == 200:
                print(f"Anfrage an {suchmaschine} war erfolgreich.")
            else:
                print(f"Anfrage an {suchmaschine} fehlgeschlagen mit Statuscode: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Anfrage an {suchmaschine} fehlgeschlagen: {e}")

        # Warte für einen zufälligen Zeitraum zwischen 1 und 30 Minuten
        wartezeit = random.randint(1 * 60, 30 * 60)  # Zeit in Sekunden
        time.sleep(wartezeit)

# Funktion zum Beenden des Skripts
def beenden():
    global stoppen
    input("Geben Sie 'Stopp' ein, um das Skript zu beenden: ")
    stoppen = True

# Hauptprogramm
stoppen = False

# Starte den Such-Thread
such_thread = threading.Thread(target=zufaellige_suche)
such_thread.start()

# Warten auf Stopp-Eingabe
beenden()

# Warten, bis der Such-Thread beendet ist
such_thread.join()

print("Das Skript wurde beendet.")
