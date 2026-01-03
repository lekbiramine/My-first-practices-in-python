from bs4 import BeautifulSoup
import requests
import csv
from urllib.parse import urljoin
import time

# The structure :
# 1 - we select the tr (data-offset = "x")
# 2 - we select the :
# * company 
# * position 
# * location 
# * tags
# * date_posted
# * job_url
# 3 - we iterate over the table rows by x (data-offset)
# 4 - we handle the missing fields safely 

# base_url = "https://remoteok.com/"
# current_url = base_url
# page = requests.get(current_url).text
# time.sleep(1)
# doc = BeautifulSoup(page, 'lxml')

# table = doc.find("table", id="jobsboard")
# rows = table.find_all("tr")[1:]
# print(rows)

# with open("jobs.csv", "w", newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(["company","position","location","tags","date_posted","job_url"])
    # while True:
    #     page = requests.get(current_url).text

# couldn't scrape it .