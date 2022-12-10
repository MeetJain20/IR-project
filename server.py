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
    result_array = list((line.strip('\n') for line in open(
        "./dist/Results.txt", 'r')))
    finResult = []
    for meet in result_array:
        x = meet.strip()
        my_list = x.split(' ')
        new_list = []
        for jain in my_list:
            print("\n")
            if jain != '':
                new_list.append(jain)
        finResult.append(new_list)
    return render_template("displayTable.html", tweet_list=finResult)


app.run()
