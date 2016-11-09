import random
import sys
from randomGen import RandomGen

def printList(listIn):
	for i in listIn:
		print(i)
	
	print("")

def reorderList(listIn):
	rand=RandomGen()
	
	rand.seedWithTime()
	rand.get()
	
	if len(listIn)==0:
		print("error: no cmd line args")
	
	for i in range(0, len(listIn)):
		j=(rand.get()%(len(listIn)-i))+i
		listIn[i], listIn[j] = listIn[j], listIn[i]
	
	return listIn

def reorderArgs():
	
	print("\ncmd line args in random order:")
	
	args = sys.argv
	
	#remove this file as it is a default argument
	args.pop(0)
	
	#remove reorder command
	args.pop(0)
	
	i=0
	
	args=reorderList(args)
	
	printList(args)
	
	print("")

def splitStringWords(strIn):
	listOut=[]
	
	subStr=""
	
	for i in strIn:
		if i==" ":
			listOut.append(subStr)
			subStr=""
		else:
			subStr+=i
	
	listOut.append(subStr)
	
	return listOut

def reorderString(strIn):
	wordList=splitStringWords(strIn)
	wordList=reorderList(wordList)
	print("\nstring with word order random:")
	printList(wordList)
	print("")
	return

def run():
	if len(sys.argv)>=2:
		cmd=sys.argv[1]
		
		if cmd=="-h":
			print("\nusage:\n")
			print("python main.py reorder [multiple words] - reorders words")
			print("python main.py string \"[string]\" - reorders words in a string")
			print("")
		
		elif cmd=="reorder":
			reorderArgs()
		
		elif cmd=="string":
			if len(sys.argv)>=3:
				reorderString(sys.argv[2])
			else:
				print("no string given")
		
		else:
			print("\nunknown command, args: " + str(sys.argv) + "\n")

if __name__ == '__main__':
	run()


