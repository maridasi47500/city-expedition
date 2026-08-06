from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_plane_ticket", methods=["GET","POST"])
def add_one_plane_ticket():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into plane_ticket (depart,destination) values (:depart,:destination)",hey)
        user = query_db('select * from plane_ticket')

        return render_template("plane_ticketform.html", plane_tickets=user, one_user=one_user, the_title="add new plane_ticket")


    user = query_db('select * from plane_ticket')
    one_user = query_db("select * from plane_ticket limit 1", one=True)
    return render_template("plane_ticketform.html", plane_tickets=user, one_user=one_user, the_title="add new plane_ticket")

@app.route("/add_one_resume", methods=["GET","POST"])
def add_one_resume():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesperson= query_db("select * from person")

        one_user = query_db("insert into resume (person_id,content,phone,email) values (:person_id,:content,:phone,:email)",hey)
        user = query_db('select * from resume')

        return render_template("resumeform.html", resumes=user, one_user=one_user, the_title="add new resume", touslesperson=touslesperson)


    touslesperson= query_db("select * from person")

    user = query_db('select * from resume')
    one_user = query_db("select * from resume limit 1", one=True)
    return render_template("resumeform.html", resumes=user, one_user=one_user, the_title="add new resume", touslesperson=touslesperson)

@app.route("/add_one_person", methods=["GET","POST"])
def add_one_person():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into person (name,phone,email) values (:name,:phone,:email)",hey)
        user = query_db('select * from person')

        return render_template("personform.html", persons=user, one_user=one_user, the_title="add new person")


    user = query_db('select * from person')
    one_user = query_db("select * from person limit 1", one=True)
    return render_template("personform.html", persons=user, one_user=one_user, the_title="add new person")

@app.route("/add_one_company", methods=["GET","POST"])
def add_one_company():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into company (name,phone,email) values (:name,:phone,:email)",hey)
        user = query_db('select * from company')

        return render_template("companyform.html", companys=user, one_user=one_user, the_title="add new company")


    user = query_db('select * from company')
    one_user = query_db("select * from company limit 1", one=True)
    return render_template("companyform.html", companys=user, one_user=one_user, the_title="add new company")

@app.route("/add_one_linkpersoncompany", methods=["GET","POST"])
def add_one_linkpersoncompany():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesperson= query_db("select * from person")

        touslescompany= query_db("select * from company")

        one_user = query_db("insert into linkpersoncompany (person_id,company_id) values (:person_id,:company_id)",hey)
        user = query_db('select * from linkpersoncompany')

        return render_template("linkpersoncompanyform.html", linkpersoncompanys=user, one_user=one_user, the_title="add new linkpersoncompany", touslesperson=touslesperson, touslescompany=touslescompany)


    touslesperson= query_db("select * from person")

    touslescompany= query_db("select * from company")

    user = query_db('select * from linkpersoncompany')
    one_user = query_db("select * from linkpersoncompany limit 1", one=True)
    return render_template("linkpersoncompanyform.html", linkpersoncompanys=user, one_user=one_user, the_title="add new linkpersoncompany", touslesperson=touslesperson, touslescompany=touslescompany)

@app.route("/add_one_musicsession", methods=["GET","POST"])
def add_one_musicsession():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into musicsession (name,description) values (:name,:description)",hey)
        user = query_db('select * from musicsession')

        return render_template("musicsessionform.html", musicsessions=user, one_user=one_user, the_title="add new musicsession")


    user = query_db('select * from musicsession')
    one_user = query_db("select * from musicsession limit 1", one=True)
    return render_template("musicsessionform.html", musicsessions=user, one_user=one_user, the_title="add new musicsession")

