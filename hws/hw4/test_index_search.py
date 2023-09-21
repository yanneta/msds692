import sys
import os

from index_search import index_search, create_index
from words import filelist, words, filenames

"""
Run with

$ python -m pytest -v test_index_search.py

test_index_search.py::test_index_tiny_text PASSED                                        [ 14%]
test_index_search.py::test_index_berlitz_none PASSED                                     [ 28%]
test_index_search.py::test_hawaii_index PASSED                                           [ 42%]
test_index_search.py::test_greek_index PASSED                                            [ 57%]
test_index_search.py::test_lisbon_index PASSED                                           [ 71%]
test_index_search.py::test_india_index PASSED                                            [ 85%]
test_index_search.py::test_dublin_and_hawaii_index PASSED                                [100%]
"""

rootdir = os.path.expanduser("~/data/berlitz1")

print("testing with dir", rootdir)

def test_index_tiny_text():
    files = ["HandRHawaii-test.txt", "HandRHongKong-test.txt"]
    index = create_index(files)
    list_keys = list(index.keys())
    list_keys.sort()
    expected = ['and', 'bathrooms', 'facing', 'has', 'hong', 'hotel', 'hotels', \
                'kong', 'large', 'luxurious', 'most', 'ocean', 'recommended', \
                'rooms', 'some', 'the', 'very', 'with', 'world']
    assert list_keys == expected
    expected_len = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1]
    for i, word in enumerate(expected):
        assert len(index[word]) == expected_len[i]

def test_index_berlitz_none():
    terms = "missspellinnng"
    files = filelist(rootdir)
    terms = words(terms)
    index = create_index(files)
    index_docs = index_search(files, index, terms)
    expected = []
    assert filenames(index_docs) == expected


def dotest(terms, expected):
    files = filelist(rootdir)
    terms = words(terms)

    index = create_index(files)
    index_docs = index_search(files, index, terms)
    names = filenames(index_docs)
    names.sort()
    expected.sort()
    assert names == expected, "found "+str(names)+" != expected "+str(expected)


def threetest(terms, expected):
    for i in range(3):
        dotest(terms=terms, expected=expected, which=i)


def test_hawaii_index():
    dotest(terms="hawaii travel", expected=['HistoryHawaii.txt'])


def test_greek_index():
    dotest(terms="greek travel",
              expected=['WhatToGreek.txt', 'WhereToLosAngeles.txt', 'WhereToFrance.txt',
                        'WhatToJapan.txt', 'WhereToMadrid.txt', 'WhereToDublin.txt',
                        'WhereToEdinburgh.txt', 'WhereToEgypt.txt', 'HistoryGreek.txt',
                        'WhereToGreek.txt', 'WhereToIndia.txt', 'WhereToIsrael.txt',
                        'WhereToIstanbul.txt', 'WhereToItaly.txt', 'WhereToJapan.txt',
                        'WhereToJerusalem.txt'])


def test_lisbon_index():
    dotest(terms="lisbon",
              expected=['HistoryMadeira.txt', 'HandRLisbon.txt', 'IntroMadeira.txt',
                        'WhereToMadeira.txt'])


def test_india_index():
    dotest(terms="india", expected=['WhereToLosAngeles.txt', 'HistoryMalaysia.txt',
                                       'WhereToMalaysia.txt', 'WhatToIndia.txt',
                                       'IntroIndia.txt', 'WhereToEgypt.txt',
                                       'WhatToMalaysia.txt', 'HistoryEgypt.txt',
                                       'HistoryFrance.txt', 'HistoryFWI.txt',
                                       'HistoryGreek.txt', 'HistoryHongKong.txt',
                                       'WhereToIndia.txt', 'HistoryIndia.txt',
                                       'HistoryIstanbul.txt'])


def test_dublin_and_hawaii_index():
    dotest(terms="hawaii dublin", expected=[])

