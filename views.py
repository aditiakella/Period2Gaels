from flask import render_template, Flask
import dataaboutus
import requests

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


@app.route('/joke', methods=['GET', 'POST'])
def joke():
    # call to random joke web api
    url = 'https://official-joke-api.appspot.com/jokes/programming/random'
    resp = requests.get(url)
    # formatting variables from return
    setup = resp.json()[0]['setup']
    punchline = resp.json()[0]['punchline']
    return render_template('joke.html', setup=setup, punchline=punchline)

@app.route('/Responses/')
def Responses():
    return render_template("Responses.html")