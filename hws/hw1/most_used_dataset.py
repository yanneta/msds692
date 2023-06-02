import sys
from bs4 import BeautifulSoup
import requests


# feel free to define other functions



def list_of_pairs(n):
    """ Get first n datasets

    Output: list of (dataset title, url)
    """
    ### Your coode here

if __name__ == "__main__":
    n = int(sys.argv[1])
    pairs = list_of_pairs(n)
    for title, url in pairs:
        print(title, url)


