from flask import Flask
from flask import render_template
from flask import request
import main
from preprocess import returnDocs, tweetdict
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/display-results", methods=["GET"])
def hello_world():
    query = request.args.get('query', '')
    print(request)
    main.evaluate(query)
    tweetsMap = tweetdict()
    scoreMap = returnDocs()
    KrelevantDocs = dict(list(scoreMap.items())[1:11])
    # print(KrelevantDocs)
    finList = []
    for key, val in KrelevantDocs.items():
        mylist = []
        mylist.append(tweetsMap[key])
        mylist.append(val)
        finList.append(mylist)
    print(finList)
    # print(tweetsMap[key], "-->", val)

    # result_array = list((line.strip('\n') for line in open(
    #     "./dist/Results.txt", 'r')))
    # finResult = []
    # for sanju in result_array:
    #     x = sanju.strip()
    #     my_list = x.split(' ')
    #     new_list = []
    #     for jain in my_list:
    #         print("\n")
    #         if jain != '':
    #             new_list.append(jain)
    #     finResult.append(new_list)
    return render_template("displayTable.html", tweet_list=finList)


app.run()
