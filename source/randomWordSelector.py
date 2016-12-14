
from wordHistogram import Histogram
import random
import sys

class WordEntry:
	
	def __init__(self, text, pos):
		self.text=text
		self.pos=pos
		

class RandomWordSelector:
		
	def __init__(self, hist):
		
		self.words=[]
		self.maxScore=0
		
		for key, val in hist.iteritems():
			self.appendWord(key, val)
		
		if self.maxScore==0:
			self.appendWord("no_words", 1)
	
	def appendWord(self, text, freq):
		self.words.append(WordEntry(text, self.maxScore))
		self.maxScore=self.maxScore+freq
	
	def getWordAtPosLinear(self, pos):
		
		i=len(self.words)-1
		
		while True:
			if i>=len(self.words):
				return "indexOutOfRangeForPos"+str(pos)
			
			if self.words[i].pos<=pos:
				return self.words[i].text
				
			i-=1
	
	def getWordAtPosBinary(self, pos):
		#pos=0
		start=0
		end=len(self.words)
		
		while(end-start>1):
			guess=int((start+end)/2.0)
			if self.words[guess].pos<=pos:
				start=guess
			else:
				end=guess
		
		#print(start)
		
		return self.words[start].text
	
	def getWordAtPos(self, pos):
		
		if pos>self.maxScore:
			return "scoreSentTooHigh"
		
		#print("getWordAtPos sent position of " + str(pos))
		
		binaryResult=self.getWordAtPosBinary(pos)
		#linearResult=self.getWordAtPosLinear(pos)
		
		#print("binary result: " + binaryResult)
		#print("linear result: " + linearResult)
		
		#if binaryResult!=linearResult:
		#	print("binary search fucked up")
		
		return binaryResult
		#return linearResult
	
	def getRandWord(self):
		pos=random.randrange(0, self.maxScore)
		out=self.getWordAtPos(pos)
		#print("\n"+out.getString())
		return out
	
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
		selector=RandomWordSelector(hist.words)
		
		#print(selector.toString())
		
		for i in range(0, int(sys.argv[2])):
			#print("\n")
			print(selector.getRandWord())
	

if __name__ == '__main__':
	run()

