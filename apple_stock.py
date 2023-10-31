from bs4 import BeautifulSoup
import requests

#link = https://finance.yahoo.com/quote/AAPL/history?p=AAPL

def download(url):
    """
    Reads data from a URL and returns data as string

    :param url:
    :return:
    """
    return requests.get(url).text

# print(soup.prettify())


if __name__ == "__main__":
    apple_stock_url = " https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
    historic_data = download(apple_stock_url)

    soup = BeautifulSoup(open(historic_data), features="lxml")

    stock_data = soup.find_all('table', class_ = "W(100%) M(0)")

    print(stock_data)