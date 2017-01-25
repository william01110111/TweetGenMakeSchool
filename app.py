import source.markovModel
import os

from flask import Flask
app = Flask(__name__)

model=source.markovModel.MarkovModel()

@app.route('/')
def welcome():
	return model.makeQuote()

"""
@app.route('/word')
def getRandWord():
	return selector.getRandWord()

@app.route('/words/<wordNum>')
def getManyWords(wordNum):
	wordList=[]
	
	for i in range(0, int(wordNum)):
		wordList.append(selector.getRandWord())
	
	return " ".join(wordList)
"""

if __name__ == "__main__":
	model.addFile("cleaned_corpus/allDoctorQuotes.txt")
	print("\n\n\nserver started\n\n\n")
	port= int(os.environ.get("PORT", 5000))
	# this to stop the app running twice
	#app.run(debug=True, host='0.0.0.0', port=port, use_reloader=False)
	
	app.run(debug=True, host='0.0.0.0', port=port)
	

