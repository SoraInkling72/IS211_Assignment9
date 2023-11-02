from bs4 import BeautifulSoup
import requests

#link = https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions

def download(url):
    """
    Reads data from a URL and returns data as string

    :param url:
    :return:
    """
    return requests.get(url).text

# print(soup.prettify())


if __name__ == "__main__":
    SBChamps_url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
    football_champs = download(SBChamps_url)

    soup = BeautifulSoup(football_champs, features="lxml")

    super_bowl_data = soup.find_all('table', class_="wikitable sortable jquery-tablesorter")

    #This line read the rows, if the bracket with a number is present, it indicates the row to mark, and the colon determines the cells to ignore, before or after#
    rows = super_bowl_data[0].find_all('tr')

    # This selects the headers
    headers = rows[0].find_all('th')

    print(
        f"{headers[0].text.strip()} - {headers[1].text.strip()} - {headers[2].text.strip()} - "
        f"{headers[3].text.strip()} - {headers[4].text.strip()} - {headers[5].text.strip()} - "
        f"{headers[6].text.strip()} - {headers[7].text.strip()} - {headers[8].text.strip()}")

    for row in rows:
        cells = row.find_all('td')
        if not cells:
            continue
        print(
            f"{cells[0].text.strip():<15} - {cells[1].text.strip():<25} - "
            f"{cells[2].text.strip():<15} - {cells[3].text.strip():<15} - "
            f"{cells[4].text.strip():<15} - {cells[5].text.strip():<15} - "
            f"{cells[6].text.strip():<15} - {cells[7].text.strip():<15} - "
            f"{cells[8].text.strip():<15}")