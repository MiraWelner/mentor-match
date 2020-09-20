from flask import Flask, render_template, request
import os
import sqlite3
import requests
import json

app = Flask(__name__)
@app.route('/')
def root():
    return render_template('index.html')

@app.route('/make_profile')
def make():
    return render_template('make_profile.html')

@app.route('/view_profile')
def view():
    return render_template('view_profile.html')    

@app.route('/view_matches')
def match():
    return render_template('view_matches.html')    

@app.route('/submitName', methods = ['GET', 'POST'])
def submitName():
    sendList = request.form.to_dict()
    return str(sendList)

@app.route('/submitMentor', methods = ['GET', 'POST'])
def submitMentor():
    sendList = request.form.to_dict()
    return str(sendList)

@app.route('/submitStudy', methods = ['GET', 'POST'])
def submitStudy():
    sendList = request.form.to_dict()
    return str(sendList)

@app.route('/submitFriend', methods = ['GET', 'POST'])
def submitFriend():
    sendList = request.form.to_dict()
    return str(sendList)

@app.route('/submitRoom', methods = ['GET', 'POST'])
def submitRoom():
    sendList = request.form.to_dict()
    return str(sendList)

if __name__ == '__main__':
    app.run(host='0.0.0.0')