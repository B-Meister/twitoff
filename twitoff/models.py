"""
SQLAlchemy models and utility functions for TwitOff
"""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    """Twitter uses corresponding to Tweets."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    # Tweet IDs are ordinal ints, so they can be used to fetch more recent tweets
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return '-User {}-'.format(self.name)


class Tweet(DB.Model):
    """Tweet test and data."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))  # Allows for texts + links
    embedding = DB.Column(DB.PickleType, nullable=False)
    # user_id is the foreign key
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
    # ^ no longer need to use join because of this line

    def __repr__(self):
        return '-User {}-'.format(self.text)
    # must add tweet to database and then append it to the user and commit



