# Search Engine Implementation

*All projects in this class are individual projects, not group projects.  You may not look at or discuss code with others until after you have submitted your own individual effort.*

The goal of this project is to learn how hashtables work and to *feel* just how much slower a linear search is. Along the way, you'll learn the basic mechanics of implementing a search engine, including displaying search results in a browser window and being able to navigate to documents. You'll also learn a tiny bit of HTML.

The functionality and the overall project itself often come up in data science interviews.


## Getting started

Please go to the and grab all the python files from github and the data files slate.7z and berlitz1.7z from Canvas. Store your data files in `~/data.`

```bash
brew install p7zip
7z x slate.7z
7z x berlitz1.7z
```
I recommend that you start by getting the simple linear search to work, which involves computing HTML and all of the basic machinery for extracting words from file content. So start by fleshing out `words.py` and `linear_search.py`.  

## Deliverables

You must complete and add these to the root of your repository:

* htable.py
* index_search.py
* linear_search.py
* myhtable_search.py (**no `dict` objects allowed in this file!**)
* words.py

If you use jinja2 templates stored on the disk, make sure those are part of the repository as well.


**The use of any `dict` objects within your `myhtable_search.py` file yields a 0 for that part of the project.**
**Please do not add the data to your repository!**


## Evaluation

To evaluate your projects, we will run the following tests:


```bash
$ pytest

test_htable.py .........                                                                 [ 31%]
test_index_search.py .......                                                             [ 55%]
test_linear_search.py ......                                                             [ 75%]
test_myhtable_search.py .......                                                          [100%]
```

## Discussion

