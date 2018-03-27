
from flask import Flask, render_template, redirect, url_for, request, session
import mlab
from models.phone import Phone
from models.average import Average
import re

mlab.connect()

app = Flask(__name__)

app.secret_key = "tuan@123"

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # phone_list = Phone.objects()
        SP_ordered = Average.objects().order_by("-averagePoint") # dau tru tuc la largest to smallest
        top4 = []
        for i in SP_ordered[0:4]:
            phone_dict = {}
            phone_dict["phone"] = Phone.objects.get(id=i.phone)
            phone_dict["averagePoint"] = round(i.averagePoint, 1)
            top4.append(phone_dict)
        return render_template('index.html', top4=top4)

    elif request.method == "POST":
        # form = request.form
        # name1 = form["name1"]
        # name2 = form["name2"]
        # regex1 = re.compile(name1)
        # regex2 = re.compile(name2)
        # phone_li1 = Phone.objects(product_name=regex1)
        # phone_li2 = Phone.objects(product_name=regex2)
        # session["phone_li1"] = phone_li1
        # session["phone_li2"] = phone_li2

        return redirect("/result")


@app.route('/result', methods=["GET", "POST"])
def result():
    if request.method == "GET":
        SP_ordered = Phone.objects()
        phone_li1 = SP_ordered[0:3]
        phone_li2 = SP_ordered[4:7]
        print(phone_li1[0].product_name)
        print(phone_li2[0].product_name)
        return render_template('result.html', phone_li1=phone_li1, phone_li2=phone_li2)
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        # name1 = form["name2"]
        # regex1 = re.compile(name1)
        # regex2 = re.compile(name2)
        # phone_li1 = Phone.objects(product_name=regex1)
        # phone_li2 = Phone.objects(product_name=regex2)
        return "a"



if __name__ == '__main__':

    app.run(debug=True)
