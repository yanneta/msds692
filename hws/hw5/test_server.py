# BUG needs else clause if !=
"""
Given an IP address or machine name, pull in the list of articles
from the root / URL.  Collect the list of links and compare to the
known title/URLs.  Pull in a sample of article pages and compare
the recommended article title/URLs.
"""
import sys
from bs4 import BeautifulSoup
import requests
import pickle

artlist = {
        "business/025.txt": ['299.txt', '083.txt', '192.txt', '391.txt', '358.txt'],
        "business/131.txt": ['332.txt', '077.txt', '314.txt', '318.txt', '324.txt'],
        "business/223.txt": ['341.txt', '367.txt', '062.txt', '119.txt', '021.txt'],
        "entertainment/157.txt": ['159.txt', '143.txt', '240.txt', '162.txt', '250.txt'],
        "entertainment/153.txt": ['264.txt', '286.txt', '251.txt', '125.txt', '243.txt'],
        "politics/242.txt": ['002.txt', '233.txt', '116.txt', '315.txt', '049.txt'],
        "sport/103.txt": ['111.txt', '104.txt', '246.txt', '178.txt', '278.txt'],
        "sport/364.txt": ['403.txt', '395.txt', '354.txt', '371.txt', '368.txt'],
        "tech/384.txt": ['074.txt', '342.txt', '252.txt', '437.txt', '242.txt'],
        }

expected_counts = {'business': 510, 'entertainment': 386, 'politics': 417, 'sport': 511, 'tech': 401}

agent = {'User-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}

def fetch_article_list():
    host = getIP()
    r = requests.get("http://"+host, headers=agent)
    links = []
    soup = BeautifulSoup(r.text, "lxml")
    for link in soup.findAll('a'):
        links.append( (link.get('href').strip(), link.text.strip()) )
    return links


def fetch_sample_articles(artlist):
    host = getIP()
    articles = []
    for url in artlist:
        r = requests.get("http://"+host+"/article/"+url, headers=agent)
        soup = BeautifulSoup(r.text, "lxml")
        links = []
        for link in soup.findAll('a'):
            links.append((link.get('href').strip(), link.text.strip()))
        articles.append( (url.strip(), links) )
    return articles


def get_topic_counts(links):
    topics = {}
    for a in links:
        topic = a[0].split("/")[-2]
        topics[topic] = topics.get(topic, 0) + 1
    return topics


def test_sample_articles():
    recommended = fetch_sample_articles(artlist)
    for i in range(len(recommended)):
        art, links = recommended[i]
        assert artlist[art] == [l[0].split("/")[-1] for l in links]
    print("Recommended articles OK")


def test_links():
    links = fetch_article_list()
    assert len(links) == 2225
    counts = get_topic_counts(links)
    for topic in counts:
        assert counts[topic] == expected_counts[topic]
    print("Article links OK")

def getIP():
    with open("IP.txt") as f:
        host = f.read().strip()
        if ':' not in host:
            host += ':5000'
    return host
