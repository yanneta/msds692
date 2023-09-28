# Recommending Articles

*All projects in this class are individual projects, not group projects.  You may not look at or discuss code with others until after you have submitted your own individual effort.*

The goal of this project is to learn how to make a simple article recommendation engine using word vectors ([word2vec](http://arxiv.org/pdf/1301.3781.pdf)). In particular, we're going to use a "database" of word vectors from [Stanford's GloVe project](https://nlp.stanford.edu/projects/glove/) trained on a dump of Wikipedia. The project involves reading in a database of word vectors and a corpus of text articles then organizing them into a handy table (list of lists) for processing.

Around the recommendation engine, you are going to build a web server that displays a list of [BBC](http://mlg.ucd.ie/datasets/bbc.html) articles for URL `http://127.0.0.1/:5000` (local testing):

<img src=../figures/articles.png width=200>

Clicking on one of those articles takes you to an article page that shows the text of the article as well as a list of five recommended articles:

<img src=../figures/article1.png width=450>

<img src=../figures/article2.png width=450>

## Getting started

Download the starterkit from canvas, which has the following files and structure:

```
├── doc2vec.py
├── server.py
└── templates
    ├── article.html
    └── articles.html
```

There are predefined functions with comments indicating the required functionality.

Go to your `~/data` dir and download the following data:
```
wget https://s3-us-west-1.amazonaws.com/msan692/glove.6B.300d.txt.zip
wget https://s3-us-west-1.amazonaws.com/msan692/bbc.zip
```


This project has two parts. In the first part, we will build a database of recommendations. In the second part, we will develop an app to serve these recommendations.


# Part 1: 

## Deliverables for part 1:

* doc2vec.py; complete the implementation of the unfinished functions in this file.

To validate this section, you should aim to successfully pass the following test:

`pytest -v test_doc2vec.py`


Running 
`python doc2vec.py ~/data/glove.6B.300d.txt ~/data/bbc`

Should produce files articles.pkl and recommended.pkl that will be used for the route functions in part 2. I have provided some recommendations on what to include in these files, but ultimately, it is up to you.


# Part 2: 

## Deliverables for part 2:

* server.py; implement flask routes
* templates/articles.html; use template language to generate the right HTML for the main list of articles page
* templates/article.html; use template language to generate the right HTML for an article page

To validate this section, you should aim to successfully pass the following test:

`pytest test_server.py`

In order for this test to run your app should be running locally. 


## Discussion

### Article word-vector centroids
Each word is represented by a 300-dimensional vector that captures the meaning of the word. These vectors are derived from a neural network that learns to map a word to an output vector, ensuring that neighboring words in a large corpus are close in the 300-dimensional space.

Two words are considered related if their word vectors are close in the 300-dimensional space. Similarly, when we compute the centroid of a document's cloud of word vectors, related articles should have centroids that are close in the 300-dimensional space. Words that frequently appear in a document influence the centroid by pushing it in the direction of their respective vectors. The centroid is computed by summing the vectors and dividing by the number of words in the article. By calculating the distance between the centroid of a given article and the centroids of other articles, we can determine the articles that are most similar to the article of interest. Surprisingly, this simple technique performs well.


### Efficiency of loading the glove file

It's important to be efficient with memory usage when loading the glove file because as a process runs out of memory it starts to slow down. Process the glove file one line at a time and build the dictionary in that loop; for example:

```
d = {}
for line in f.readlines():
    d[...] = ...
```

### Web server

In addition to those core functions, you also need to build a web server using flask. The server should be able to respond to two different URLs: the list of articles should be accessible at `/`, and each article should have a URL structure like `/article/business/353.txt`. The BBC corpus in directory `bbc` is organized with topic subdirectories and then a list of articles as text files:

<img src="../figures/bbc.png" width=300>

When testing from your laptop, you would go to the following URL in your browser to get the list of articles:

`http://127.0.0.1:5000/`

And to get to a specific article you would go to:

`http://127.0.0.1:5000/article/business/030.txt`


The `server.py` file contains flask "routes" for the necessary URLs. You just have to fill in those functions:

```Python
@app.route("/")
def articles():
    """Show a list of article titles"""
```

```Python
@app.route("/article/<topic>/<filename>")
def article(topic,filename):
    """
    Show an article with relative path filename.
    Assumes the BBC structure of topic/filename.txt
    so our URLs follow that.
    """
```    

Also note that we are using the template engine [jinja2](http://jinja.pocoo.org/docs/2.9/) that is built-in with flask. When you call `render_template()` from within a flask route method, it looks in the `templates` subdirectory for the file indicated in that function call. You need to pass in appropriate arguments to the two different page templates so the pages fill with data.

