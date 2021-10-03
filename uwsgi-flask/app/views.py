from app import app
import os
from typing import List, Dict
import simplejson as json
from flask import request, Response, redirect, render_template, Flask, url_for, flash
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app.config['MYSQL_DATABASE_HOST'] = 'mysql-db'
app.config['MYSQL_DATABASE_USER'] = 'bowluser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Yahoo123'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'bowlera'
mysql = MySQL(cursorclass=DictCursor)
mysql.init_app(app)

@app.route('/')
def index():
    app_name = os.getenv('APP_NAME')
    if app_name:
        return(f"Hello World. This (app_name) is {app_name}.")
    return 'bowlera flask app'
