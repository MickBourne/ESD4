#!/usr/bin/env python
# -*- coding: utf-8 -*-
░░░▄▀▀▀▄░░░░░░░░░░░░░▄▀▀▀▄░░░░░░
░░░█░░░██░░░░░░░░░░░░█░░░█░░░░░░
░░░▀█░░░█░░░░░░░░░░░█▀░░░█░░░░░░
░░░░█░░░▀█▄▄▄▄░▄▄▄▄▄█░░░█▀░░░░░░
░░░░█░░░░██░░▀█▀░░██▀░░▄█░░░░░░░
░░░░░█░░░▀█░░░█░░░██░░░█░░░░░░░░
░░░░░█░░░░█░░░█░░░█░░░░█░░░░░░░░
░░░░▄█░░░░█▄░▄█▄░▄█░░▄█▀▀██▄░░░░
░░░░█░░░░░░▀▀▀▀▀▀▀░░░█▄░░░░█▄░░░
░░░░█░░░░░░░░░░░░░░░░▀█▄▄░░░█░░░
░░░░█░░░░░░░░░░░░░░░░░░░░░░▄█░░░
░░░░█░░░░░░░░░░░░░░░░░░░░░░█░░░░
░░░░░█░░░░░░░░░░░░░░░░░░░▄██░░░░
░░░░░▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄██▀▀▀░░░░░░
░░░░░░█████████████▀░░░░░░░░░░░░
░░░░░░██▀▀█████████░░░░░░░░░░░░░
####################################################################
# --- Mickey Bourne ---
# --- Programme de calculatrice ---
# --- 29/02/2016 --- Bisextille t'as vu
####################################################################


nb1 = int(raw_input("Entrez votre premier nombre : \n"))
op = raw_input("Entrez votre operateur : \n")
nb2 = int(raw_input("Entrez votre deuxième nombre : \n"))
	
if op == "+" :
	res = nb1 + nb2
	print "le resultat est : %s" %res
elif op == "-" :
	res = nb1 - nb2
	print "le resultat est : %s" %res
elif op == "*" :
	res = nb1 * nb2
	print "le resultat est : %s" %res
elif op == "/" :
	res = nb1 / nb2
	print "le resultat est : %s" %res
elif op == "**" :
	res = nb1 ** nb2
	print "le resultat est : %s" %res
else : print "c'est pas une calculatrice que tu cherches"