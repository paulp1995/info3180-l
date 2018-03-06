from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired,Email
from flask_wtf.file import FileAllowed, FileRequired, FileField 
from flask import Flask, render_template, flash, session, redirect, url_for
from wtforms import TextAreaField, TextField, SubmitField


class SignupForm(FlaskForm):
    FirstName = TextField("First Name", validators=[InputRequired("Please enter your name properly.")])
    LastName = TextField("Last Name", validators=[InputRequired("Please enter your name properly.")])
    Email = TextField("E-Mail", validators=[InputRequired("Please enter a Email address."),Email("Please enter a valid Email.")])
    Location = TextField("Location", validators=[InputRequired("Please enter a Location matter.")])
    Bio = TextAreaField("Message", validators=[InputRequired("Please enter some small personal information.")])
    Upload = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'], 'Only image files accepted.')])
    Submit = SubmitField("Send")