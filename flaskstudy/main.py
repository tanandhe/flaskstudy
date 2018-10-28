# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:51:24 2018

@author: Administrator
"""

from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug = True)