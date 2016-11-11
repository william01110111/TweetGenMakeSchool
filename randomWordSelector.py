
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
		self.maxScore=self.maxScore+freq
		
	def __init__(self, hist):
		
		for key, val in hist.words.iteritems():
			self.appendWord(key, val)
		
		if self.maxScore==0:
			self.appendWord("no_words", 1)
	
	def getWordAtPos(self, pos):
		
		if pos>self.maxScore:
			return "scoreSentTooHigh"
		
		i=0
		
		while True:
			if i>len(self.words):
				return "indexOutOfRange"
			
			if pos>=self.words[i].pos and pos<self.words[i].pos+self.words[i].freq:
				return self.words[i].text
			i+=1
	
	def getRandWord(self):
		pos=randint(0, self.maxScore-1)
		return self.getWordAtPos(pos)
	
	def toString(self):
		out=""
		for i in self.words:
			out+=i.text+": "+str(i.freq)+", "+str(i.pos)+"\n"
		return out
	
def run():
	hist=Histogram()
	if len(sys.argv)<3:
		print("too few args")
	else:
		hist.addFile(sys.argv[1])
		selector=RandomWordSelector(hist)
		
		for i in range(0, int(sys.argv[2])):
			print(selector.getRandWord())
	

if __name__ == '__main__':
	run()

