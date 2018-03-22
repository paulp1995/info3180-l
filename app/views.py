"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, session, abort, make_response,jsonify
from flask_login import login_user, logout_user, current_user, login_required
from forms import SignupForm
from models import UserProfile
import os , datetime
from werkzeug.utils import secure_filename

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route('/profile/',methods=["GET", "POST"])
def profile():
    filledform = SignupForm()
    if request.method == 'POST':
        if filledform.validate_on_submit():

            # collection of data from the form
            first_name = filledform.first_name.data
            last_name = filledform.last_name.data
            gender = filledform.gender.data
            email = filledform.email.data
            location = filledform.location.data
            bio = filledform.bio.data
            pic = filledform.upload.data
            date_created = str(datetime.date.today())
    
            image_name = secure_filename(pic.filename)
            
            # Validate file upload on submit
            pic.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
            
            # save data to database
            newuser = UserProfile(first_name, last_name, gender, email, location, bio, image_name, date_created)
            
            db.session.add(newuser)
            db.session.commit()
    
            flash("Profile Successfully Created", "success")
            return redirect(url_for("profile"))
            
            
        flash_errors(filledform)
    print filledform.errors.items()
    
    """Render a secure page on our website that only logged in users can access."""
    return render_template('profile.html',  form = filledform)
    ##return render_template('profile.html')

@app.route('/profiles',methods=['POST','GET'])
def profiles():
    user_list = UserProfile.query.all()
    users = [{"user_ID":user.u_id,"FirstName": user.first_name, "LastName": user.last_name, "gender": user.gender, "Location": user.location} for user in user_list]
    
    if request.method == 'GET':
        if user_list is not None:
            return render_template("profiles.html", users=user_list)
        else:
            flash('No Users Found', 'danger')
            return redirect(url_for("home"))

@app.route('/profiles/<userid>', methods=['POST', 'GET'])
def viewProfile(userid):
    user = UserProfile.query.filter_by(u_id=userid).first()
    if user is not None:
        return render_template('viewprofile.html',user=user)
    else:
        flash('Unable to view user profile', 'danger')
        return redirect(url_for('profile'))


###
# The functions below should be applicable to all Flask apps.
###

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
getattr(form, field).label.text,error), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
