
import re
import sys

class Histogram:
	
	words={}
	
	def __init__(self):
		return
	
	def addList(self, wordList):
		for word in wordList:
			if word:
				if word in self.words:
					self.words[word]+=1
				else:
					self.words[word]=1;
	
	def addString(self, text):
		delimiters = " ", ",", ".", "\n", "\t", ";"
		regexPattern = '|'.join(map(re.escape, delimiters))
		wordList=re.split(regexPattern, text)
		self.addList(wordList)
	
	def addFile(self, filename):
		self.addString(open('/usr/share/dict/words', 'r').read())
	
	def getFrequency(self, word):
		return self.words[word]

def run():
	hist=Histogram()
	if len(sys.argv)<3:
		print("too few args")
	else:
		hist.addFile(sys.argv[1])
		print("'" + sys.argv[2] + "' appears " + str(hist.getFrequency(sys.argv[2])) + " times")
		print(hist.words)
	

if __name__ == '__main__':
	run()


