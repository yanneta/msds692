from htable import *


"""
pytest -v test_htable.py
"""


def get_xyz_table():
    table = htable(5)
    htable_put(table, "a", "x")
    htable_put(table, "b", "y")
    htable_put(table, "c", "z")
    htable_put(table, "f", "i")
    htable_put(table, "g", "j")
    htable_put(table, "k", "k")
    return table

def test_hashcode():
    assert hashcode(7) == 7
    l = ["carrots", "apples", "carrot", "apple", "data science"]
    out = [hashcode(s) for s in l]
    expected = [90748680016, 2883905625, 2927376771, 93029210, 2623502345479838702]
    assert out == expected

def test_bucket_indexof():
    table = get_xyz_table()
    assert bucket_indexof(table, "k") == 2
    assert bucket_indexof(table, "k") == 2
    assert bucket_indexof(table, "k") == 2

def test_empty():
    expected = '0000->\n0001->\n0002->\n0003->\n0004->\n'
    table = htable(5)
    assert htable_str(table) == "{}"
    assert htable_buckets_str(table) == expected

def test_single():
    expected = '0000->\n0001->\n0002->\n0003->parrt:99\n0004->\n'
    table = htable(5)
    htable_put(table, "parrt", 99)
    assert htable_str(table) == "{parrt:99}"
    assert htable_buckets_str(table) == expected

def test_singleton():
    expected = '0000->\n0001->\n0002->\n0003->parrt:{99}\n0004->\n'
    table = htable(5)
    htable_put(table, "parrt", set([99]))
    assert htable_str(table) == "{parrt:{99}}"
    assert htable_buckets_str(table) == expected

def test_int_to_int():
    expected_str = "{5:5, 10:10, 1:1, 6:6, 2:2, 7:7, 3:3, 8:8, 4:4, 9:9}"
    expected = '0000->5:5, 10:10\n0001->1:1, 6:6\n0002->2:2, 7:7\n0003->3:3, 8:8\n0004->4:4, 9:9\n'
    table = htable(5)
    for i in range(1, 11):
        htable_put(table, i, i)
    s = htable_str(table)
    assert s == expected_str
    s = htable_buckets_str(table)
    assert s == expected


def test_str_to_str():
    expected_str = '{a:x, f:i, k:k, b:y, g:j, c:z}'
    expected = '0000->\n0001->\n0002->a:x, f:i, k:k\n0003->b:y, g:j\n0004->c:z\n'
    table = get_xyz_table()
    assert htable_str(table) == expected_str
    assert htable_buckets_str(table) == expected


def test_str_to_list():
    expected_str = '{apples:[6, 3, 1024, 99, 102342], carrots:[2, 99, 3942]}'
    expected = '0000->apples:[6, 3, 1024, 99, 102342]\n0001->carrots:[2, 99, 3942]\n0002->\n0003->\n0004->\n' 
    table = htable(5)
    htable_put(table, "carrots", [2, 99, 3942])
    htable_put(table, "apples", [6, 3, 1024, 99, 102342])
    assert htable_str(table) == expected_str
    assert htable_buckets_str(table) == expected


def test_replace_str():
    expected = '0000->\n0001->\n0002->a:i\n0003->b:y, g:k\n0004->\n'
    table = htable(5)
    htable_put(table, "a", "x")
    htable_put(table, "b", "y")
    htable_put(table, "a", "z")
    htable_put(table, "a", "i")
    htable_put(table, "g", "j")
    htable_put(table, "g", "k")
    s = htable_str(table)
    assert s == '{a:i, b:y, g:k}'
    s = htable_buckets_str(table)
    assert s == expected
