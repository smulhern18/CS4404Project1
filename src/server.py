from flask import Flask, render_template, request, current_app, url_for, redirect
import initializeDatabase
from database import Database
from datetime import date

global app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=["GET", "POST"])
def submit():
    if (request.method == "GET"):
        print("GET request")
        return render_template('submitted.html')
    else:
        ipAddress = request.remote_addr
        todayDate = date
        choice = request.form.getlist('candidates')
        print(choice)
        Database.add_vote(ipAddress, todayDate, choice)
        return render_template('submitted.html')


def create_app():
    dbConnector = initializeDatabase.init()
    app.config["DEBUG"] = True
    db = Database()
    app.config["db"] = db


if __name__ == "__main__":
    create_app()
    app.run(host="localhost", port=8080, debug=True)


