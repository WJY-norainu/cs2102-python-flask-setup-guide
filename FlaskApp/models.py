from __init__ import db


class WebUser(db.Model):
    username = db.Column(db.String, primary_key=True)
    preferred_name = db.Column(db.String, nullable=True)
    password = db.Coloumn(db.String, nullable=False)

    def __init__(self):
        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False

    def get_id(self):
        return self.username
