import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib # Zum Speichern des Modells

# Hier möchte ich mit scikit-learn ein Modell erstellen
# Isolation Forest ist ein Algorithmus, der gut für Anomalieerkennung geeignet ist.

def train_security_model():
    # 1. Daten laden
    df = pd.read_csv('login_logs.csv')
    
    # 2. Features vorbereiten (Nur Zahlen!)
    # Wir wandeln Orte in einfache Zahlen um (0, 1, 2...)
    df['location_code'] = df['location'].astype('category').cat.codes
    
    # X sind unsere Trainingsdaten in einem Dataframe: Stunde, Ort, Bekanntes Gerät
    X = df[['hour', 'location_code', 'device_known']]
    
    # 3. Modell erstellen (Isolation Forest)
    # 'contamination' ist die geschätzte Rate an Angriffen (z.B. 5 %)
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(X)
    
    # 4. Modell speichern, damit die engine.py es nutzen kann
    joblib.dump(model, 'security_model.pkl')
    print("AI-Modell trainiert und als 'security_model.pkl' gespeichert!")

if __name__ == "__main__":
    train_security_model()
