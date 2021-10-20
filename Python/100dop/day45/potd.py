"""
this doesn't work even when same as solution from udemy
"""

from bs4 import BeautifulSoup
import lxml
from urllib import request


def get_page(url: str):
    page = request.urlopen(url)
    page = page.read().decode("utf-8")
    return page


def scrape(page_content: str):
    soup = BeautifulSoup(page_content, "lxml")
    found_movies = soup.find_all(name="h3", class_="jsx-4245974604")
    print(found_movies)
    return found_movies


def create_file(found_movies):
    with open("my_movies.txt", "w+") as file:
        for found_movie in found_movies[:-1]:
            text = found_movie.getText()
            print(text)
            file.write(text)


if __name__ == "__main__":
    create_file(scrape(get_page("https://www.empireonline.com/movies/features/best-movies-2/")))