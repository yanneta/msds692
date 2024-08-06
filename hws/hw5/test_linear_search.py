import sys
import os

from linear_search import linear_search
from words import filelist, words, filenames

"""
Run with
pytest -v test_linear_search.py

test_linear_search.py::test_linear_berlitz_none PASSED                                             [ 16%]
test_linear_search.py::test_hawaii_linear PASSED                                                   [ 33%]
test_linear_search.py::test_greek_linear PASSED                                                    [ 50%]
test_linear_search.py::test_lisbon_linear PASSED                                                   [ 66%]
test_linear_search.py::test_india_linear PASSED                                                    [ 83%]
test_linear_search.py::test_dublin_and_hawaii_linear PASSED                                        [100%]
"""

rootdir = os.path.expanduser("~/data/berlitz1")

print("testing with dir", rootdir)


def test_linear_berlitz_none():
    terms = "missspellinnng"
    files = filelist(rootdir)
    terms = words(terms)
    linear_docs = linear_search(files, terms)
    expected = []
    assert filenames(linear_docs) == expected


def dotest(terms, expected):
    files = filelist(rootdir)
    terms = words(terms)
    expected.sort()
    linear_docs = linear_search(files, terms)
    names = filenames(linear_docs)
    names.sort()
    assert names == expected, "found "+str(names)+" != expected "+str(expected)

def test_hawaii_linear():
    dotest(terms="hawaii travel", expected=['HistoryHawaii.txt'])

def test_greek_linear():
    dotest(terms="greek travel",
              expected=['WhatToGreek.txt', 'WhereToLosAngeles.txt', 'WhereToFrance.txt',
                        'WhatToJapan.txt', 'WhereToMadrid.txt', 'WhereToDublin.txt',
                        'WhereToEdinburgh.txt', 'WhereToEgypt.txt', 'HistoryGreek.txt',
                        'WhereToGreek.txt', 'WhereToIndia.txt', 'WhereToIsrael.txt',
                        'WhereToIstanbul.txt', 'WhereToItaly.txt', 'WhereToJapan.txt',
                        'WhereToJerusalem.txt'])

def test_lisbon_linear():
    dotest(terms="lisbon",
              expected=['HistoryMadeira.txt', 'HandRLisbon.txt', 'IntroMadeira.txt',
                        'WhereToMadeira.txt'])


def test_india_linear():
    dotest(terms="india", expected=['WhereToLosAngeles.txt', 'HistoryMalaysia.txt',
                                       'WhereToMalaysia.txt', 'WhatToIndia.txt',
                                       'IntroIndia.txt', 'WhereToEgypt.txt',
                                       'WhatToMalaysia.txt', 'HistoryEgypt.txt',
                                       'HistoryFrance.txt', 'HistoryFWI.txt',
                                       'HistoryGreek.txt', 'HistoryHongKong.txt',
                                       'WhereToIndia.txt', 'HistoryIndia.txt',
                                       'HistoryIstanbul.txt'])

def test_dublin_and_hawaii_linear():
    dotest(terms="hawaii dublin", expected=[])


