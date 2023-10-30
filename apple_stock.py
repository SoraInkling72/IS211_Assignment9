from bs4 import BeautifulSoup
import requests

def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

url_to_scrape = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
stock_data = getHTMLdocument(url_to_scrape)

soup = BeautifulSoup(open(stock_data),
                      "lxml")

print(soup.prettify())

if __name__ == "__main__":
    pass
