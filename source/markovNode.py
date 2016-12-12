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
	
	def getString(self):
		out=self.text+":\n"
		for key, val in self.next.iteritems():
			out+="\t"
			if len(key.text)==0:
				out+="[end]"
			else:
				out+=key.text
			out+=": "+str(val)+"\n"
		return out
	
	def getRandomNext(self):
		selector=RandomWordSelector(self.next)
		out=selector.getRandWord()
		print("\n\nfrom\n"+self.getString()+"got\n"+out.getString())
		return out
		
