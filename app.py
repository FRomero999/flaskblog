from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3307
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pacoromero'
app.config['MYSQL_DB'] = 'blog'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_DATABASE_CHARSET'] = 'utf-8'

mysql = MySQL(app)

import database as db


@app.route('/')
def index():
    posts = db.get_all_posts()
    return render_template('index.html', posts=posts)

@app.route('/<int:id_post>')
def post(id_post):
    post = db.get_post(id_post)
    return render_template('post.html', post=post)

app.run()
