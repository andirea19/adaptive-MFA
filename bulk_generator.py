import os
from fake_date import generate_context  # Gekürzte Funktion aus fake_date.py, um den Fokus auf die Logik zu legen
from engine import RiskEngine           # Nutze den Risk-Engine aus engine.py
from logger import SecurityLogger       # Nutzt den Logger aus logger.py, der sich um CSV-Handling kümmert

engine = RiskEngine(threshold=5)
logger = SecurityLogger()

def run_simulation(amount=10):
    print(f"--- Starte Simulation von {amount} Logins ---")
    
    for i in range(amount):
        # 1. Daten generieren
        context = generate_context()
        
        # 2. Risiko berechnen
        score = engine.calculate_score(context)
        mfa_needed = engine.is_mfa_required(score)
        
        logger.log_attempt(context, score, mfa_needed)
        
        print(f"[{i+1}/{amount}] Logged: {context['location']} - Score: {score}")

    print("\n Erfolg! Alle Einträge wurden in 'login_logs.csv' gespeichert.")

if __name__ == "__main__":
    run_simulation(20)