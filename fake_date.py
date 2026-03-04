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

# ich lege die generierten Daten in einer Liste ab, damit ich sie später analysiert werden kann

fake_data_list = []
for _ in range(10):
    fake_data_list.append(generate_fake_data())
    time.sleep(1) 
print("Gesammelte gefälschte Daten:")
for data in fake_data_list:
    print(data)     


