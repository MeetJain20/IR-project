from preprocess import returnDocs
from preprocess import tweetdict
rankmap = []
tweetsMap = tweetdict()
scoreMap = returnDocs()
# print(tweetsMap)
# print(scoreMap)
KrelevantDocs = dict(list(scoreMap.items())[1:11])
print(KrelevantDocs)
for key, val in KrelevantDocs.items():
    print(tweetsMap[key], "-->", val)
