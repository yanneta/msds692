# pytest -v test_doc2vec.py

from doc2vec import *

article = ["tech/1.txt", "title", "", np.array([0,0,0])]

articles = [["tech/384.txt", "tech", "", np.array([1.5,0,0])],
            ["tech/4.txt", "more tech", "", np.array([0,0,2])],
            ["tech/3.txt", "mas tech", "", np.array([0,0,1])],
            ["tech/1.txt", "title", "", np.array([0,0,0])]]


def test_load_glove():
    expected = [-0.1393, 0.15164, -0.27668]
    d = load_glove("test_glove.txt")
    assert len(d) == 166
    for i in range(3):
        assert np.abs(d["meeting"][i] - expected[i]) < 1e-7

def test_words():
    text = "the,: . of to and in a s for - that on is was said with he as it by at"
    assert words(text) == ['said']
    text = "iraq use members each area found, official sunday place go based" 
    expected = ['Iraq', 'use', 'members', 'area', 'official', 'sunday', 'place', 'based']
    words(text) == expected

def test_doc2vec():
    text = "iraq use members each area found, official sunday place go based"
    gloves = load_glove("test_glove.txt")
    assert len(doc2vec(text, gloves)) == 300
    text = "a sunday,"
    doc2vec(text, gloves) == gloves["sunday"]

def test_distances():
    dist = distances(article, articles)
    assert [a[0] for a in dist] == [1.5, 2.0, 1.0, 0]

def test_recommended():
    top_3 = recommended(article, articles, 3)
    assert [a[1] for a in top_3] == ['3.txt', '384.txt', '4.txt']

