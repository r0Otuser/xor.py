# -*- coding: utf-8 -*-
from hashlib import sha256
entree = input("nom du fichier à chiffrer")
sortie = input("nom du fichier final")

key = input("rentrez la clef")

keyencode = sha256(key.encode('utf-8')).digest()

with open(entree,'rb') as entree2:    # rb : r--> reed , b--> binary
	with open(sortie,'wb') as sortie2:
		compteur = 0;
		while entree2.peek(): # renvoie vrai tant qu'il y a des elements
			c = ord(entree2.read(1))
			i = compteur % len(keyencode)
			b = bytes([c^keyencode[i]])
			sortie2.write(b)
			compteur+=1
