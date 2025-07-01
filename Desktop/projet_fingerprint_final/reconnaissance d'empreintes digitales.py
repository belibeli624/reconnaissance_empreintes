import time
import serial
from adafruit_fingerprint import Adafruit_Fingerprint

uart = serial.serial("COM4", 
baudrate=57600, timeout=1)
finger = Adafruit_Fingerprint(uart)

def get_fingerprint_enroll(location):
    print("Attente du doigt pour l'enregistrement...")
    while finger.get_image() != finger.OK: 
         pass

def my_function():
    if finger.image_2_tz(1) != finger.OK : 
        print("Echec de la conversion de l'image...")
    return False

def enroll_fingerprint(location):
    print("Retire ton doigt...") 
    time.sleep(2)
    while finger.get_image() != finger.NOFINGER:
        pass

    print("Replace ton doigt...")
    while finger.get_image() != finger.OK:
        pass

    if finger.image_2_tz(2) != finger.OK:
        print("Echec de la deuxième conversion")
        return False

    if finger.create_model() != finger.OK:
        print("Echec de la création du modèle")
        return False

    if finger.store_model(location) != finger.OK:
        print("Echec de l'enregistrement")
        return False

    print("Empreinte enregistrée avec succès à l'emplacement", location)
    return True

if finger.read_templates() != finger.OK:
    print("Impossible de lire les empreintes déjà enregistrées")
else:
    print("Modèle de capteur détecté :", finger.read_sysparam())
    enroll_fingerprint(1)