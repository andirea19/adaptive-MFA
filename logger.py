import csv
import os
import datetime

class SecurityLogger:
    def __init__(self, filename='login_logs.csv'):
        self.filename = filename
        self._prepare_csv()

    def _prepare_csv(self):
        """Erstellt die Datei mit Headern, falls sie nicht existiert."""
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['timestamp', 'hour', 'location', 'device_known', 'risk_score', 'mfa_triggered'])

    def log_attempt(self, context, risk_score, mfa_triggered):
        """Speichert einen neuen Login-Versuch."""
        with open(self.filename, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                context['hour'],
                context['location'],
                context['device_known'],
                risk_score,
                mfa_triggered
            ])
        print(f"-> Log gespeichert in {self.filename}")
