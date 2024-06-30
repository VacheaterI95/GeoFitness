from flask import render_template, redirect, request, Flask, session, render_template, redirect
from forms import BMIForm, Registerform, Loginform, CaloriesForm, ContactForm
from flask_login import login_user, logout_user, login_required, current_user
from extensions import app, db
from models import BMI, User, Calories, Message


@app.route("/")
def home():
    return render_template('gym.html')
@app.route("/dogs")
def dogs():
    return render_template('dogs.html')

@app.route("/cats")
def cats():
    return render_template('cats.html')

@app.route("/push")
def push():
    return render_template('pushday.html')

@app.route("/pull")
def pull():
    return render_template('pullday.html')


@app.route("/pullups")
def pullups():
    return render_template('pullups.html')

@app.route("/cablerows")
def cablerows():
    return render_template('cablerows.html')

@app.route("/shrugs")
def shrugs():
    return render_template('shrugs.html')

@app.route("/seatedincline")
def seatedincline():
    return render_template('seatedincline.html')

@app.route("/preachercurls")
def preachercurls():
    return render_template('preachercurls.html')

@app.route("/cablelateral")
def cablelateral():
    return render_template('cablelateral.html')

@app.route("/rearflies")
def rearflies():
    return render_template('rearflies.html')



@app.route("/login", methods=["GET", "POST"])
def login():
    form = Loginform()
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            return redirect ("/")
    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = Registerform()
    if form.validate_on_submit():
        user = User.query.filter(User.firstname == form.firstname.data, User.lastname == form.lastname.data, User.email == form.email.data).first()
        if user:
            username_taken = True
            print ("unsuccessful L")
        else:
            username_taken = False
            print ("successful W")
            new_user = User(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, password=form.password.data)
            new_user.create()

        return render_template('signup.html', username_taken=username_taken, form=form)
    return render_template('signup.html', form=form)





@app.route("/contactus", methods=["GET", "POST"])
def contactus():
    form = ContactForm()
    if form.validate_on_submit():
        new_message = Message(name=form.name.data, email=form.email.data, message=form.message.data)
        new_message.create()
        print (new_message)
        return render_template('contactus.html', form=form, new_message=new_message)
    return render_template('contactus.html', form=form)


@app.route("/bodybuilding6")
def bodybuilding6():
    return render_template('bodybuilding6.html')

@app.route("/legs")
def legs():
    return render_template('legday.html')

@app.route("/bodybuilding3")
def bodybuilding3():
    return render_template('bodybuilding3.html')

@app.route("/schedule")
def schedule():
    return render_template('schedule.html')

@app.route("/inclinebench")
def inclinebench():
    return render_template('inclinebench.html')

@app.route("/barbellbench")
def barbellbench():
    return render_template('barbellbench.html')

@app.route("/overheadbarbell")
def overheadbarbell():
    return render_template('overheadbarbell.html')

@app.route("/triceppushdown")
def triceppushdown():
    return render_template('triceppushdown.html')

@app.route("/tricepdbextensions")
def tricepdbextensions():
    return render_template('tricepdbextensions.html')

@app.route("/legextensions")
def legextensions():
    return render_template('legextensions.html')

@app.route("/hamstringcurls")
def hamstringcurls():
    return render_template('hamstringcurls.html')

@app.route("/squats")
def squats():
    return render_template('squats.html')

@app.route("/hipthrustsrdls")
def hipthrustsrdls():
    return render_template('hipthrustsrdls.html')

@app.route("/standcalf")
def standcalf():
    return render_template('standcalf.html')

@app.route("/seatedcalf")
def seatedcalf():
    return render_template('seatedcalf.html')

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')


@app.route("/bmi", methods=["GET", "POST"])
def bmi():
    form = BMIForm()
    if form.validate_on_submit():
        print ("bmis")
        wh = BMI(weight = int(form.weight.data),
                  height = float(form.height.data))
        bmi = int(form.weight.data) / float(form.height.data)**2
        print(bmi)
        if bmi > 1:
            rezultati = True
            print (rezultati)

        return render_template('BMI.html', bmi=bmi, rezultati=rezultati, form=form)
    return render_template('BMI.html', form=form)


@app.route("/caloriemaintenance", methods=["GET", "POST"])
def caloriemaintenance():
    form = CaloriesForm()
    if form.validate_on_submit():
        print("calories")
        calorie = Calories(weight=int(form.weight.data),
                            height=int(form.height.data),
                            age=int(form.age.data))
        calories = 10 * int(form.weight.data) + 6.25 * int(form.height.data) - 5 * int(form.age.data) + 5
        print(calories)
        if calories > 1:
            result = True
            print (result)


        return render_template('caloriemaintenance.html', calories=calories, result=result, form=form)
    return render_template('caloriemaintenance.html', form=form)