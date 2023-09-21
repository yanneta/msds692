import sys
import os

from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, filenames
from htable import *
"""
Run with
$ pytest -v test_myhtable_search.py
===================================== test session starts ======================================
platform darwin -- Python 3.11.4, pytest-7.4.0, pluggy-1.0.0 -- /Users/yinterian/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/yinterian/teaching/data_acquisition/data_acquisition/hws/hw4/sol
plugins: anyio-3.5.0
collected 7 items                                                                              

test_myhtable_search.py::test_myhtable_create_index PASSED                               [ 14%]
test_myhtable_search.py::test_myhtable_berlitz_none PASSED                               [ 28%]
test_myhtable_search.py::test_hawaii_myhtable PASSED                                     [ 42%]
test_myhtable_search.py::test_greek_myhtable PASSED                                      [ 57%]
test_myhtable_search.py::test_lisbon_myhtable PASSED                                     [ 71%]
test_myhtable_search.py::test_india_myhtable PASSED                                      [ 85%]
test_myhtable_search.py::test_dublin_and_hawaii_myhtable PASSED                          [100%]
"""

rootdir = os.path.expanduser("~/data/berlitz1")

print("testing with dir", rootdir)

def test_myhtable_create_index():
    files = ["HandRHawaii-test.txt", "HandRHongKong-test.txt"]
    index = myhtable_create_index(files)
    actual = []
    for bucket in index:
        for (w, v) in bucket:
            actual.append(w)

    actual.sort()
    expected = ['and', 'bathrooms', 'facing', 'has', 'hong', 'hotel', 'hotels', \
                'kong', 'large', 'luxurious', 'most', 'ocean', 'recommended', \
                'rooms', 'some', 'the', 'very', 'with', 'world']
    assert actual == expected
    expected_len = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1]
    for i, word in enumerate(expected):
        assert len(htable_get(index, word)) == expected_len[i]


def test_myhtable_berlitz_none():
    terms = "missspellinnng"
    files = filelist(rootdir)
    terms = words(terms)
    index = myhtable_create_index(files)
    myhtable_docs = myhtable_index_search(files, index, terms)
    expected = []
    assert filenames(myhtable_docs) == expected


def dotest(terms, expected):
    files = filelist(rootdir)
    terms = words(terms)

    index = myhtable_create_index(files)
    index_docs = myhtable_index_search(files, index, terms)
    names = filenames(index_docs)
    names.sort()
    expected.sort()
    assert names == expected, "found "+str(names)+" != expected "+str(expected)


def test_hawaii_myhtable():
    dotest(terms="hawaii travel", expected=['HistoryHawaii.txt'])


def test_greek_myhtable():
    dotest(terms="greek travel",
              expected=['WhatToGreek.txt', 'WhereToLosAngeles.txt', 'WhereToFrance.txt',
                        'WhatToJapan.txt', 'WhereToMadrid.txt', 'WhereToDublin.txt',
                        'WhereToEdinburgh.txt', 'WhereToEgypt.txt', 'HistoryGreek.txt',
                        'WhereToGreek.txt', 'WhereToIndia.txt', 'WhereToIsrael.txt',
                        'WhereToIstanbul.txt', 'WhereToItaly.txt', 'WhereToJapan.txt',
                        'WhereToJerusalem.txt'])

def test_lisbon_myhtable():
    dotest(terms="lisbon",
              expected=['HistoryMadeira.txt', 'HandRLisbon.txt', 'IntroMadeira.txt',
                        'WhereToMadeira.txt'])


def test_india_myhtable():
    dotest(terms="india", expected=['WhereToLosAngeles.txt', 'HistoryMalaysia.txt',
                                       'WhereToMalaysia.txt', 'WhatToIndia.txt',
                                       'IntroIndia.txt', 'WhereToEgypt.txt',
                                       'WhatToMalaysia.txt', 'HistoryEgypt.txt',
                                       'HistoryFrance.txt', 'HistoryFWI.txt',
                                       'HistoryGreek.txt', 'HistoryHongKong.txt',
                                       'WhereToIndia.txt', 'HistoryIndia.txt',
                                       'HistoryIstanbul.txt'])


def test_dublin_and_hawaii_myhtable():
    dotest(terms="hawaii dublin", expected=[])

