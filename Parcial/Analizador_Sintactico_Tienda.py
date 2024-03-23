import sys
import re

nombre_archivo = "store_grammar_sample.txt"
currentTokenPosition = 0
currentToken = ""

def match(token):
	global currentTokenPosition
	global currentToken
	global vecTokenTypes
	currentToken=vecTokenTypes[currentTokenPosition]
	if currentToken==token:
		currentTokenPosition=currentTokenPosition+1
		print("The consume: ", token, "\n")
	else:
		print("Syntax Error\n")



