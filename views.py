from flask import Flask, render_template
import dataaboutus
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/feedback/')
def feedback():
    return render_template("Feedback.html")
@app.route('/aboutus/')
def aboutus():
    #Flask import uses Jinga to render HTML
    return render_template("aboutus.html", data=dataaboutus.alldata()