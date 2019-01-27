#!/usr/bin/env python
# coding: utf-8

import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell = True)

adresse = raw_input("Entre un adresse IP: ")
IPAdresse = socket.gethostbyname(adresse)

portMin = raw_input("Entre le port minimum à scanner: ")
portMax = raw_input("Entre le port maximum à scanner: ")

print "#" * 60
print "Scanning en cours sur ", IPAdresse, " des ports ", portMin, " à ", portMax
print "#" * 60

tempsDebut = datetime.now()

try:
    for port in range(int(portMin), int(portMax) + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultat = sock.connect_ex((IPAdresse, port))

        print("test du port {}".format(port))
        sys.stdout.write("\033[F")

        if resultat == 0:
            print ("port {}   ouvert".format(port))

        sock.close()


except socket.gaierror:
    print "Adresse introuvable"
    sys.exit(0)

except socket.error:
    print "Impossible de se connecter"
    sys.exit(0)

except KeyboardInterrupt:
    tempsAnnul = datetime.now()

    print " >> fin du programme"
    print "port n°", port
    print "temps écoulé: ", tempsAnnul - tempsDebut
    sys.exit(0)

tempsFin = datetime.now()

print ("port {} atteint".format(port))
print "Scan terminé en ", tempsFin - tempsDebut
