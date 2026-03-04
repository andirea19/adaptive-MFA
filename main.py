# ich versuche, die Authentifizierungslogik mit den gefälschten Daten zu kombinieren

from multiprocessing import context

import pyotp
import datetime

# Ich importiere die Funktion, um gefälschte Daten zu haben
from fake_date import generate_fake_data

# Ich binden den Logger ein, damit ich die Login-Versuche protokollieren kann
from logger import SecurityLogger
import logger

SECRET = pyotp.random_base32()
totp = pyotp.TOTP(SECRET)

def calculate_risk(context):
    risk_score = 1

    if context['hour'] < 6 or context['hour'] > 22:
        risk_score += 1
    if context['location'] not in ['Vienna', 'Berlin']:
        risk_score += 1
    if not context['is_known_device']:
        risk_score += 1

    return risk_score

# Jetzt versuche ich einen Login und dessen Bewertung

def start_login():
    print("Starte Login-Prozess...")
    context = generate_fake_data()  
    print(f"Login-Kontext: {context}")
    risk_score = calculate_risk(context)
    print(f"Risikobewertung: {risk_score}")

# wenn das Risiko den Schwellenwert überschreitet, muss ein zusätzlicher Code angegeben werden

    if risk_score >= 2:
        print("Hohe Risikobewertung! Zusätzliche Authentifizierung erforderlich.")
        code = totp.now()
        print(f"Generierter TOTP-Code: {code}")
        user_input = input("Bitte geben Sie den TOTP-Code ein: ")
        if totp.verify(user_input):
            print("Authentifizierung erfolgreich!")
        else:
            print("Authentifizierung fehlgeschlagen!")
    else:
        print("Niedrige Risikobewertung. Kein zusätzlicher Authentifizierungsbedarf.")

# Ich starte den Login-Prozess, wenn das Skript direkt ausgeführt wird
# __name__ == "__main__" ist eine gängige Python-Konvention, um zu überprüfen, ob das Skript direkt ausgeführt wird oder importiert wurde.

if __name__ == "__main__":
    start_login()   

logger = SecurityLogger()
logger.log_attempt(context, risk, True)


