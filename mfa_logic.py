import pyotp
import time

# Ich generiere einen geheimen Schlüssel (Base 32)
# Der ist noralerweise einzigartig, aber ich bin ja nur eine Person

secret = pyotp.random_base32()
print("Mein geheimer Schlüssel:", secret) 

pyotp.random_hex()  # returns a 40-character hex-encoded secret
# Hex-encodierte Geheimnisse sind nicht so üblich, aber ich wollte es mal ausprobieren

totp = pyotp.TOTP('base32secret3232')
totp.now() # => '123456' 
# Ich werd den aktuellen TOTP-Code generieren, damit ich ihn prüfen kann

totp.verify('123456') # => True
time.sleep(15)
totp.verify('123456') # => False

# ich schaue nach, ob der Code in den letzten 15 Sekunden gültig war
totp.verify('123456', valid_window=1) # => True

# das ergebnis wahr/falsch gebe ich aus
if totp.verify('123456', valid_window=1):
    print("Der Code ist gültig!")
else:    print("Der Code ist ungültig!")    

## Ich möchte auch die Zeit bis zum nächsten Code wissen
#print("Zeit bis zum nächsten Code:", totp.interval - time.time() % totp.interval, "Sekunden")

# Ich möchte auch HOTP (HMAC-based One-Time Password) verwenden, das auf einem Zähler basiert, anstatt auf der Zeit. Das wäre nützlich für Geräte ohne Uhrzeit oder für Einmalpasswörter, die nicht zeitabhängig sind.
hotp = pyotp.HOTP('base32secret3232')
print("HOTP Code für Zaehler 0:", hotp.at(0)) # => '000000'
print("HOTP Code für Zaehler 1:", hotp.at(1)) # => '111111'

# Ich überprüfe den HOTP-Code für Zähler 0
if hotp.verify('000000', 0):
    print("Der HOTP-Code für Zaehler 0 ist gueltig!") 
else:
    print("Der HOTP-Code für Zaehler 0 ist ungueltig!")

    






