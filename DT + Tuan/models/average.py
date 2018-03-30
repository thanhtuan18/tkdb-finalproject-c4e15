from mongoengine import*

class Average(Document):
    phone = StringField()
    averagePoint = StringField()
