# Import helper functions
from preprocess import importQuery, importTweets, buildIndex, lengthOfDocument,tweetdict,returnDocs 
from results import retrieve
from write import resultFileCreation


def evaluate(query=""):
    print(query)

    print("\n Preprocessing... \n")
    returnDocs()
    maptweets = tweetdict()

    tweets = importTweets()
    

    query_file = importQuery()
    # print(query_file)
    # Build the inverted index.
    index = buildIndex(tweets)
    
    # Get the length of each document.
    document_length = lengthOfDocument(index, tweets)

    print("\n Preprocessing Done! \n")
    print("\n Retrieval and Ranking... \n")
    # Get length of query.
    ranking = retrieve(query_file, index, document_length)

    print("\n Retrieval and Ranking Done! \n")

    print("\n Starting to create Result File... \n")

    resultFileCreation(ranking)

    print("\n Result File Creation Done! \n")

    # news = returnDocs()


if __name__ == "__main__":
    evaluate()
