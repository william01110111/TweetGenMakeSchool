
class Histogram:
	
	words={}
	
	def __init__(self):
		return
	
	def addList(self, wordList):
		for word in wordList:
			if word in self.words:
				self.words[word]+=1
			else:
				self.words[word]=1;
	
	def addString(self, text):
		wordList=text.split()
		self.addList(wordList)
	
	def getFrequency(self, word):
		return self.words[word]

def run():
	hist=Histogram()
	hist.addString("cat dog dog mouse cat cat.\ncat")
	print("cat appears " + str(hist.getFrequency("cat")) + " times")
	
	

if __name__ == '__main__':
	run()


