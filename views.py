from flask import render_template, Flask
import dataaboutus
import requests
from flask import render_template, request, redirect, url_for
# session and database support
from flask_login import login_required
from models import login_manager
from models.create import user_create, users_query_all
from models.login import model_authorize, model_login, model_logout
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


# CRUD read, which is filtering table based off of ID
@app.route('/read/', methods=["POST"])
def read():
    record = []
    if request.form:
        userid = request.form.get("ID")
        # model_read expects userid
        user_dict = model_read(userid)
        # model_read returns: username, password, email, phone_number
        record = [user_dict]  # placed in list for compatibility with index.html
    return render_template("pythondb/index.html", table=record)


# CRUD update
@app.route('/update/', methods=["POST"])
def update():
    if request.form:
        user_dict = {
            'userid': request.form.get("ID"),
            'email': request.form.get("email"),
        }
        # model_update expects userid, email
        model_update(user_dict)
    return redirect(url_for('pythondb_bp.databases'))


# CRUD delete
@app.route('/delete/', methods=["POST"])
def delete():
    if request.form:
        """fetch userid"""
        userid = request.form.get("ID")
        model_delete(userid)
    return redirect(url_for('pythondb_bp.databases'))


# if email url, show the email table only
@app.route('/emails/')
def emails():
    # fill the table with emails only
    records = model_query_emails()
    return render_template("index.html", table=records, menu=menus)


# if phones url, show phones table only
@app.route('/phones/')
def phones():
    # fill the table with phone numbers only
    records = model_query_phones()
    return render_template("index.html", table=records, menu=menus)


# Authorise User Section
# if auth user is the signup section
# the public page does not include @login_required
@app.route('/public/')
def public():
    return render_template("public_page.html")


@app.route('/auth_user/', methods=["GET", "POST"])
def auth_user():
    # check form inputs and create auth user
    if request.form:
        # validation should be in HTML
        user_dict = {
            'user_name': request.form.get("txtUsername"),
            'email': request.form.get("txtEmail"),
            'password': request.form.get("txtPwd1")
        }
        # model_authorize requires user_dict: user_name, email, password
        model_authorize(user_dict)
        return redirect(url_for('pythondb_bp.login'))
    # show the auth user page if the above fails for some reason
    return render_template("pythondb/auth_user.html")


# if login url, show phones table only
@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.form:
        # validation should be in HTML
        user_dict = {
            'user_name': request.form.get("txtUsername"),
            'email': request.form.get("txtEmail"),
            'password': request.form.get("txtPwd1")
        }
        if model_login(user_dict):
            return redirect(url_for('pythondb_bp.dashboard'))

    # if not logged in, show the login page
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    model_logout()
    return redirect(url_for('login.html'))


# this code lets Flask-Login take unauthorised users back to the login page
@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    return redirect(url_for('login.html'))

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
@login_required
def Responses():
    return render_template("Responses.html")

@app.route('/database/')
def database():
    return render_template("index.html")

@app.route('/easteregg')
def Easter():
    return render_template("easteregg.html")

# connects default URL to a function