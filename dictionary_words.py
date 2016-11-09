from random import randint
import sys

def printList(listIn):
	
	out=""	
	
	for i in range(0, len(listIn)):
		out+=listIn[i]
		if i<len(listIn)-1:
			out+=" "
	
	print(out)

def getWordsFileStr():
	return open('/usr/share/dict/words', 'r').read()

def splitStringWords(strIn):
	listOut=[]
	
	subStr=""
	
	for i in strIn:
		if i=="\n":
			if subStr!="":
				listOut.append(subStr)
			subStr=""
		else:
			subStr+=i
	
	listOut.append(subStr)
	
	return listOuttime

def getRandWord(listIn):
	return listIn[randint(0, len(listIn)-1)]

def run():
	if len(sys.argv)==2:
		wordNum=int(sys.argv[1])
		wordsFileStr=getWordsFileStr()
		wordList=splitStringWords(wordsFileStr)
		randWordList=[]
		for i in range(0, wordNum):
			randWordList.append(getRandWord(wordList))
		printList(randWordList)
		
	else:
		print("error: wrong number of args")

if __name__ == '__main__':
	run()


