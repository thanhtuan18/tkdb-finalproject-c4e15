import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds147265.mlab.com:47265/projectphonemarker

host = "ds147265.mlab.com"
port = 47265
db_name = "projectphonemarker"
user_name = "admin"
password = "admin"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)
