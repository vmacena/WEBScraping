from bs4 import BeautifulSoup
import requests 

#Read link
r = requests.get("google.com")

html = r.text

soup = BeautifulSoup(html, "html.parser")
print(soup)

#Answer and write 
soup.prettify()

soup.title

soup.title.name

soup.find_all("ranking-data-load")

soup.find_all("div", class_="row ind")

soup.find_all("div", class_="td-wrap")