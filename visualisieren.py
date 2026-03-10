import pandas as pd
import matplotlib.pyplot as plt
import os

def create_reports():
    filename = "login_logs.csv"
    
    if not os.path.exists(filename):
        print("Keine Daten gefunden. Starte erst die Simulation!")
        return

    # Daten laden
    df = pd.read_csv(filename)

    # --- Grafik 1: Risiko pro Standort ---
    plt.figure(figsize=(10, 6))
    df.groupby('location')['risk_score'].mean().sort_values().plot(kind='barh', color='skyblue')
    plt.title('Durchschnittlicher Risiko-Score nach Standort')
    plt.xlabel('Risiko (0-100)')
    plt.ylabel('Standort')
    plt.tight_layout()
    plt.savefig('risk_by_location.png') # Speichert das Bild
    print("Grafik 'risk_by_location.png' erstellt.")

    # --- Grafik 2: MFA Verteilung (Kuchen-Diagramm) ---
    plt.figure(figsize=(8, 8))
    df['mfa_triggered'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightgreen', 'tomato'])
    plt.title('Verhältnis: Direkter Login vs. MFA Abfrage')
    plt.ylabel('')
    plt.savefig('mfa_distribution.png')
    print("Grafik 'mfa_distribution.png' erstellt.")

if __name__ == "__main__":
    create_reports()