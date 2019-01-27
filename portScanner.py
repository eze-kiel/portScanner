#!/usr/bin/env python
# coding: utf-8

import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell = True)

adresse = sys.argv[1]
IPAdresse = socket.gethostbyname(adresse)

portMin = sys.argv[2]
portMax = sys.argv[3]

print "#" * 60
print "Scanning en cours sur ", IPAdresse, " des ports ", portMin, " à ", portMax
print "#" * 60

tempsDebut = datetime.now()

try:
    for port in range(int(portMin), int(portMax) + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(2)

        resultat = sock.connect_ex((IPAdresse, port))

        print("test du port {}".format(port))
        sys.stdout.write("\033[F")

        if resultat == 0:
            print ("port {}   ouvert -> {}".format(port, socket.getservbyport(port)))

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
