from src.etl import fetch_html
from selectolax.parser import HTMLParser
from src.selectors import selectors

url = r"https://books.toscrape.com/"

html = fetch_html(url)

parser = HTMLParser(html)

link = r"https://books.toscrape.com/"

ol = parser.css_first(selectors.ol_tag)
lis = ol.css(selectors.li_tag)

for li in lis:
    article = li.css_first(selectors.article)
    print(f"{link}{article.css_first(selectors.image_container).attributes["href"]}")