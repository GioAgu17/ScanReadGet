#!/usr/bin/python
# coding=utf-8

import os

#Naive method of defining variables
#Import nomefile, next step
#Counters

points = [" ", ",", ";", ":", "'", ".", "?", "!", ">", "<", "-", "+", "*", "\n"]
PointCounter = [0]*len(points)

def SortPoints(new_c):
	
	if new_c == " ":
		PointCounter[points.index(" ")] += 1
	if new_c == ",":
		PointCounter[points.index(",")] += 1
	if new_c == ";":
		PointCounter[points.index(";")] += 1
	if new_c == ":":
		PointCounter[points.index(":")] += 1
	if new_c == "'":
		PointCounter[points.index("'")] += 1
	if new_c == ".":
		PointCounter[points.index(".")] += 1
	if new_c == "?":
		PointCounter[points.index("?")] += 1
	if new_c == "!":
		PointCounter[points.index("!")] += 1
	if new_c == ">":
		PointCounter[points.index(">")] += 1
	if new_c == "<":
		PointCounter[points.index("<")] += 1
	if new_c == "-":
		PointCounter[points.index("-")] += 1
	if new_c == "+":
		PointCounter[points.index("+")] += 1
	if new_c == "*":
		PointCounter[points.index("*")] += 1
	if new_c == "\n":
		PointCounter[points.index("\n")] += 1

def PrintPoints():
	WritePoints.write( "\nNumber of blank spaces =  :  " + str( PointCounter[points.index(" ")] ))
	WritePoints.write( "\nNumber of commas =  :  " + str( PointCounter[points.index(",")] ))
	WritePoints.write( "\nNumber of semicolumns =  :  " + str( PointCounter[points.index(";")] ))
	WritePoints.write( "\nNumber of columns =  :  " + str(PointCounter[points.index(":")] ))
	WritePoints.write( "\nNumber apostrophes =  :  " + str( PointCounter[points.index("'")] ))
	WritePoints.write( "\nNumber of dots =  :  " + str( PointCounter[points.index(".")] ))
	WritePoints.write( "\nNumber of question marks =  :  " + str( PointCounter[points.index("?")] ))
	WritePoints.write( "\nNumber of exclamations marks =  :  " + str( PointCounter[points.index("!")] ))
	WritePoints.write( "\nNumber of greater then =  :  " + str( PointCounter[points.index(">")] ))
	WritePoints.write( "\nNumber of lower then =  :  " + str( PointCounter[points.index("<")] ))
	WritePoints.write( "\nNumber of minus signs =  :  " + str( PointCounter[points.index("-")] ))
	WritePoints.write( "\nNumber of plus signs =  :  " + str( PointCounter[points.index("+")] ))
	WritePoints.write( "\nNumber of stars =  :  " + str( PointCounter[points.index("*")] ))
	WritePoints.write( "\nNumber of new lines =  :  " + str( PointCounter[points.index("\n")] ))	

##########################################################################################################################
ReadBook = open("../prova.txt", "r")

book = ReadBook.read()
ReadBook.close()

print( "\n\nScanReadGet Versione 1.0\n\nLettura del file\nText analysed:\n\n" )
print( book )







ReadChar = open("../prova.txt", "r")
WritePoints = open("point_frequency.txt", "w")

new_c = ReadChar.read(1)
word = ""
words = []
count =[]


word_number = 0 #conta il totale delle parole

while new_c != "" :
    
    if new_c not in points :
        word = word + new_c
    else :
	SortPoints( new_c )
        word = word.lower()
        word_number += 1
        
        if word not in words :
            words.append(word)
            count.append(1)
            
        else :
            count[words.index(word)] += 1
        
        word = new_c
        
        while new_c in points :
            new_c = ReadChar.read(1)
            word = new_c
    
    new_c = ReadChar.read(1)

PrintPoints()

WordFrequency = open("result.txt", "w")
WordFrequency.write ( book )
WordFrequency.write ( "\n" )

for w, f in zip(words, count) :
    if f > 1 :
        print ("La parola ", w, "è comparsa ", f, "volte")
        WordFrequency.write ("La parola %s e' comparsa %u volte\n" % ( w, f ) ) #string formatting operator
    else :
        print ("La parola ", w, "è comparsa ", f, "volta")
        WordFrequency.write ("La parola %s e' comparsa %u volta\n" % ( w, f ) ) #string formatting operator        
        

print (len(words))
WordFrequency.write ( str( len( words ) ) + '\n' )#write accetta solo stringhe, str(num) trasforma un numero in stringa
print ( "Number of words in file:  ", word_number)#word number è di fatto inutile
WordFrequency.write ( "Number of words in file:  " + str(word_number) + '\n' )
prop = word_number / len( words )
perc = len( words ) / word_number
print ( "Proportion? of words:  ", str(prop), '\n' )
print( "Percentage? of words:  ", str(perc), '\n' )
WordFrequency.write ( "Proportion? of words:  " + str(prop) + '\n' )
WordFrequency.write ( "Percentage? of words:  " + str(perc) + '\n' )
    


"""Problemi riscontrati:
       caratteri non ascii:
           accenti
           simboli strani
       apostrofi
       inizializzare variabili
       inserimento da tastiera del file
       tabella risultati, come riutilizzarli
       ordine alfabetico o di uscita

Miglioramenti possibili
	Separazione in file, scrivere le funzioni dopo un main
	Riorganizzare gli stampa
	Creare un sistema a cartelle per la stampa
	Leggere da internet
	Migliorare la stampa
	Lettura caratteri da file
"""








