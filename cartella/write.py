#!/usr/bin/python
# coding=utf-8

import os

import var
import stats

def PrintIntro():
	print( "\n\nScanReadGet Versione 1.0\n\nLettura del file\nText analysed:\n\n" )
	print( var.book )



def PrintBook():
	var.WriteBook.write (var.book )
	var.WriteBook.write ( "\n" )


def PrintWords():
	for w, f in zip(var.words, var.count) :
		if f > 1 :
			print ("La parola ", w, "e' comparsa ", f, "volte")
			var.WriteWords.write ("La parola %s e' comparsa %u volte\n" % ( w, f ) ) #string formatting operator
		else :
			print ("La parola ", w, "e' comparsa ", f, "volta")
			var.WriteWords.write ("La parola %s e' comparsa %u volta\n" % ( w, f ) ) #string formatting operator        

def PrintPoints():
	var.WritePoints.write( "\nNumber of blank spaces =  :  " + str( var.PointCounter[var.points.index(" ")] ))
	var.WritePoints.write( "\nNumber of commas =  :  " + str( var.PointCounter[var.points.index(",")] ))
	var.WritePoints.write( "\nNumber of semicolumns =  :  " + str( var.PointCounter[var.points.index(";")] ))
	var.WritePoints.write( "\nNumber of columns =  :  " + str( var.PointCounter[var.points.index(":")] ))
	var.WritePoints.write( "\nNumber apostrophes =  :  " + str( var.PointCounter[var.points.index("'")] ))
	var.WritePoints.write( "\nNumber of dots =  :  " + str( var.PointCounter[var.points.index(".")] ))
	var.WritePoints.write( "\nNumber of question marks =  :  " + str( var.PointCounter[var.points.index("?")] ))
	var.WritePoints.write( "\nNumber of exclamations marks =  :  " + str( var.PointCounter[var.points.index("!")] ))
	var.WritePoints.write( "\nNumber of greater then =  :  " + str( var.PointCounter[var.points.index(">")] ))
	var.WritePoints.write( "\nNumber of lower then =  :  " + str( var.PointCounter[var.points.index("<")] ))
	var.WritePoints.write( "\nNumber of minus signs =  :  " + str( var.PointCounter[var.points.index("-")] ))
	var.WritePoints.write( "\nNumber of plus signs =  :  " + str( var.PointCounter[var.points.index("+")] ))
	var.WritePoints.write( "\nNumber of stars =  :  " + str( var.PointCounter[var.points.index("*")] ))
	var.WritePoints.write( "\nNumber of new lines =  :  " + str( var.PointCounter[var.points.index("\n")] ))
        

def PrintStats():
	print ( stats.TotalDifferentWords )
	var.WriteStats.write ( str( stats.TotalDifferentWords ) + '\n' )	#write accetta solo stringhe, str(num) trasforma un numero in stringa
	
	print ( "Number of words in file:  ", stats.TotalWords)
	var.WriteStats.write ( "Number of words in file:  " + str(stats.TotalWords) + '\n' )
	
	print( "Percentage of new words:  ", str(stats.PercentageNewWords), '\n' )
	var.WriteStats.write ( "Percentage of new words:  " + str(stats.PercentageNewWords) + '\n' )
    

def CloseAllOutput():
	var.WriteBook.close()
	var.WriteWords.close()
	var.WritePoints.close()
	var.WriteStats.close()

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








