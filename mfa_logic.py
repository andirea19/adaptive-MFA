import pyotp
import time

# Ich generiere einen geheimen Schlüssel (Base 32)
# Der ist noralerweise einzigartig, aber ich bin ja nur eine Person

secret = pyotp.random_base32()
print("Mein geheimer Schlüssel:", secret)    