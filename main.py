from logger import SecurityLogger
from engine import RiskEngine
#from write_fake_date import generate_context
from fake_date import generate_context

# Initialisierung
logger = SecurityLogger()
engine = RiskEngine(threshold=5)

neuer_login = generate_context()

for _ in range(100):
    daten = generate_context()

def start_login():
    print("\n---Mein tolles Smart Auth System ---")
    
    # 1. Daten generieren (jetzt in der externen Datei)
    context = generate_context()
    
    # 2. Risiko berechnen
    risk_score = engine.calculate_score(context)
    mfa_needed = engine.is_mfa_required(risk_score)
    
    print(f"Standort: {context['location']}, Stunde: {context['hour']}")
    print(f"Risiko-Score: {risk_score}")
    
    # 3. Loggen
    logger.log_attempt(context, risk_score, mfa_needed)
    
    # 4. MFA-Logik
    if mfa_needed:
        print("Code erforderlich!")
    else:
        print("Login möglich.")

if __name__ == "__main__":
    start_login()