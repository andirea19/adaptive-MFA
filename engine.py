import datetime
import os

import joblib

class RiskEngine:
    def __init__(self, threshold=5):
        self.threshold = threshold
        self.model_path = 'security_model.pkl'
        self.model = self._load_model()

    def _load_model(self):
        #Versucht das AI-Modell zu laden.
        if os.path.exists(self.model_path):
            try:
                return joblib.load(self.model_path)
            except:
                return None
        return None

    def calculate_score(self, context):
        #Analysiert den Kontext und gibt einen Risiko-Score zwischen 0 und 10 zurück.

        score = 0
        
        # Regel 1: Unbekannter Standort
        if context.get('location') == "Unbekannt":
            score += 5
            
        # Regel 2: Nachtzeit (z.B. 22 bis 5 Uhr)
        hour = context.get('hour', 0)
        if hour < 5 or hour > 22:
            score += 3
            
        # Regel 3: Unbekanntes Gerät
        if not context.get('device_known', True):
            score += 2
            
        # Score deckeln bei 10
        return min(score, 10)
    
    
    def is_mfa_required(self, score):
        """Entscheidet basierend auf dem Schwellenwert, ob MFA nötig ist."""
        return score >= self.threshold
    
 # Hier möchte ich die AI-Logik integrieren
def calculate_ai_score(self, context):
    score = self.calculate_score(context)
    ai_score = 0
    if self.model:
        # Ich bereiten die Daten für das Modell vor
        loc_mapping = {'Berlin': 1, 'Sofia': 2, 'Vienna': 3, 'Tokyo': 4, 'Unbekannt': 5}
        loc_code = loc_mapping.get(context['location'], 5)
        
        features = [[context['hour'], loc_code, int(context['device_known'])]]
        
        # Isolation Forest gibt -1 für Anomalie zurück
        prediction = self.model.predict(features)
        if prediction[0] == -1:
            ai_score = 4  # Die AI hat ein ungewöhnliches Muster erkannt

    total_score = min(score + ai_score, 10)
    return total_score
