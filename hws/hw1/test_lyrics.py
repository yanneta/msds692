from lyrics import *
from bs4 import BeautifulSoup

expected_albums_top_10 = [
       'Cohen Live', 'Dear Heather', "Death Of A Ladies' Man",
       'Field Commander Cohen', "I'm Your Man", 'Live In Fredericton',
       'Live Songs', 'Live at the Isle of Wight', 'Live in Dublin',
       'Live in Fredericton']

expected_song_test = [
        'Samson In New Orleans', 'Sisters Of Mercy',
        'Stories Of The Street', 'Take This Longing',
        "That Don't Make It Junk", 'The Goal',
        'The Land Of Plenty', 'The Old Revolution',
        'The Window', 'Tower Of Song','True Love Leaves No Traces',
        'Whither Thou Goest']

test_row = """<tr valign="bottom">
      <td align="left"> 
      Ain't No Cure For Love </td>
      <td align="left">
      <a href="album9.html" style="text-decoration:none">I'm Your Man (L)</a> </td>
      </tr>
      """

def test_process_row():
    row = BeautifulSoup(test_row, "lxml")
    song, album, link = process_row(row)
    assert song == "Ain't No Cure For Love"
    assert album == "I'm Your Man"
    assert link == 'album9.html'


def test_clean_text():
    texts = ["1. Hola", "Hola.", "Hola (L)", "Hola (1790)", "Hola 1790"]
    for text in texts:
        assert clean_text(text) == "Hola"


def test_get_albums():
    albums = get_albums()
    assert len(albums) == 30
    for i in range(10):
        assert albums[i] == expected_albums_top_10[i]


def test_get_songs():
    songs = get_songs()
    assert len(songs) == 163
    j = 0
    for i in range(100, 160, 5):
        assert songs[i] == expected_song_test[j]
        j += 1


def test_scrape_lyrics_from_url():
    url = "https://www.leonardcohenfiles.com/album9.html"
    song = "Tower Of Song"
    text = scrape_lyrics_from_url(song, url)
    assert len(text.split(" ")) > 300
    url = "https://www.leonardcohenfiles.com/album1.html"
    song = "Suzanne" 
    text = scrape_lyrics_from_url(song, url)
    assert len(text.split(" ")) > 300
    url = "https://www.leonardcohenfiles.com/album2.html"
    song = "Story of Isaac"
    text = scrape_lyrics_from_url(song, url)
    assert len(text.split(" ")) > 200
