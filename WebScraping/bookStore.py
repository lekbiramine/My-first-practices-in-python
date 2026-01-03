from bs4 import BeautifulSoup
import requests
import csv
from urllib.parse import urljoin

base_url = "https://books.toscrape.com/"
current_url = base_url

with open("books.csv","w",newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title","Price","Availability"])

    while True:
        page = requests.get(current_url).text
        print(f"Scraping: {current_url}")
        doc = BeautifulSoup(page, 'lxml')

        books = doc.find_all("article", class_="product_pod")
        print(f"Found {len(books)} books")

        for book in books:
            title = book.find("h3").find("a")["title"]
            price = book.find("p", class_="price_color").text
            availability = book.find("p", class_="instock availability").text.strip()

            writer.writerow([title, price[1:], availability])

            # print(f"Title => {title}")
            # print(f"Price => {price[1:]}")
            # print(f"The book => {availability}")
            # print("#" * 50)

        # Move next page logic here, outside the for-loop
        next_btn = doc.find("li", class_="next")
        if next_btn:
            next_url = next_btn.find("a")["href"]
            current_url = urljoin(current_url, next_url)
            print(f"Next page: {current_url}")
        else:
            break
