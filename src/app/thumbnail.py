from bs4 import BeautifulSoup
import imdb
import urllib

def get_thumbnail(movie_id):
    access = imdb.IMDb()
    id = 0
    with open("links.csv") as f:
        for row in f:
            row = row.split(',')
            if row[0] == movie_id:
                id = row[1]
    movie = access.get_movie(id)

    page = urllib.request.urlopen(access.get_imdbURL(movie))
    soup = BeautifulSoup(page)
    movie_container = soup.find_all('div', class_="poster")
    a = movie_container[0].a.img['src']
    return a