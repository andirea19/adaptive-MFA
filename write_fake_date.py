import csv
import os

from fake_date import generate_fake_data
from main import calculate_risk

def log_login_attempt(context, risk_score):
    """Fügt einen einzelnen Login-Versuch der CSV-Datei hinzu."""
    filename = "login_logs.csv"
    file_exists = os.path.isfile(filename)
    
    with open(filename, mode='a', newline='') as f:
        fieldnames = ['hour', 'location', 'is_known_device', 'risk_score']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        # Nur wenn die Datei neu ist, schreiben wir den Header
        if not file_exists:
            writer.writeheader()
            
        writer.writerow({
            "hour": context['hour'],
            "location": context['location'],
            "is_known_device": context['is_known_device'],
            "risk_score": risk_score
        })

def start_login():
    print("\n--- Neuer Login-Versuch ---")
    context = generate_fake_data() 
    risk_score = calculate_risk(context)
    
    print(f"Kontext: {context}")
    print(f"Risiko-Score: {risk_score}")
    
    log_login_attempt(context, risk_score)
    print("Versuch wurde im CSV-Log gespeichert.")

# Zum Testen rufen wir es 5 Mal auf
if __name__ == "__main__":
    for _ in range(5):
        start_login()