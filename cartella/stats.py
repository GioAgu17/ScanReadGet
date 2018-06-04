#!/usr/bin/python
# coding=utf-8

import var

TotalWords = 0
TotalDifferentWords = 0
PercentageNewWords = 0

def ComputeWords():
	TotalWords = var.word_number
	TotalDifferentWords = len( var.words )
	PercentageNewWords = TotalDifferentWords/TotalWords
	#prop = word_number / len( words )

#	WordsPerParagraph
#	WordsPerSentence
