from flask import Flask, render_template, url_for
from flask_mysqldb import MySQL
import config

app = Flask(__name__)

app.config['MYSQL_HOST'] = config.host
app.config['MYSQL_USER'] = config.user
app.config['MYSQL_PASSWORD'] = config.password
app.config['MYSQL_DB'] = config.database

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard')
def dasboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(port=3000, debug=True)