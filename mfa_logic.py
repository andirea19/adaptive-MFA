import pyotp
import time

# Ich generiere einen geheimen Schlüssel (Base 32)
# Der ist noralerweise einzigartig, aber ich bin ja nur eine Person

secret = pyotp.random_base32()
print("Mein geheimer Schlüssel:", secret) 

pyotp.random_hex()  # returns a 40-character hex-encoded secret
# Hex-encodierte Geheimnisse sind nicht so üblich, aber ich wollte es mal ausprobieren

totp = pyotp.TOTP('base32secret3232')
totp.now() # => '492039'
# Ich werd den aktuellen TOTP-Code generieren, damit ich ihn prüfen kann

totp.verify('492039') # => True
time.sleep(15)
totp.verify('492039') # => False

# ich schaue nach, ob der Code in den letzten 15 Sekunden gültig war
totp.verify('492039', valid_window=1) # => True

# das ergebnis wahr/falsch gebe ich aus
if totp.verify('492039', valid_window=1):
    print("Der Code ist gültig!")
else:    print("Der Code ist ungültig!")    





