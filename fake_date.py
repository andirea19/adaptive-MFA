import datetime
import random
import time

# Funktion, um gefälschte Daten zu erstellen, die ich analysieren kann

def generate_fake_data():
    hour = datetime.datetime.now().hour
    location = random.choice(['Sofia', 'Vienna', 'Tokyo', 'Berlin', 'Unbekannt'])

    context = {
#    "data": generate_fake_data(),
    "hour": hour,
    "location": location,
    "is_known_device": random.choice([True, False])
    }
    return context

print(f"Aktueller Login-Versuch: {generate_fake_data()}")
