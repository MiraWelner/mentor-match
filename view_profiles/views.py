# really need to figure out why it's called this
# The purpose of this file is to allow users to add and alter information?

from view_profiles import app
from flask import render_template, request, redirect
import requests

categories = ["School", "Class", "Grade", "Major", "Intensity"]
School = ["UCLA","MIT", "UCD", "John Oliver Centennial Koala Chlamydia University"]
Class = ["Chemistry", "Physics", "Multivariable Calculus", "Linear Algebra", "Circuits"]
Grade = ["Freshman", "Sophomore", "Junior", "Senior"]
Major= ["Electrical Engineering", "Computer Engineering", "Computer Science", "Philosophy"]

cards = [{"card_name": "dummy_name", "card_image": "https://i.pinimg.com/originals/ed/33/47/ed33475048bb9c5229245ca8847ee241.jpg", "card_description": "stuff from database"}]
@app.route("/")
def index():
    #create objects(?) that html can access
    return render_template("view_profile.html", categories=categories, School=School, Class=Class, Grade=Grade, Major=Major, Intensity=Intensity, cards=cards)

@app.route("/func_name")
def function_name():
    return redirect("/")

#going to want a create a card function - unless mira is handling this
#unsure if search options take place here or html
