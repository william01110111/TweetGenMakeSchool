from randomWordSelector import RandomWordSelector

class MarkovNode:
	
	def __init__(self, text):
		self.text=text
		self.next={}
	
	def addNode(self, node):
		if node in self.next:
			self.next[node]+=1
		else:
			self.next[node]=1
	
	def getRandomNext(self):
		selector=RandomWordSelector(self.next)
		return selector.getRandWord()
		
