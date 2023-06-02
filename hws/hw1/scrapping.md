*All projects in this class are individual projects, not group projects.  You may not look at or discuss code with others until after you have submitted your own individual effort.*


## Goal
The objective of this assignment is to create Python functions that can extract basic HTML data from different websites. The required libraries for this task are Beautiful Soup 4, Requests, and lxml.

### 1. Extracting Most Used Datasets
Write a Python script that scrapes the website "https://catalog.data.gov/dataset?q=&sort=views_recent+desc" and retrieves a list of URLs for the top 'n' websites. If 'n' exceeds 20, you should scrape multiple pages.

To verify your code, run the following test:
`pytest test_most_used_dataset.py`

### 2. Leonard Cohen Song Information
Create a Python script that gathers information about Leonard Cohen's songs and lyrics. The script should be able to provide the following:

(a) A list of unique albums by Leonard Cohen, along with links for more information about each album. Extract this data from the website "https://www.leonardcohenfiles.com/songind.html".

(b) A unique list of songs by Leonard Cohen, extracted from the same website mentioned above.

(c) Given the name of a song, retrieve the lyrics for that specific song.

The functionality should be implemented in a file named "lyrics.py". To verify your script, run the following test:

`pytest test_lyrics.py`

This command should print a list of albums
`python lyrics.py -a`

This command should print a list of songs
`python lyrics.py -s`

Given the name of a song `-l <song name>` should pring the lyrics of the song
`python lyrics.py -l "Suzanne"

Note: I will only be testing songs present in one of the album*.html urls since the other urls have a different structure.`

