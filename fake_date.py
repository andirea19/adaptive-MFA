import random
import datetime

# Reduzierte Daten, ohne Timer und print Aufrufe, um die Logik zu fokussieren

def generate_context():
    """Erzeugt einen zufälligen Login-Kontext für die Risiko-Analyse."""
    locations = ['Sofia', 'Vienna', 'Tokyo', 'Berlin', 'Unbekannt']
    
    return {
        "hour": random.randint(0, 23), # Simuliert verschiedene Uhrzeiten
        "location": random.choice(locations),
        "device_known": random.choice([True, False])
    }
