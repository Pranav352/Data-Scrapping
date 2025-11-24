#  Scrape products data from amazon website

# Beautifulsoup4
# requests
# lxml

from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.amazon.in/Apple-Headphones-Cancellation-Transparency-Personalised/dp/B0DGJ7S59D/ref=sr_1_6?crid=1BOFR2YX05FC9&dib=eyJ2IjoiMSJ9.y08pMqaeTlUXGU64oyMGl5sraP85JHUPoalcqPVLtSt4_oUOL27_tztq9ZrRm4kTeWVlGQma05xM42VbTYQ2oCFzSYNS-EHvHwnt71udBj0EwnaDDLN1RQ1DAY8Ur23zBWyB8XFNM_4WLy3H6qPs8q6_lMgm_iOXzEm1tmpUxHOCz5SAg1JX6AvFKOYF0lq_EZoEtfL6q8FDEHHHkPpu9YI7sLBq07QkQqro12dR5Ak.-wP_ZNR1UYqMZfJ33mDTshAMbtmWKb3tyFQxmDceb60&dib_tag=se&keywords=apple%2Bairpods%2Bpro%2Bmax&nsdOptOutParam=true&qid=1758445942&sprefix=apple%2Bairpods%2Bpro%2Bm%2Caps%2C385&sr=8-6&th=1"

headers = {"user-agents": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"}

response = requests.get(url,headers=headers)

if response.status_code == 200:
    # print(response.status_code)
    html_content = response.text
else:
    print("Fatching error",response.status_code)

# print(html_content)

soup = BeautifulSoup(html_content,'lxml')

# print(soup.prettify())

product_title = soup.find("span", id="productTitle").text.strip()
product_price = soup.find("span", class_="a-price-whole").text.strip()
product_rating = soup.find("span",id="acrPopover").text.strip()
product_about = soup.find("ul", class_="a-unordered-list a-vertical a-spacing-mini").text.strip()
product_description = soup.find("div", id="productDescription").text.strip()
# product_review = soup.find("ul", id="cm-cr-dp-review-list").text.strip()

print(  product_title,"\n",
        product_price,"\n",
        product_rating,"\n",
        product_about,"\n",
        product_description,"\n",
        # product_review
        )
# find, find all

# saving the data

with open("amazon_airpod pro max.csv",mode='w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow([product_title,product_price,product_rating,product_about,product_description])
print("data saved!")

