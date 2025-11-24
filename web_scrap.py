#  Scrape products data from apple  website

# Beautifulsoup4
# requests
# lxml

from bs4 import BeautifulSoup
# import requests
import csv

html_path = '/Users/pranavpatel/Desktop/Data Scrap/apple store/apple_store.html'

with open(html_path, 'r') as html_file:
    html_content = html_file.read()

# print(html_content)

soup = BeautifulSoup(html_content, 'html.parser')

header = soup.find("h1").text

# menus = soup.find_all('a')
# for menu in menus:
#     print(menu.text)

# menus = soup.find_all('a',href=True)
# for menu in menus:
#     print(menu['href'])

print(soup.find('h3').text)


print(header)


