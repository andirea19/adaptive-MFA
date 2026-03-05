from logger import SecurityLogger
from engine import RiskEngine
import random

# Initialisierung der Werkzeuge
logger = SecurityLogger()
engine = RiskEngine(threshold=5)

def generate_fake_data():
    """Simuliert einen Login-Versuch."""
    return {
        "hour": random.randint(0, 23),
        "location": random.choice(["Berlin", "München", "Unbekannt"]),
        "device_known": random.choice([True, False])
    }

def start_login():
    print("\n--- Smart Auth System ---")
    
    # 1. Daten generieren
    context = generate_fake_data()
    
    # 2. Risiko berechnen (über die Engine)
    risk_score = engine.calculate_score(context)
    mfa_needed = engine.is_mfa_required(risk_score)
    
    print(f"Standort: {context['location']}, Stunde: {context['hour']}")
    print(f"Risiko-Score: {risk_score}")
    
    # 3. Loggen (über den Logger)
    logger.log_attempt(context, risk_score, mfa_needed)
    
    # 4. MFA-Logik
    if mfa_needed:
        print("MFA erforderlich! Bitte Code eingeben...")
    else:
        print("Login ohne MFA erlaubt.")

if __name__ == "__main__":
    start_login()