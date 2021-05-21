from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Information(db.Model):
    __tablename__ = 'info'
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime)
    write_date = db.Column(db.DateTime)
    sequence = db.Column(db.String(255))
    passkey = db.Column(db.String(255))
    url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    preview = db.Column(db.Text)
    content = db.Column(db.Text)
