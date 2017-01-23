import sys

class Tokenizer():
	
	def finishToken(self):
		
		if (self.pos>self.start):
			self.tokens.append(self.data[self.start:self.pos])
		
		self.start=self.pos+1
	
	def finishQuote(self):
		
		self.finishToken()
		
		if len(self.tokens)>0:
			self.quotes.append(list(self.tokens))
			self.tokens=[]
	
	def __init__(self, data):
		self.data=data
		self.tokens=[]
		self.quotes=[]
		self.start=0
		self.pos=0
		
	def get(self):
		while(self.start<len(self.data)):
		
			c=self.data[self.pos]
			
			if (c==" " or c=="," or c=="(" or c==")" or c=="[" or c=="]" or c==";" or c==":"):
				self.finishToken()
		
			elif (c=="." or c=="\n" or c=="!" or c=="?" or c=='-'):
				self.finishQuote()
		
			self.pos+=1
	 
		self.finishQuote() 
	
		#print(len(self.quotes))
	
		#for i in self.quotes:
		#	for j in i:
		#		print(j)
		#	print("\n\n")
		#
		
		return self.quotes
	
def tokenize(data):
	t=Tokenizer(data)
	return t.get()

if __name__ == "__main__":
	tokens=tokenize(open("../../DW_scraper/allDoctorQuotes.txt", 'r').read())
	for i in tokens:
		for j in i:
			print(j)
		print("\n\n")
		
