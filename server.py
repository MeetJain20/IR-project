from flask import Flask
from flask import render_template
from flask import request
import main

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/display-results", methods=["GET"])
def hello_world():
    query = request.args.get('query', '')
    print(request)
    main.evaluate(query)
    tweet_list = [
        "hello world",
        "hehe"
    ]
    return render_template("displayTable.html", tweet_list=tweet_list)

app.run()