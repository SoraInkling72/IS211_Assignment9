from bs4 import BeautifulSoup
import requests

#link = https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/all/

def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

url_to_scrape = "https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/all/"
scoring_data = getHTMLdocument(url_to_scrape)

soup = BeautifulSoup(open(scoring_data),
                      "lxml")

# print(soup.prettify())

final_score = soup.ul.main.div.table.span.td
final_score.decompose()

touchdowns = soup.find_all('td')

for td in touchdowns:
    names = td.contents[0, 19]
    touchdown_score = td.get('td')
    print(names)
    print(touchdown_score)

if __name__ == "__main__":
    pass
