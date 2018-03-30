from mongoengine import *
import datetime

class Blog(Document):
    title = StringField(max_length=200, required=True)
    author = StringField()
    date_modified = DateTimeField(default=datetime.datetime.utcnow)