@app.route("/add_one_participantjamuser", methods=["GET","POST"])
def add_one_participantjamuser():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesmusicsession= query_db("select * from musicsession")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into participantjamuser (musicsession_id,user_id) values (:musicsession_id,:user_id)",hey)
        user = query_db('select * from participantjamuser')

        return render_template("participantjamuserform.html", participantjamusers=user, one_user=one_user, the_title="add new participantjamuser", touslesmusicsession=touslesmusicsession, touslesuser=touslesuser)


    touslesmusicsession= query_db("select * from musicsession")

    touslesuser= query_db("select * from user")

    user = query_db('select * from participantjamuser')
    one_user = query_db("select * from participantjamuser limit 1", one=True)
    return render_template("participantjamuserform.html", participantjamusers=user, one_user=one_user, the_title="add new participantjamuser", touslesmusicsession=touslesmusicsession, touslesuser=touslesuser)

@app.route("/add_one_participantjamperson", methods=["GET","POST"])
def add_one_participantjamperson():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesmusicsession= query_db("select * from musicsession")

        touslesperson= query_db("select * from person")

        one_user = query_db("insert into participantjamperson (musicsession_id,person_id) values (:musicsession_id,:person_id)",hey)
        user = query_db('select * from participantjamperson')

        return render_template("participantjampersonform.html", participantjampersons=user, one_user=one_user, the_title="add new participantjamperson", touslesmusicsession=touslesmusicsession, touslesperson=touslesperson)


    touslesmusicsession= query_db("select * from musicsession")

    touslesperson= query_db("select * from person")

    user = query_db('select * from participantjamperson')
    one_user = query_db("select * from participantjamperson limit 1", one=True)
    return render_template("participantjampersonform.html", participantjampersons=user, one_user=one_user, the_title="add new participantjamperson", touslesmusicsession=touslesmusicsession, touslesperson=touslesperson)

@app.route("/add_one_city", methods=["GET","POST"])
def add_one_city():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into city (name) values (:name)",hey)
        user = query_db('select * from city')

        return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city")


    user = query_db('select * from city')
    one_user = query_db("select * from city limit 1", one=True)
    return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city")

@app.route("/add_one_resume_matcher", methods=["GET","POST"])
def add_one_resume_matcher():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into resume_matcher (resume1_id,resume2_id,description) values (:resume1_id,:resume2_id,:description)",hey)
        user = query_db('select * from resume_matcher')

        return render_template("resume_matcherform.html", resume_matchers=user, one_user=one_user, the_title="add new resume_matcher")


    user = query_db('select * from resume_matcher')
    one_user = query_db("select * from resume_matcher limit 1", one=True)
    return render_template("resume_matcherform.html", resume_matchers=user, one_user=one_user, the_title="add new resume_matcher")

@app.route("/add_one_concert", methods=["GET","POST"])
def add_one_concert():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescity= query_db("select * from city")

        one_user = query_db("insert into concert (time,date,place,title,city_id) values (:time,:date,:place,:title,:city_id)",hey)
        user = query_db('select * from concert')

        return render_template("concertform.html", concerts=user, one_user=one_user, the_title="add new concert", touslescity=touslescity)


    touslescity= query_db("select * from city")

    user = query_db('select * from concert')
    one_user = query_db("select * from concert limit 1", one=True)
    return render_template("concertform.html", concerts=user, one_user=one_user, the_title="add new concert", touslescity=touslescity)

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,email,password,phone,country_id) values (:username,:email,:password,:phone,:country_id)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','email','password','phone','country_id']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','email','password','phone','country_id']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','email','password','phone','country_id']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_concert_ticket", methods=["GET","POST"])
def add_one_concert_ticket():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesconcert= query_db("select * from concert")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into concert_ticket (promotion_name,price,concert_id,user_id) values (:promotion_name,:price,:concert_id,:user_id)",hey)
        user = query_db('select * from concert_ticket')

        return render_template("concert_ticketform.html", concert_tickets=user, one_user=one_user, the_title="add new concert_ticket", touslesconcert=touslesconcert, touslesuser=touslesuser)


    touslesconcert= query_db("select * from concert")

    touslesuser= query_db("select * from user")

    user = query_db('select * from concert_ticket')
    one_user = query_db("select * from concert_ticket limit 1", one=True)
    return render_template("concert_ticketform.html", concert_tickets=user, one_user=one_user, the_title="add new concert_ticket", touslesconcert=touslesconcert, touslesuser=touslesuser)

