from bs4 import BeautifulSoup
import requests

#link = https://finance.yahoo.com/quote/AAPL/history?p=AAPL

def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

url_to_scrape = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
stock_data = getHTMLdocument(url_to_scrape)

soup = BeautifulSoup(open(stock_data),
                      "lxml")

# print(soup.prettify())

historic_stock = soup.span.tr
historic_stock.decompose()

stocks = soup.find_all('tr')

for tr in stocks:
    date = tr.contents[0]
    close_price = tr.get('tr')
    print(date)
    print(close_price)

if __name__ == "__main__":
    pass
