import requests
from bs4 import BeautifulSoup

page = requests.get('https://twitter.com/bod_republic')
soup = BeautifulSoup(page.text, "lxml")

tweets = []
for data in soup.find_all("article", class_="css-1dbjc4n r-1loqt21 r-18u37iz r-1ny4l3l r-1udh08x r-1qhn6m8 r-i023vh r-o7ynqc r-6416eg"):
    post_tweet = data.span
    print(post_tweet)