import unittest
from engine import RiskEngine

class TestRiskEngine(unittest.TestCase):

    def __init__(self, model_path='security_model.pkl', threshold=50):
        self.threshold = threshold

    def setUp(self):
        """Wird vor jedem einzelnen Test ausgeführt."""
        # Wir initialisieren die Engine ohne AI-Modell für die Basis-Tests
        self.engine = RiskEngine(model_path='non_existent.pkl', threshold=5)
        self.engine = RiskEngine(threshold=5)

    def test_safe_login(self):
        """Testet einen normalen Login (sollte 0 Risiko haben)."""
        context = {
            'hour': 12,
            'location': 'Berlin',
            'device_known': True
        }
        assessment = self.engine.analyze(context)
        self.assertEqual(assessment.total_score, 0, "Sicherer Login sollte Score 0 haben")

    def test_unknown_location(self):
        """Testet Risiko bei unbekanntem Standort."""
        context = {
            'hour': 12,
            'location': 'Unbekannt',
            'device_known': True
        }
        assessment = self.engine.analyze(context)
        self.assertGreaterEqual(assessment.total_score, 4)

    def test_mfa_threshold(self):
        #Prüft, ob die MFA-Entscheidung korrekt gefällt wird.
        # Score von 7 (Unbekannt + Unbekanntes Gerät)
        context = {
            'hour': 12,
            'location': 'Unbekannt',
            'device_known': False
        }
        assessment = self.engine.analyze(context)
        mfa_required = self.engine.is_mfa_required(assessment.total_score)
        self.assertTrue(mfa_required, "Bei Score 7 sollte MFA aktiv sein")

if __name__ == '__main__':
    unittest.main()
