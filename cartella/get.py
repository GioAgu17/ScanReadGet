#!/usr/bin/python
# coding=utf-8

import os

import var

def GetPoints(c):
	
	if c == " ":
		var.PointCounter[var.points.index(" ")] += 1
	if c == ",":
		var.PointCounter[var.points.index(",")] += 1
	if c == ";":
		var.PointCounter[var.points.index(";")] += 1
	if c == ":":
		var.PointCounter[var.points.index(":")] += 1
	if c == "'":
		var.PointCounter[var.points.index("'")] += 1
	if c == ".":
		var.PointCounter[var.points.index(".")] += 1
	if c == "?":
		var.PointCounter[var.points.index("?")] += 1
	if c == "!":
		var.PointCounter[var.points.index("!")] += 1
	if c == ">":
		var.PointCounter[var.points.index(">")] += 1
	if c == "<":
		var.PointCounter[var.points.index("<")] += 1
	if c == "-":
		var.PointCounter[var.points.index("-")] += 1
	if c == "+":
		var.PointCounter[var.points.index("+")] += 1
	if c == "*":
		var.PointCounter[var.points.index("*")] += 1
	if c == "\n":
		var.PointCounter[var.points.index("\n")] += 1


def GetWords():		#Potrebbe diventare il main, lo riempio di cicli e condizioni per la lettura di Paragrafi, Frasi, Parole, Punteggiatura, Categorie grammaticali
	new_c = var.ReadChar.read(1)	#In tal caso chiamerebbe le funzioni get frasi dal file
	while new_c != "" :		#Anzichè leggerlo carattere per carattere puoi salvare il libro come stringone e scorrere la stringa
		if new_c not in var.points :
			word = var.word + new_c
			print(word)
		else :
			#SortPoints( new_c )
			var.word = word.lower()
			var.word_number += 1
        
			if var.word not in var.words :
				var.words.append(word)
				var.count.append(1)
			else :
				var.count[var.words.index(var.word)] += 1
			var.word = new_c
			while new_c in var.points :
				new_c = var.ReadChar.read(1)
				var.word = new_c
		new_c = var.ReadChar.read(1)


def CloseInput():
	var.ReadChar.close()



