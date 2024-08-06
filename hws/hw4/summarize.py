from tfidf import *
import os
import pickle

"""
python summarize.py ~/data/reuters-vol1-disk1-subset/33312newsML.xml
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


1. Run compute_tok_corpus.py ~/data/reuters-vol1-disk1-subset to produce the pickle file with tokenized corpus.
2. Load ~/data/tok_corpus.pickle into a list.
3. Compute doc_freq of tokens.
4. Summarize the input xml input file (top 20).
5. Print the tfidf of top 20 words with three decimals of precision. Print only those words scoring >= 0.01. In your summarize() function, discard any terms with scores < 0.01.

"""

summarize_file = sys.argv[1]

pickle_file = os.path.expanduser("~/data/tok_corpus.pickle")
with open(pickle_file, 'rb') as file:
    tok_corpus = pickle.load(file)

# your code here 
