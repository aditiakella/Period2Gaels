from flask import render_template, Flask
import dataaboutus

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/feedback/')
def feedback():
    return render_template("Feedback.html")

@app.route('/aboutus/')
def about():
    #Flask import uses Jinga to render HTML
    return render_template("About.html", data=dataaboutus.alldata())
@app.route('/aboutus/aditi/')
def aditi():
    #Flask import uses Jinga to render HTML
    return render_template("aditi.html", data=dataaboutus.aditis_info())
@app.route('/aboutus/sophie/')
def sophie():
    #Flask import uses Jinga to render HTML
    return render_template("sophie.html", data=dataaboutus.sophies_info())
@app.route('/aboutus/grace/')
def grace():
    #Flask import uses Jinga to render HTML
    return render_template("grace.html", data=dataaboutus.graces_info())

@app.route('/Phylogenetic/')
def Phylogenetic():
    return render_template("Phylogenetic.html")