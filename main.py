import random
import sys
import time

class RandomGen:
	
	val=0
	
	def seed(this, valIn):
		this.val=valIn
		this.get()
	
	def seedWithTime(this):
		this.seed(int(time.time()))
	
	def get(this):
		this.val = (this.val * 22695477 + 1) % 4294967296
		return this.val

def run():
	inAry = sys.argv
	#remove this file as it is a default argument
	inAry.pop(0)
	
	rand=RandomGen()
	
	rand.seedWithTime()
	
	outAry = []
	
	while (len(inAry)>0):
		outAry.append(inAry.pop(rand.get()%len(inAry)))
		
	for i in outAry:
		print(i)

if __name__ == '__main__':
	run()


