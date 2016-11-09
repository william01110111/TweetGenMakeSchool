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
		

if __name__ == '__main__':
	rand=RandomGen()
	rand.seedWithTime()
	for i in range(0, 10):
		print(rand.get()%10)
	
