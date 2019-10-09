import requests
import re
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def clean_text(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub("", text)


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    article_name = soup.find_all("a", class_="post__title_link")
    for i in article_name:
        print(clean_text(str(i)))
    return article_name


def main():
    url = "https://habr.com/top/monthly/"
    return get_data(get_html(url))


if __name__ == "__main__":
    main()
