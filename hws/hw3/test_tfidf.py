from tfidf import *
import pickle
import sys

"""
pytest -v

test_tfidf.py::test_load_corpus PASSED                                                                       [ 14%]
test_tfidf.py::test_gettext PASSED                                                                           [ 28%]
test_tfidf.py::test_tokenize PASSED                                                                          [ 42%]
test_tfidf.py::test_doc_freq PASSED                                                                          [ 57%]
test_tfidf.py::test_compute_tfidf_i PASSED                                                                   [ 71%]
test_tfidf.py::test_compute_tfidf PASSED                                                                     [ 85%]
test_tfidf.py::test_summarize PASSED                                                                         [100%]
"""

testfiles = [
	"33214newsML.xml",
	"33232newsML.xml",
	"33029newsML.xml",
	"32899newsML.xml",
	"32775newsML.xml",
	"32770newsML.xml",
	"32664newsML.xml",
	"32611newsML.xml",
	"32351newsML.xml",
	"32238newsML.xml",
	"3214newsML.xml",
	"32030newsML.xml",
	"2878newsML.xml",
	"2900newsML.xml",
	"2804newsML.xml",
	"2433newsML.xml",
	"198798newsML.xml"
]


title_text = 'Example news item. Here is the text for the example news item. It has two paragraphs.'

tok_corpus = [
 ['cat', 'hat'],
 ['green', 'egg', 'ham', 'sam', 'cat'],
 ['fox', 'jump', 'lazi', 'dog', 'cat'],
 ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'],
 ['like', 'green', 'egg', 'ham'],
 ['sam', 'hat', 'ham', 'cat']
]

freq_expected = {'cat': 4,
 'hat': 2,
 'egg': 2,
 'green': 2,
 'ham': 3,
 'sam': 2,
 'dog': 1,
 'fox': 1,
 'jump': 1,
 'lazi': 1,
 'blue': 1,
 'fish': 1,
 'one': 1,
 'red': 1,
 'two': 1,
 'like': 1}

tfidf_expected = [{'cat': 0.091, 'hat': 0.347},
 {'cat': 0.036, 'egg': 0.139, 'green': 0.139, 'ham': 0.081, 'sam': 0.139},
 {'cat': 0.036, 'dog': 0.22, 'fox': 0.22, 'jump': 0.22, 'lazi': 0.22},
 {'blue': 0.137, 'fish': 0.549, 'one': 0.137, 'red': 0.137, 'two': 0.137},
 {'egg': 0.173, 'green': 0.173, 'ham': 0.101, 'like': 0.275},
 {'cat': 0.046, 'ham': 0.101, 'hat': 0.173, 'sam': 0.173}]

expected_summary = [('net', 0.158),
                    ('share', 0.156),
                    ('jul', 0.156),
                    ('loss', 0.132),
                    ('income', 0.105),
                    ('outstanding', 0.078),
                    ('week', 0.063),
                    ('weight', 0.063),
                    ('average', 0.053),
                    ('acquisition', 0.039)]

xml_dir = "~/data/reuters-vol1-disk1-subset"
xml_dir = os.path.expanduser(xml_dir) 
print("path to xml files is {}".format(xml_dir))


def test_gettext():
    text = gettext("test_file.xml")
    assert text == title_text

def test_tokenize():
    nlp = spacy.load("en_core_web_sm")
    expected = ['example', 'news', 'item', 'text', 'example', 'news', 'item', 'paragraph']
    assert tokenize(title_text, nlp) == expected
    assert tokenize("Hello World!", nlp) == ['hello', 'world']
    assert tokenize("This is sentence one. This is sentence two.", nlp) == ['sentence', 'sentence']
    assert tokenize("The well-known actor appeared on TV.", nlp) == ['know', 'actor', 'appear']

def test_doc_freq():
    freq = doc_freq(tok_corpus)
    for w in freq_expected:
        assert freq[w] == freq_expected[w]

def test_compute_tfidf_i():
    tfidf = compute_tfidf_i(tok_corpus[0], freq_expected, len(tok_corpus))
    expected = {'cat': 0.091, 'hat': 0.347}
    for w in tfidf:
        assert round(tfidf[w], 3) == expected[w] 

def test_compute_tfidf():
    tfidf = compute_tfidf(tok_corpus, freq_expected)
    for i in range(len(tfidf_expected)):
        for w in tfidf_expected[i]:
            assert tfidf_expected[i][w] == round(tfidf[i][w], 3)

def test_summarize():
    nlp = spacy.load("en_core_web_sm")
    testfile_paths = [os.path.join(xml_dir, file) for file in testfiles]
    text_corpus = [gettext(f) for f in testfile_paths]
    tok_corpus = [tokenize(text, nlp) for text in text_corpus]
    test_doc_freq = doc_freq(tok_corpus)
    file_path = os.path.join(xml_dir, "2900newsML.xml")
    sum0 = summarize(file_path, test_doc_freq, len(tok_corpus), 10)
    for i, (k, v) in enumerate(expected_summary):
        (k0, v0) = sum0[i]
        assert k == k0
        assert v == round(v0, 3)

