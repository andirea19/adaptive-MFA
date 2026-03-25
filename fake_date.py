import random
import datetime

# Diese Funktion erzeugt Werte, aber ich möchte jetzt das Datum auch zufällig genereieren
# Ich habe die Logik zu verändert, dass sie realisitische Daten ergibt

def generate_context():
    
    # 1. Zeit-Logik (User:innen arbeiten meistens 08:00 - 18:00)
    if random.random() < 0.8:  # 80% Wahrscheinlichkeit für Arbeitszeit
        hour = random.randint(8, 18)
    else:
        hour = random.randint(0, 23) # 20% für den Rest des Tages

    # 2. Standort-Logik (User ist meistens in Wien)
    if random.random() < 0.9:  
        location = "Vienna"
    else:
        location = random.choice(["Sofia", "Tokyo", "Vienna", "Unbekannt"])

    # 3. Geräte-Logik (Meistens das bekannte Gerät)
    if random.random() < 0.95: 
        device_known = True
    else:
        device_known = False

    # 4. Zufälliges Datum in den letzten 30 Tagen
    heute = datetime.datetime.now()
    zufalls_tage = random.randint(0, 30)
    zufalls_datum = heute - datetime.timedelta(days=zufalls_tage)
    timestamp = zufalls_datum.replace(hour=hour, minute=random.randint(0, 59)).strftime("%Y-%m-%d %H:%M:%S")

    return {
        "timestamp": timestamp,
        "hour": hour,
        "location": location,
        "device_known": device_known
    }

def generate_context():
    # Erzeugt einen zufälligen Login-Kontext für die Risiko-Analyse
    
    locations = ['Sofia', 'Vienna', 'Tokyo', 'Berlin', 'Unbekannt']
    heute = datetime.datetime.now()
    zufalls_tage = random.randint(0, 30)
    zufalls_datum = heute - datetime.timedelta(days=zufalls_tage)
    timestamp = zufalls_datum.replace(hour=random.randint(0, 23), minute=random.randint(0, 59)).strftime("%Y-%m-%d %H:%M:%S")
    
    return {
        "hour": random.randint(0, 23), # Simuliert verschiedene Uhrzeiten
        "location": random.choice(locations),
        "device_known": random.choice([True, False]),
        "date": zufalls_datum.date(),
        "timestamp": timestamp
    }

