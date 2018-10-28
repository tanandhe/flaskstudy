# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:51:24 2018

@author: Administrator
"""

from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User_Agent')
    res = make_response("<h1>The response carries a cookie</h1>")
    res.set_cookie('answer','42')
    return res
@app.route('/user/<id>')
def user(id):
    cookie = request.cookies.get('answer')
    if not id:
        abort(404)
    return cookie+id
@app.route('/404/')
def reDirect():
    return redirect('http://www.baidu.com')
if __name__ == '__main__':
    app.run(debug = True,host='0.0.0.0',port=80)