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
    apple_stock_url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
    historic_data = download(apple_stock_url

    soup = BeautifulSoup(historic_data, features="lxml")

    stock_data = soup.find_all('table', class_="W(100%) M(0)")

    #This line read the rows, if the bracket with a number is present, it indicates the row to mark, and the colon determines the cells to ignore, before or after#
    rows = stock_data[0].find_all('tr')

    # This selects the headers
    headers = stock_data[0].find_all('th')

    print(
        f"{headers[0].text.strip()} - {headers[1].text.strip()} - "
        f"{headers[2].text.strip()} - {headers[3].text.strip()} - {headers[4].text.strip()} - "
        f"{headers[5].text.strip()} - {headers[6].text.strip()}")

    for row in rows:
        cells = row.find_all('td')
        if not cells:
            continue
        print(
            f"{cells[0].text.strip():<15} - {cells[1].text.strip():<25} - "
            f"{cells[2].text.strip():<15} - {cells[3].text.strip():<15} - "
            f"{cells[4].text.strip():<15} - {cells[5].text.strip():<15} - "
            f"{cells[6].text.strip():<15}")
