from . import db


class UserProfile(db.Model):
    u_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80),nullable=False)
    last_name = db.Column(db.String(80),nullable=False)
    gender = db.Column(db.String(10),nullable=False)
    email = db.Column(db.String(100),  unique=True, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.Text)
    profile_pic = db.Column(db.String(80))
    date_created = db.Column(db.DateTime)
    
    __tablename__ = "UserProfile"
    
    def __init__( self, first_name, last_name, gender, email, location, bio, profile_pic, date_created):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.location = location
        self.bio = bio
        self.profile_pic = profile_pic
        self.date_created = date_created

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
