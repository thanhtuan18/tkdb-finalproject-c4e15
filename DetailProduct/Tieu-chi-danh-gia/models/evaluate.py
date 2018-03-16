from mongoengine import Document, IntField,StringField


class Evaluate(Document):
    design = IntField()
    screen = IntField()
    func = IntField()
    exp = IntField()
    cam = IntField()
    pin = IntField()
    comment = StringField()
