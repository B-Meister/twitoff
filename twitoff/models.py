"""
SQLAlchemy models and utility functions for TwitOff
"""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    """Twitter uses corresponding to Tweets."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

    def __repr__(self):
        return '-User {}-'.format(self.name)


class Tweet(DB.Model):
    """Tweet test and data."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))  # Allows for texts + links
    # user_id is the foreign key
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user_id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
    # ^ no longer need to use join because of this line

    def __repr__(self):
        return '-User {}-'.format(self.name)
    # must add tweet to database and then append it to the user and commit


def insert_example_users():
    """ Example of data to insert/play with.
        more for testing purposes """
    austen = User(id=1, name='austen')
    elon = User(id=2, name='elonmusk')
    DB.session.add(austen)
    DB.session.add(elon)
    DB.session.commit()

