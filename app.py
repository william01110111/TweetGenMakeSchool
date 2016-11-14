from wordHistogram import Histogram
from randomWordSelector import RandomWordSelector

from flask import Flask
app = Flask(__name__)

hist=Histogram()

hist.addFile("trump_speach.txt")
selector=RandomWordSelector(hist)

@app.route('/')
def welcome():
	return "welcome to random word selector, go to /random_word to get a word"

@app.route('/random_word')
def getRandWord():
	return selector.getRandWord()

if __name__ == "__main__":
    app.run()

