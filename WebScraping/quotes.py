from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/"
page = requests.get(url).text
doc = BeautifulSoup(page,'lxml')

quotes = doc.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    tags = quote.find_all("a", class_="tag")
    tags_text = [tag.text for tag in tags]
    
    print(f"Quote : {text}")
    print(f"Author: {author}")
    print(f"Tags  : {tags_text}")
    print("#" * 50)