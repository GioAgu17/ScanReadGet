#!/usr/bin/python
# coding=utf-8



points = [" ", ",", ";", ":", "'", ".", "?", "!", ">", "<", "-", "+", "*", "\n"]
PointCounter = [0]*len(points)

book = ""
word = ""
words = []
count =[]
word_number = 0 #conta il totale delle parole

#Read
#ReadBook = open("prova.txt", "r")
ReadChar = open("prova.dat", "r")

#Write
WriteBook = open("book.txt", "w")
WriteWords = open("words.txt", "w")
WritePoints = open("points.txt", "w")
WriteStats = open("stats.txt", "w")



