#!/usr/bin/python
# coding=utf-8

import os

import var
import get
import stats
import write


#PrintIntro()
write.PrintBook()

get.GetWords()
get.CloseInput()

stats.ComputeWords()

write.PrintWords()
write.PrintPoints()
write.PrintStats()

write.CloseAllOutput()




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
	Leggere da internet
	Migliorare la stampa
		Generalità
		Riordinare
	File Statistiche
		Frequenza o percentuale
			Totale, Per paragrafo per frase
		Di
			Punteggiatura, singole parole, categorie grammaticali
	Collegare a un dizionario

"""








