import time
import csv
import os
import datetime

class SecurityLogger:

# mein Speicherort ist eine CSV-Datei, die ich "login_logs.csv" nenne

    def __init__(self, filename='login_logs.csv'):
        self.filename = filename
        self._prepare_csv()

    def _prepare_csv(self):
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['timestamp', 'hour', 'location', 'device_known', 'risk_score', 'mfa_triggered'])

    def log_attempt(self, context, risk_score, mfa_triggered):
        """Speichert einen neuen Login-Versuch."""
# erstelle eine neue Zeile in der CSV-Datei mit den relevanten Informationen
        with open(self.filename, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([

# ich verwende %Y-%m-%d %H:%M:%S, um das Datum und die Uhrzeit im Format Jahr-Monat-Tag Stunde:Minute:Sekunde zu speichern
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                context['hour'],
                context['location'],
                context['device_known'],
                risk_score,
                mfa_triggered
            ])

# ich gebe eine Bestätigung aus, dass der Log gespeichert wurde
        print(f"-> Log gespeichert in {self.filename}")