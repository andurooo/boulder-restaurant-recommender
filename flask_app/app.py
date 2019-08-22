from flask import Flask, render_template 
from flask import Flask, redirect, url_for, request
import pandas as pd
import pickle
import get_recs

app = Flask(__name__)

with open('../data/restaurant_df.pkl','rb') as f:
    df = pickle.load(f)

@app.route("/", methods=['GET','POST'])
def home():
    names = df.index
    return render_template('home.html', names=names)

@app.route('/recs', methods=['GET', 'POST'])
def recs():
    if request.method=='POST':
        name = request.form.get('name')
    W, H = get_recs.get_latent_topics(df)
    cos_sim = get_recs.get_cosine_sim(W)
    recs = get_recs.get_recs(name, cos_sim)
    return render_template("recs.html", recs=recs)

if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
