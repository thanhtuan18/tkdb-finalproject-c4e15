# import mlab
# from models.phone import Phone
#
# mlab.connect()
#
# phone_list = Phone.objects() #product_name="samsung"
# first_phone = phone_list[0]
#
# print(first_phone.to_mongo())

from flask import Flask, render_template, redirect, url_for, request, session
import mlab
from models.phone import Phone
from models.average import Average
import re

mlab.connect()
# regex = re.compile("sam sung")
#
pipeline = [
    {
        "$match" : {
            "product_name" : "Samsung Galaxy S8"
        }
    }
]

phone_li = Phone.find({"product_name" : "Samsung Galaxy S8"})


print(phone_li)
