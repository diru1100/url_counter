from app import db

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(64), index=True, unique=True)
    count = db.Column(db.Integer(), index=True, unique=True)
   
    def __repr__(self):
        return '<Url {url} count is {count}>'.format(url = self.url, count = self.count)