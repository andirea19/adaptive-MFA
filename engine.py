import datetime

class RiskEngine:
    def __init__(self, threshold=50):
        self.threshold = threshold

    def calculate_score(self, context):
        """
        Analysiert den Kontext und gibt einen Risiko-Score zwischen 0 und 10 zurück.
        """
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