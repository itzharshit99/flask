from flask import Blueprint,request,flash

auth = Blueprint('auth',__name__)

@auth.route("/login",methods=['GET','POST'])
def login():
    data = request.json
    print(data)
    return "login"
@auth.route("/logout")
def logout():
    return "logout"
@auth.route("/sign-up",methods=['GET','POST'])
def signUp():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email)<4:
            flash('Email must be greater than 4',category='error')
            pass
        elif len(firstName)<2:
            pass
        elif password1!=password2:
            pass
        elif len(password1) <7:
            pass
        else:
            #add user to db
            pass
    return "sign-up"
