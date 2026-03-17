import random
import datetime

# Diese Funktion erzeugt Werte, aber ich möchte jetzt das Datum auch zufällig genereieren

def generate_context():
    """Erzeugt einen zufälligen Login-Kontext für die Risiko-Analyse."""
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
