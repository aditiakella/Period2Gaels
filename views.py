from flask import render_template, Flask
import dataaboutus
import requests
from flask import render_template, request, redirect, url_for
# session and database support
from flask_login import login_required
from models import login_manager
from models.create import user_create, users_query_all
app = Flask(__name__)

@app.route('/databases/')
def databases():
    print("grace was here")
    """convert Users table into a list of dictionary rows"""
    records = users_query_all()
    return render_template("index.html", table=records)


# create/add a new record to the table
@app.route('/create/', methods=["POST"])
def create():
    if request.form:
        """extract data from form"""
        user_dict = {'name': request.form.get("name"), 'password': request.form.get("password"),
                     'email': request.form.get("email")}
        user_create(user_dict)
    return redirect(url_for('.databases'))


# if email url, show the email table only
@app.route('/emails/')
def emails():
    # fill the table with emails only
    records = model_query_emails()
    return render_template("index.html", table=records)


# if phones url, show phones table only
@app.route('/phones/')
def phones():
    # fill the table with phone numbers only
    records = model_query_phones()
    return render_template("index.html", table=records)

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
@app.route('/aboutus/luke/')
def luke():
    #Flask import uses Jinga to render HTML
    return render_template("luke.html", data=dataaboutus.lukes_info())

@app.route('/Phylogenetic/')
def Phylogenetic():
    return render_template("Phylogenetic.html")


@app.route('/joke', methods=['GET', 'POST'])
def joke():
    url = "https://twitter32.p.rapidapi.com/getTweetIdByUrl"

    querystring = {"url":"https://twitter.com/Nike/status/1319639821451554818"}
    headers = {
        'x-rapidapi-key': "SIGN-UP-FOR-KEY",
        'x-rapidapi-host': "twitter32.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template('joke.html')

@app.route('/Responses/')
def Responses():
    return render_template("Responses.html")

@app.route('/database/')
def database():
    return render_template("index.html")

@app.route('/easteregg')
def Easter():
    return render_template("easteregg.html")

# connects default URL to a function