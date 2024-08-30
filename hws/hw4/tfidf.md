# TFIDF with SpaCy

*All projects in this class are individual projects, not group projects.  You may not look at or discuss code with others until after you have submitted your own individual effort.*

## Goal

The goal of this homework is to learn a core technique used in text analysis called *TFIDF* or *term frequency, inverse document frequency*.  We will use what is called a *bag-of-words* representation where the order of words in a document doesn't matter--we care only about the words and how often they occur. A word's TFIDF value is often used as a feature for document clustering or classification. The more a term helps to distinguish its enclosing document from other documents, the higher its TFIDF score. As such, words with high TFIDF scores are often very good summarizing keywords for document.

As a practical matter, you will learn how to process some real XML files (Reuters articles) in Python.

## Getting started

I have provided a starter kit in github. Also download the `reuters-vol1-disk1-subset.zip` file from the files area of Canvas. You will be processing that file as a zip but you can unzip it as well so that you can test individual files. Copy this file to `~/data/`.`

## Deliverables

In your repository you must have the following files in the root of your repository directory:

* `tfidf.py`; Implement methods `gettext()`,`tokenize()`,`doc_freq()`,`compute_tfidf_i()`,`compute_tfidf()`,`summarize()`
* `common.py`; Print most common 10 "*word* *score*" pairs
* `compute_tok_corpus.py`; tokenizes the entire corpus and saves it into a pickle file.
* `summarize.py`; Print up to 20 scores with **three decimals of precision**

## Evaluation

We will test your TFIDF functionality using `test_tfidf.py`, which uses the entire corpus for "training" but then uses just a small subset of the files for testing. For example, on my machine:

```bash
$ pytest -vv test_tfidf.py
============================================== test session starts ===============================================
test_tfidf.py::test_gettext PASSED                                                              [ 14%]
test_tfidf.py::test_tokenize PASSED                                                             [ 28%]
test_tfidf.py::test_tokenize_2 PASSED                                                           [ 42%]
test_tfidf.py::test_doc_freq PASSED                                                             [ 57%]
test_tfidf.py::test_compute_tfidf_i PASSED                                                      [ 71%]
test_tfidf.py::test_compute_tfidf PASSED                                                        [ 85%]
test_tfidf.py::test_summarize PASSED                                                            [100%]

```

## Description

### Reading in Reuters' XML
To begin, retrieve text from a Reuters article in XML format. You can download the `reuters-vol1-disk1-subset.zip` compressed Reuters corpus containing 9164 files from Canvas. Please note that this data should not be shared publicly, so refrain from posting the articles anywhere. Once downloaded, copy the zip file to the `~/data` directory and extract its contents.

We will use `etree` from the lxml library to process XML. Use the function `xpath` as we have used in previous labs. 


### Tokenizing text

Now that we have extracted raw text devoid of XML tags, let's proceed to tokenize English text properly. This entails a multistep process, some of which you may recall from previous projects or labs:

1. Begin by converting all text to lowercase and  removing punctuation, numbers, and special characters such as \r, \n, and \t.
2. Replace multiple consecutive spaces with a single space.
3. Utilize SpaCy for tokenization with the English language model loaded as follows: nlp = spacy.load("en_core_web_sm").
4. Apply a stopword removal step using SpaCy to eliminate common stopwords.
5. Exclude words with a length less than 3 characters.
6. Lastly, employ SpaCy for lemmatization to obtain the base forms of words.


### Sample application

Our sample application for tokenization will be in `common.py` and will summarize an article by showing the most common words. The input file is specified as a commandline argument and used from Python via `sys.argv[1]`. Follow the following steps:

1. Use `gettext` to get the text of the xml file.
2. Tokenize the text with `tokenize`.
3. Compute word counts with Counter.
4. Print most common words with counts.

**Sample output.** For file `33313newsML.xml` in our `reuters-vol1-disk1-subset` data directory, we would get the following output:

```
$ python common.py ~/data/reuters-vol1-disk1-subset/33313newsML.xml
power 14
transmission 14
new 12
say 12
generator 12
electricity 11
cost 10
zealand 9
signal 8
charge 7
```


For file `33312newsML.xml`, I get the following final output:

```
$ python common.py ~/data/reuters-vol1-disk1-subset/33312newsML.xml
awb 8
wheat 6
tonne 6
say 6
steady 4
price 4
crop 4
report 3
queensland 3
australian 2
```

This works great but can we do better? 

### TFIDF

Our "most common word" mechanism is simple and pretty effective but not as good as we can do.  We need to penalize words that are not only uncommon in that article but common across articles.

We need to use TFIDF on a corpus of articles from which we can compute the term frequency across articles.  Here is how we will execute our program (`summarize.py`):

Before we use `summarize.py`, let's tokenize the entire corpus and save the results. Follow the following steps in the `compute_tok_corpus.py` file:

1. Get a list of all xml_files in the corpus (~/data/reuters-vol1-disk1-subset).
2. Get a list of texts for all files xml_files.
3. Get a list of tokenized text (list of list of tokens).
4. Save the tokenized corpus in ~/data/tok_corpus.pickle.


To complete the summarize.py code follow the following steps:
1. Run `compute_tok_corpus.py ~/data/reuters-vol1-disk1-subset` to produce the pickle file with tokenized corpus.
2. Load ~/data/tok_corpus.pickle into a list.
3. Compute `doc_freq` of tokens.
4. Summarize the input xml input file (top 20).
5. Print the tfidf of top 20 words with **three decimals of precision**. Print only those words scoring >= 0.01. In your `summarize()` function, discard any terms with scores < 0.01. 

```bash
$ python summarize.py  ~/data/reuters-vol1-disk1-subset/33313newsML.xml
generator 0.178
transmission 0.172
electricity 0.115
power 0.091
zealand 0.09
signal 0.082
esanz 0.081
trans 0.081
generation 0.065
gisborne 0.061
leay 0.061
cost 0.053
island 0.05
auckland 0.046
charge 0.045
pricing 0.043
eastland 0.041
priciple 0.041
electron 0.036
efficiency 0.035
```


For file `33312newsML.xml`, I get the following final output:

```
$ python summarize.py ~/data/reuters-vol1-disk1-subset/33312newsML.xml
awb 0.542
wheat 0.234
tonne 0.165
queensland 0.16
crop 0.151
steady 0.13
frost 0.112
weekly 0.071
recede 0.066
hard 0.063
impact 0.062
australian 0.062
nsw 0.061
victoria 0.058
price 0.057
protein 0.057
wale 0.053
pool 0.05
estimate 0.049
trim 0.048
```


