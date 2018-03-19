from flask import Flask, render_template, redirect, url_for, request
import mlab
from models.phone import Phone

mlab.connect()
app = Flask(__name__)

@app.route('/')
def index():
    phone_list = Phone.objects()
    return render_template('index.html', phone_list= phone_list)

if __name__ == '__main__':
  app.run(debug=True)
