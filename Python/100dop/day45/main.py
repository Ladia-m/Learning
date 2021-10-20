from bs4 import BeautifulSoup
import lxml
from urllib import request

######################################################
with open('website.html', 'r') as web_page:
    contents = web_page.read()

soup_1 = BeautifulSoup(contents, 'lxml')

anchor_tags = soup_1.findAll(name="a")
for tag in anchor_tags:
    print(tag.getText())

######################################################
html = """    <form method="get" action="/search/">
     <input type="text" name="q" maxlength="255" value=""></input>
    </form> """
soup2 = BeautifulSoup(html, 'lxml')

form_tag = soup2.find("input")
print(form_tag.get("maxlength"))

######################################################
page = request.urlopen("https://news.ycombinator.com/")
html_bytes = page.read()
yc_webpage = html_bytes.decode("utf-8")

soup = BeautifulSoup(yc_webpage, 'lxml')
article_tag = soup.find(name="a", class_="titlelink")
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").getText()
print(article_text, article_link, article_upvote)

