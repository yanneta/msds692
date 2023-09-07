# Data translation pipeline

*All projects in this class are individual projects, not group projects.  You may not look at or discuss code with others until after you have submitted your own individual effort.*

## Goal

The goal of this assignment is to explore prevalent text-based data formats, namely csv, xml, json, and html. Parsing data files may pose challenges, but creating them is a straightforward way to gain proficiency in these languages. Throughout this homework, you will create data in various formats and employ standard Python libraries to retrieve and process the data. The only exception is that you will manually parse comma-separated value (CSV) files.

*This exercise will teach you the art of crafting structured text. Although there are libraries available for generating data in various formats, it is essential not to rely on them unless explicitly directed. Using someone else's output generation functions would hinder your learning experience and fail to address the problem at hand.*


You will be working with Python scripts rather than notebooks because we want a set of executable commands.

The basic idea is that you will be able to read in some data in csv format and pass it  along a pipeline of data conversions, ultimately getting it back to the original format. From the commandline, it will look like this:

```
$ cat data.csv | \
  python csv2xml.py | \
  python xml2csv.py | \
  python csv2json.py | \
  python json2csv.py > samedata.csv
$ diff data.csv samedata.csv | wc
       0       0       0
```

## Description

### Getting some initial stock data

The data is a CSV file with 8996 lines, which we can discover easily with `wc`:
 
```
$  wc AAPL.csv
    8996    8997  583817 AAPL.csv
```

The first thing to notice is that there is a header row that describes the data in the various columns.
 
```
$ head -4 AAPL.csv
Date,Open,High,Low,Close,Volume,Adj Close
2016-08-12,107.779999,108.440002,107.779999,108.18,18612300,108.18
2016-08-11,108.519997,108.93,107.849998,107.93,27484500,107.93
2016-08-10,108.709999,108.900002,107.760002,108.00,24008500,108.00
```

The data follows the header row, with one record per line. The key element of the CSV format is the separator, the comma. It is the column or field separator that allows us to distinguish between the elements. For *m* columns, there are *m-1* separators. For *n* records, there are *n* lines (with possibly a header row in addition).

### Parsing simple CSV files

It's often best to start with a tiny input example before tackling a bigger data set:
 
```csv
when,a,b
2016-08-12,1.2,3
2016-08-13,3.99003,4.3
```

To parse that, we read the file and convert it to a list of lines and then we split each line on commas. That gives us a list of lists. Of course, the first line of the file is special; it is the header row. Let's get this first task out of the way then by completing the following code in `mycsv.py`:

To test your solution run:
```
pytest test_mycsv.py
```

Or, if you want to go back to csv format, you could use the following Python code:

```python
print(f"header = {','.join(header)}")
for row in data:
    print(','.join(row))
```

###  Generating HTML

Now that we have `mycsv.py`, we can use it to read in CSV and dump some sample output in HTML format. This is useful for viewing large tables because the browser knows how to scroll. It's also an opportunity to learn some more HTML.

From our sample test data file, you need to generate the following HTML:

```html
<html>
<body>
<table>
<tr><th>when</th><th>a</th><th>b</th></tr>
<tr><td>2016-08-12</td><td>1.2</td><td>3.0</td></tr>
<tr><td>2016-08-13</td><td>3.99003</td><td>4.3</td></tr>
</table>
</body>
</html>
```
In file `csv2html.py`, write a small script that reads in the CSV using `readcsv(getdata())` and then prints out an HTML `table`.The program should read from standard input or from a filename parameter to the script (this is handled automatically for you by `getdata()`):

```bash
$ python csv2html.py < testdata.csv > /tmp/t.html
$ python csv2html.py testdata.csv > /tmp/t.html
```

### Generating XML

One of the most common data formats you will run into is XML (HTML is like a specific kind of XML). There are begin and end tags that must match up. XML files also tend to start with information about the version: `<?xml version="1.0"?>`, so please put that in as well.

For the test file, the output should look like the following.

```xml
<?xml version="1.0"?>
<file>
  <headers>when,a,b</headers>
  <data>
    <record>
      <when>2016-08-12</when><a>1.2</a><b>3.0</b>
    </record>
    <record>
      <when>2016-08-13</when><a>3.99003</a><b>4.3</b>
    </record>
  </data>
</file>
```

**For evaluation purposes, you must follow the order shown in that XML. The records must be in the order of the rows found in the CSV and the order of the tag names must follow the columns found in the CSV.**

*Please note that `Adj Close` is the proper name of the header, what you see in the `headers` tag. But, XML does not allow spaces in the name of the tag and so you must convert spaces to `_` characters.*

In file `csv2xml.py`, write a small script that reads in the CSV using `getdata()` and then prints out the data in XML. It also must specifically use the tags I have above: `file`, `headers`, `data`, `record`. Note that the `when` tag and the others within a record are not hardcoded: they depend on the headers from the CSV input.

