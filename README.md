Team Details:

Sanju Sabu S20200010187
Meet Jain S20200010126

Project Overview

An IR system to retrieve the tweets using a query entered and ranking them according to their score.

The following have been implented :

1. Stemming, Stopwords removal, Tokenisation.
2. Building the inverted index, and tfidf weighting.
3. Calculating the cosine similarity and ranking the documents.
4. Writing the result into "/dist/Results.txt"
5. Capturing user feedback

Setting Up and Running the Code:

1. python3 installed and executable.
2. nltk libaries installed (all of these can be downloaded using python3 -> import nltk -> nltk.download('corpus | tokenize | stem.porter'):
3. Install flask from frontend.
4. Run the server.py file and enter the query and press search.
5. We get the result with the rank,docno, tweet, and score.
6. The user can then choose if the tweet is relevant or not.
