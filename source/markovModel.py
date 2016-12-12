import tokenizer
from markovNode import MarkovNode

class MarkovModel:
	
	def __init__(self):
		self.words={}
		self.begin=MarkovNode("")
		self.end=MarkovNode("")
	
	def addList(self, quotes):
		print("adding to model...")
		tokens=0
		for quote in quotes:
			
			last=self.begin
			
			for token in quote:
				tokens+=1
				if not token in self.words:
					self.words[token]=MarkovNode(token)
				
				node=self.words[token]
				
				last.addNode(node)
				last=node
			
			last.addNode(self.end)
		
		print("added "+str(tokens)+" tokens to model")
		print("done adding file")
	
	def addFile(self, filepath):
		print("reading from '"+filepath+"'...")
		contents=open(filepath, 'r').read()
		print("tokenizing...")
		quotes=tokenizer.tokenize(contents)
		print("found "+str(len(quotes))+" quotes")
		addList(quotes)
	
	def getString(self):
		out=""
		out+="[begin]"+self.begin.getString()+"\n"
		for key, val in self.words.iteritems():
			out+=val.getString()+"\n"
		return out
	
	def makeQuote(self):
		text=""
		node=self.begin.getRandomNext()
		words=0
		
		while (node.text!=""):
			if words>30:
				text+=" [quote got too long]"
				break;
				
			if words>0:
				text+=" "
				
			text+=node.text
			node=node.getRandomNext()
			words+=1
		
		return text

if __name__=="__main__":
	model=MarkovModel()
	model.addList([["one", "two", "one", "three"]])
	#model.addFile("../../DW_scraper/allDoctorQuotes.txt")
	
	print("\nmodel:\n"+model.getString())
	
	print("randomly generated quote:\n")
	
	for i in range(0, 1):
		print(model.makeQuote())


