from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired,Email
from flask_wtf.file import FileAllowed, FileRequired, FileField 
from flask import Flask, render_template, flash, session, redirect, url_for
from wtforms import TextAreaField, TextField, SubmitField


class SignupForm(FlaskForm):
    first_name = TextField("First Name", validators=[InputRequired("Please enter your name properly.")])
    last_name = TextField("Last Name", validators=[InputRequired("Please enter your name properly.")])
    gender = SelectField('Gender', choices=[('male','Male'),('female','Female')],validators=[InputRequired('Gender is required')])
    email = TextField("E-Mail", validators=[InputRequired("Please enter a Email address."),Email("Please enter a valid Email.")])
    location = TextField("Location", validators=[InputRequired("Please enter a Location matter.")])
    bio = TextAreaField("Message", validators=[InputRequired("Please enter some small personal information.")])
    upload = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'], 'Only image files accepted.')])
    submit = SubmitField("Add Profile")