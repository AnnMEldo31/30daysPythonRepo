import requests
from bs4 import BeautifulSoup

price_selector = ".price_color"
title_selector = ".product_pod h3 a"
rating_selector = ".star-rating"

rating_mappings = {
    "One":      "★",
    "Two":      "★ ★",
    "Three":    "★ ★ ★",
    "Four":     "★ ★ ★ ★",
    "Five":     "★ ★ ★ ★ ★"
}


def get_rating(tag):
    for term, stars in rating_mappings.items():
        if term in tag['class']:
            return stars


data = requests.get("http://books.toscrape.com/").content
soup = BeautifulSoup(data, "html.parser")

prices = soup.select(price_selector)
titles = soup.select(title_selector)
ratings = soup.select(rating_selector)

with open("books.csv", "w", encoding="utf-8") as book_file:
    for price, title, rating in zip(prices, titles, ratings):
        book_file.write(f"{title['title']},{price.string},{get_rating(rating)}\n")
