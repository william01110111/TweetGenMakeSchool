
from flask import Flask
app = Flask(__name__)

hist=Histogram()

hist.addFile("trump_speach.txt")
selector=RandomWordSelector(hist)

@app.route('/random_word')
def hello_world():
    return selector.getRandWord()
    
    