A **search engine** accepts one or more **terms** and searches a corpus for files matching *all* of those terms.  A **corpus** is just a directory and possibly subdirectories full of text files. If you go to the [American National corpus](http://www.anc.org/data/oanc/contents/), you'll see lots of fun text data. We will be working with some articles from Slate magazine and also from Berlitz travelogues. Berlitz is smaller and so we will be using it for unit test.

In repo you're going to implement 3 different search mechanisms:

1. Linear search; file `linear_search.py`
2. Hashtable via built in Python `dict` objects; file `index_search.py`
3. Hashtable that you implement yourself; file `myhtable_search.py`

All three mechanism should give exactly the same results, but you will notice that the linear search is extremely slow.

File search.py  is the main program, which you execute like this:

```bash
$ python search.py linear ~/data/slate
$ python search.py index ~/data/slate
$ python search.py myhtable ~data/slate
```

Assuming you have placed the `slate` directory under a `data` directory in your home directory. Here is what the program looks like in action:

```bash
$ python search.py linear ~/data/slate
4530 files
Search terms: Reagan Iran
```

After you enter the search terms and hit return, the Python program pops up your default browser on the HTML file you have just generated as a result of the search.

**Please do not add data files to your repository!** I don't need them and it takes forever to download your repos if you add the data. 

### Linear search

Your first task is to perform a linear search, which looks at each file in turn to see if it contains all of the search terms. If it does, that filename is included in the list (not `set`) of matching documents. (Function `results()` expects a list, not a set.)

Given a list of fully-qualified filenames for files containing the search terms, the main program in search.py uses function `results()` to get a string containing HTML, which `search.py` writes to file `/tmp/results.html`. It then requests, via `webbrowser.open_new_tab()`, that your default browser open that page.

### HTML output

You can create whatever fancy HTML you want to show search results, but here is the basic form you should follow:

```
<html>
    <body>
       <h2>Search results for <b> hawaii</b> in 30 files</h2>
       <p> <a href=file:///Users/yannetinterian/teaching/data_acquisition/hws/hw2/data/slate/50/ArticleIP_29630.txt>/Users/yannetinterian/teaching/data_acquisition/hws/hw2/data/slate/50/ArticleIP_29630.txt</a><br>
       Hawaii, of Polynesian and Samoan ancestry. In 1993, Akebono became the first<br><br>
       <p> <a href=file:///Users/yannetinterian/teaching/data_acquisition/hws/hw2data/slate/34/ArticleIP_2251.txt>/Users/yannetinterian/teaching/data_acquisition/hws/hw2/data/slate/34/ArticleIP_2251.txt</a><br>
       in local races in Hawaii, South Americans giving to the Democratic Party of<br><br>
...    
</body>
</html>
```      

Notice that the links are URLs just like you see going to websites except they refer to a file on the local disk instead of another machine because of the `file://` prefix.

Also notice that in my search results, I am showing up to 2 lines containing at least one of the search term(s). You must also wrap any search terms in `<b>` (bold) tags.

You can use the template engine [jinja2](https://jinja.palletsprojects.com/en/3.0.x/), or just put together strings in order to create the HTML.

### Creating an index using `dict`

<img src="../figures/word-index.png" width="150" align="right">Rather than looking through each file for every search, it's better to create a fast lookup index that maps a word to all of the files that contain that word. To compute the search results for multiple words, find the intersection of documents among the document set (`index[w]`) for each word. The resulting set will be just the documents that have all words.  `index[w]` returns a set (or unique list) of integers representing document indexes into your document list, `files`. In this way we don't have to duplicate the string for filenames in all of the `index` values. You can then convert a set of file indexes to filenames using the `files` list created during index creation, which might look something like:

<img src="../figures/file-index.png" width="120">

It takes about the same time to create the index as it does to do one linear search because both are linearly walking through the list of files. The complexity of index creation is *O(n)* for *n* total words in all files. BUT, searching takes just *O(1)*, or constant time, once we have the index.  

The main program uses the following sequence for this `dict` version of the search engine:

```python
index = create_index(files) # files is a list of fully-qualified filenames
docs = index_search(files, index, terms) # terms is a list of normalized words
```

Once the index is created, function `index_search()` can crank out search results faster than you can take your fingers off the keyboard.

Here are the two key methods you must implement:
 
```python
def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document IDs. A document ID is just the index into the
    files parameter (indexed from 0) to get the file name. Make sure that
    you are mapping a word to a set of doc IDs, not a list.
    For each word w in file i, add i to the set of document IDs containing w
    Return a dict object mapping a word to a set of doc IDs.
    """
```

```python
def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of
    filenames whose file contents has all words in terms parameter as normalized
    by your words() function.  Parameter terms is a list of strings.
    You can only use the index to find matching files; you cannot open the files
    and look inside.
    """
```

These functions will use expressions like `index[w]`, where `index` is a `dict`, to get the document IDs containing word `w`.

### Creating an index using your own hashtable

We know that a linear search of a list of associations is slow because it requires a search through all associations, in the worst case. But how can we find something without looking through all the items?

A **hashtable**  is a data structure used for efficient data retrieval and storage. A hashtable is a list of buckets and a bucket is a list of associations mapping an arbitrary key to arbitrary value.  The only real restriction is that the key must be immutable such as a string, a number, tuple, etc... We compute a function, a **hash function**, on the key that indicates the partition to search for that key. Because that function could yield arbitrary integers and we have finite computers, we convert the hash function value to a bucket index using the modulo operator with the number of buckets.  If there are 10 buckets, then we modulo 10 and the resulting value is *[0,9]*.  With a uniform distribution, we would expect roughly *N*/*B* associations in each bucket for *B* buckets and *N* total elements in the dictionary.  A complexity of *N*/*B* is much better than *N* and, with sufficiently large *B*, we would say that *N*/*B* approaches 1, giving complexity *O(1)* versus *O(n)*.

Because we are not currently studying the object-oriented aspects of Python, we are going to represent a hashtable as a list of lists (list of buckets):

```python
def htable(nbuckets):
    """Return a list of nbuckets empty lists"""
```

The number of buckets should be a prime number to avoid hash code collisions. In memory, the empty hash table looks like (with 5 buckets):

<img src=../figures/hashtable-empty.png width=140>

Let's look at an example that adds something to our hashtable. Imagine that our keys are always single element strings like `'a'`, which means we can use their character code as the hash code. That hash code could be some very large number in general, so we need to constrain it in 0..*B*-1. The modulo operator, `%`, takes care of that for us:

```python
key = 'a'
value = 'tom'
def hashcode(o):
	return ord(o) # assume keys are single-char strings
print("hashcode =", hashcode(key))
bucket_index = hashcode(key) % len(table)
print("bucket_index =", bucket_index)
```

Gives:

```python
hashcode = 97
bucket_index = 2
```

To actually add something to the hash table, we get the bucket and then add an association tuple to the list:

```python
bucket = table[bucket_index]
bucket.append( (key,value) ) # add association to the bucket
```

The data structure now looks like this:

<img src=../figures/hashtable3.png width=180>

Different hash codes can hash to the same bucket because of the modulo operation that constrains the hash code value. For example, `'f'` will also have to the same bucket despite having a different hash code:

```python
key = 'f'
value = 'mary'
print "hashcode =", hashcode(key)
bucket_index = hashcode(key) % len(table)
print "bucket_index =", bucket_index
bucket = table[bucket_index]
bucket.append( (key,value) ) # add association to the bucket
```

Gives:

<img src=../figures/hashtable4.png width=250>

The straight in-line code to add those two elements would look like:
 
```pytnon
table[ord('a')%5].append( ('a','tom') )  # 'a'==97
table[ord('f')%5].append( ('f','mary') ) # 'f'==102
```
 
Ok, back to this specific project. The version of the search engine you create for this section should look and perform just like the version using `dict`. The difference is **you cannot use the built-in dictionary operations** like `index[k]` for `dict` `index` and key `k`. You will build your own hashtable and call your own `get` and `put` functions explicitly to manipulate the index.

Each element in a bucket is an association `(key,value)` where `value` is a set or unique list of document indexes. The buckets are themselves lists; do not confuse the buckets with the set of document indexes in each association. For example, `htable_put(index, 'parrt', [99])` should add tuple `('parrt',[99])` to the bucket associated with key string `parrt`. The following method embodies the put operation:

```python
def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket indicated by key and then append (key,value)
    to that bucket if the (key,value) pair doesn't exist yet in that bucket.
    If the bucket for key already has a (key,value) pair with that key,
    then replace the tuple with the new (key,value).
    Make sure that you are only adding (key,value) associations to the buckets.
    The type(value) can be anything. Could be a set, list, number, string, or anything!
    """
```

In our case our values for the association are sets of document IDs.  If `ronald` is in documents 9 and 3 and `reagan` is in document 17 and both of those terms hashed to bucket 0, you would see the following 2-element bucket 0 with two associations:

<img src=../figures/hashtable2.png width=300>


To make that work, you need a function that computes hash codes:

```python
def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
```

*We are only computing hash codes for string and integer keys but mapped values can be of any type.* The hash code for a string could be just the sum of all of all the character ASCII codes, via `ord()`, but that would mean a lot of collisions like `pots` and `stop`.  A collision is when different keys hash to the same bucket. Ideally we would have one association per bucket. The "distribution" of elements to buckets is a function of how many buckets we have and how good our hash function is. The multiplication by prime number 31 starts shifting the bits around and gets a bit of "randomness" into our key computation.

The hash code is not directly used to get the bucket index because the hash code will typically be many times larger than the number of buckets.  The index of a bucket is the hash code modulo the number of buckets:

```python
bucket = hashcode(key) % nbuckets
```

To get a value out of the hash table associated with a particular key, we use this function:

```python
def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """
```

It computes the bucket where `key` lives and then linearly searches that (hopefully) small bucket for an association with key `key`. It then returns the value, the second element, from that association.

<img src="../figures/redbang.png" width=30 align="left"> Building a search index on top of your own implementation of a hash table can be quite confusing. This is particularly so because we are associating a word (string) with a **mutable** set of document IDs.

The confusing part is how you update the search index entries when it is your own hash table implementation. If you look at the example from above, where `'a'` maps to `tom`, we can see that changing `tom` to `jane` requires that we replace that mapping. Tuples are immutable and so is `99`. So, we replace the entire tuple `('a',tom)` with `('a',jane)`. 

Now look at the example where we map `'ronald'` to set `{9,3}`.  That set is **mutable** so, if you want to update the set, you don't have to replace the `('ronald', {9,3})` association in the hash table. Just update the set that already exists.  You would need to initialize the search index with empty sets as part of your search index initialization but after that the hash table "get" will retrieve the existing set. You can then simply call set `add()` to add a document ID to that set. Recall the slide from lecture:

<img src="../figures/mutable-values.png" width="500" align="center">

To create `mytable_search.py`, copy `index_search.py` and modify the code that uses `dict` objects to use your functions from `htable.py`. For example, replace `index[w]` expressions with `htable_get(index, w)`.

