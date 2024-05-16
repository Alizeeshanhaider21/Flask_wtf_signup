
# Importing Libraries.. 
from flask import Flask, render_template, request ,redirect
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField 
from wtforms import DecimalField, RadioField, SelectField, TextAreaField, FileField ,validators
from wtforms.validators import InputRequired 
from wtforms.fields import EmailField
from werkzeug.security import generate_password_hash 
from flask_bootstrap import Bootstrap5
import os

    
class MyForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=2, max=30)]) 
    email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password',[ validators.InputRequired()])
    

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap5(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        name = form.username.data 
        email = form.email.data
        password = form.password.data
        print(name,password)
        
        if email == "admin@email.com" and password == "1234" and name=='admin':
            context={
            'name':name,
            'password':password,
            'email':email,
            'hassPass':generate_password_hash(password)
        }
            return render_template('success.html' ,context=context)
        else:
            return render_template("denied.html")
    return render_template('login.html',form=form)

@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('success.html')

@app.route('/denied', methods=['GET', 'POST'])
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
