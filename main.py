from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, Length
import os


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

#Create a Form Class

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[InputRequired("Please enter your email address."),
                                  Email("This field requires a valid email address")])
    password = PasswordField(label="Password", validators=[InputRequired(), Length(min=6)])
    submit = SubmitField(label="Login")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def get_login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)