from randomWordSelector import RandomWordSelector

class MarkovNode:
	
	def __init__(self, data):
		self.data=data
		self.next={}
	
	def addNode(self, node):
		if node in self.next:
			self.next[node]+=1
		else:
			self.next[node]=1
	
	def getString(self):
		out=self.data+":\n"
		for key, val in self.next.iteritems():
			out+="\t"
			if len(key.data)==0:
				out+="[end]"
			else:
				out+=key.data
			out+=": "+str(val)+"\n"
		return out
	
	def getRandomNext(self):
		#print("number of elements in dict: "+str(len(self.next)))
		#print(self.getString())
		selector=RandomWordSelector(self.next)
		out=selector.getRandWord()
		#print("\n\nfrom\n"+self.getString()+"got\n"+out.getString())
		return out
		
