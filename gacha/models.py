from gacha import db

class Follower(db.Model):
    __tablename__ = 'followers'
    user_id = db.Column(db.Integer, primary_key=True)
    screen_name = db.Column(db.String)

    def __repr__(self):
        return self.screen_name

class Reply(db.Model):
    __tablename__ = 'replies'
    rep_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)

    def __repr__(self):
        return self.text

def init():
    db.create_all()
