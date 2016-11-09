
from wordHistogram import Histogram
from random import randint
import sys

class WordEntry:
	text=None
	freq=None
	pos=None
	
	def __init__(self, text, freq, pos):
		self.text=text
		self.freq=freq
		self.pos=pos

class RandomWordSelector:
	
	words=[]
	maxScore=0
	
	def appendWord(self, text, freq):
		self.words.append(WordEntry(text, freq, self.maxScore))
		self.maxScore+=freq
		
	def __init__(self, hist):
		
		self.appendWord("cat", 1)
		self.appendWord("dog", 1)
		self.appendWord("mouse", 1)
		
		if self.maxScore==0:
			self.appendWord("no_words", 1)
		
		print()
	
	def getWordAtPos(self, pos):
		i=0
		while(i<len(self.words) and not(self.words[i].pos>=pos and pos<self.words[i].freq+self.words[i].pos)):
			i+=1
		
		if len(self.words)<=i:
			return "indexOutOfRange"
		else:
			return self.words[i].text
	
	def getRandWord(self):
		pos=randint(0, self.maxScore-1)
		return self.getWordAtPos(pos)
	
	def toString(self):
		out=""
		for i in words:
			out+=i.text+": "+str(i.freq)+", "+str(i.pos)+"\n"
	
def run():
	hist=Histogram()
	if len(sys.argv)<3:
		print("too few args")
	else:
		hist.addFile(sys.argv[1])
		selector=RandomWordSelector(hist)
		
		print(selector.toString())
		
		for i in range(0, int(sys.argv[2])):
			print(selector.getRandWord())
	

if __name__ == '__main__':
	run()

