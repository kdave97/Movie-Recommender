from flask import Flask, request, render_template
import pandas as pd
#import json
#import random, threading, webbrowser
#from collaborative_model import *
from content_model import *
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
	
@app.route('/predict',methods=['POST'])
def predict():
	int_features=[]	
	int_features.append(request.form['movie_1'])
	int_features.append(request.form['rating_1'])
	int_features.append(request.form['movie_2'])
	int_features.append(request.form['rating_2'])
	int_features.append(request.form['movie_3'])
	int_features.append(request.form['rating_3'])
	#int_features = [x for x in request.form.values()]
	ip=[]
	print (int_features)
	for i in range(0,len(int_features),2):
		views={'title':int_features[i],'rating':float(int_features[i+1])}
		ip.append(views)
	print (ip)		
	results=recommend(ip)
	return render_template('index.html', my_list=results)
	
if __name__ == "__main__":
	app.run(host="0.0.0.0",port=8080)
