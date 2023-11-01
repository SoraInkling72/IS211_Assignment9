from bs4 import BeautifulSoup
import requests

#link = https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions

def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

url_to_scrape = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
football_champ = getHTMLdocument(url_to_scrape)

soup = BeautifulSoup(football_champ, "lxml")

# print(soup.prettify())

superbowl_champ = soup.p.tbody.tr.td
superbowl_champ.decompose()

champs = soup.find_all('td')

for td in champs:
    Superbowl_No = td.contents[0]
    data = td.get('td')
    print(Superbowl_No)
    print(data)

if __name__ == "__main__":
    pass