The program should read from standard input or from a filename parameter to the script (this is handled automatically for you by `getdata()`:

```bash
$ python csv2xml.py < testdata.csv > /tmp/t.xml
$ python csv2xml.py testdata.csv > /tmp/t.xml
```

### Generating JSON

JSON, a format typically used for the transmission of JavaScript data objects, is also extremely popular. It is very similar to XML in that each data element is identified specifically. Naturally, JSON syntax looks quite different from XML but at an abstract level there very similar.

```json
{
  "headers":["when", "a", "b"],
  "data":[
    {
      "when":"2016-08-12", "a":"1.2", "b":"3"
    },
    {
      "when":"2016-08-13", "a":"3.99003", "b":"4.3"
    }
  ]
}
```

**For evaluation purposes, you must follow the order shown in that JSON. The records must be in the order of the rows found in the CSV and the order of the key names/data must follow the columns found in the CSV.**

You can use `jq` (`brew install jq`) to view JSON files from the commandline.

In file `csv2json.py`, write a small script that reads in the CSV using `getdata()` and then prints out the data in JSON. It also must specifically use the keys I have above: `headers`, `data`. Note that the `when` key and the others within a record are not hardcoded: they depend on the headers from the CSV input.

The program should read from standard input or from a filename parameter to the script (this is handled automatically for you by `getdata()`:

```bash
$ python csv2json.py < testdata.csv > /tmp/t.json
$ python csv2json.py testdata.csv > /tmp/t.json
```

### Reading XML Data

Parsing XML is beyond the scope of this class, but we still need to know how to use libraries that read this XML in. We're going to make a program called `xml2csv.py` that reads in XML and spits out CSV:
 
```bash
$ python xml2csv.py < /tmp/t.xml
```

There are a number of XML libraries for Python, but the simplest one to use is [untangle](https://github.com/stchris/untangle). You'll need to install `xmltodict ` as well as I use that for testing:

```bash
pip install untangle
pip install xmltodict
```

From some text, you can get a tree representation of the XML like this:

```python
xml = untangle.parse(xmltxt)
```

At this point, we need to know about the actual structure of the XML before we can pull data out. The root of the structure is the `file` tag so `xml.file` will get us that node in the tree. From there, you need to iterate over the `record` elements underneath the `data` tag. Pull out the individual values by their name such as `Date`.  Be careful how you fill in the CSV "table" for output: the order of the columns must be the order given in the headers tag.

Notice that there are no spaces in the tag names but the `headers` tag includes the real header names like `Adj Close`. You will have to take this into consideration when looking for tags in the XML.

You can check your work with:
 
```bash
$ python xml2csv.py /tmp/t.xml | python csv2xml.py > /tmp/t2.xml
$ diff /tmp/t.xml /tmp/t2.xml
```

### Reading JSON data

Parsing JSON is also beyond the scope of this class, but we still need to know how to use libraries that read this JSON in. We're going to make a program called `json2csv.py` that reads in JSON and spits out CSV:
 
```bash
$ python json2csv.py < /tmp/t.json
```

The standard `json` Python library works well. You can get a (possibly nested) dictionary from some JSON text with this:

```python
data = json.loads(jsontxt)
```

As with XML, we need to know the structure of the JSON "object" in order to pull data out of it. For example, you can pull out the headers like this:

```python
headers = data['headers']
```

Using the debugger, you can examine the various components of the `data` `dict`. I highly recommend you do that to orient yourself with the structure of the object.
 
You can check your work with:
 
```bash
$ python json2csv.py /tmp/t.json | python csv2json.py > /tmp/t2.json
$ diff /tmp/t.json /tmp/t2.json
```

## Deliverables

In your repo root directory (no subdirectories), please add:

* mycsv.py
* csv2html.py
* csv2xml.py
* csv2json.py
* json2csv.py
* xml2csv.py

You shouldn't add data to the repo. 


## Evaluation

Each of the five translators will be tested automatically. Any programming errors or invalid output will result in a zero for that particular test. Note, however, that if your CSV `readcsv()` function doesn't work, your `csv*.py` scripts will not work either so make sure you get that working correctly first.


```bash
$./testdata.sh data output 
Test AAPL
   csv2html: output/AAPL.html and /tmp/csv2html-AAPL.html same
   csv2xml: output/AAPL.xml and /tmp/csv2xml-AAPL.xml same
   csv2json: output/AAPL.json and /tmp/csv2json-AAPL.json same
   xml2csv: data/AAPL.csv and /tmp/xml2csv-AAPL.csv same
   json2csv: data/AAPL.csv and /tmp/json2csv-AAPL.csv same
   xml2csv|csv2xml: output/AAPL.xml and /tmp/xml2csv-csv2xml-AAPL.xml same
   json2csv|csv2json: output/AAPL.json and /tmp/json2csv-csv2json-AAPL.json same
Test TSLA
   csv2html: output/TSLA.html and /tmp/csv2html-TSLA.html same
   csv2xml: output/TSLA.xml and /tmp/csv2xml-TSLA.xml same
   csv2json: output/TSLA.json and /tmp/csv2json-TSLA.json same
   xml2csv: data/TSLA.csv and /tmp/xml2csv-TSLA.csv same
   json2csv: data/TSLA.csv and /tmp/json2csv-TSLA.csv same
   xml2csv|csv2xml: output/TSLA.xml and /tmp/xml2csv-csv2xml-TSLA.xml same
   json2csv|csv2json: output/TSLA.json and /tmp/json2csv-csv2json-TSLA.json same
Test t
   csv2html: output/t.html and /tmp/csv2html-t.html same
   csv2xml: output/t.xml and /tmp/csv2xml-t.xml same
   csv2json: output/t.json and /tmp/csv2json-t.json same
   xml2csv: data/t.csv and /tmp/xml2csv-t.csv same
   json2csv: data/t.csv and /tmp/json2csv-t.csv same
   xml2csv|csv2xml: output/t.xml and /tmp/xml2csv-csv2xml-t.xml same
   json2csv|csv2json: output/t.json and /tmp/json2csv-csv2json-t.json same
```

To get credit for the various deliverables, all related tests must pass, as shown here.
