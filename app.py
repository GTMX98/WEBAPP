from flask import Flask, request, render_template
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
from numpy import random
#import nltk
import statistics

app = Flask(__name__)
#sid = SentimentIntensityAnalyzer()
co = {'compound':random.rand(0,9)}
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form['input-text']
        if len(text)>0:
            Virality = abs(co['compound'])+random.randint(20, 150)
            Believability = abs(co['compound'])+random.randint(20, 150)
            PFI = (Virality+Believability)/2
        else:
            Virality = 0
            Believability = 0
            PFI = statistics.mean([Virality,Believability])
        result = {'PFI':PFI,'BEL':Believability,'Vir':Virality}
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run()
