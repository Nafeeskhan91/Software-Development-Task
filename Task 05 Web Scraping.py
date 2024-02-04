import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract quotes and authors
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')

        for quote, author in zip(quotes, authors):
            print(f"{quote.text} - {author.text}")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_quotes()
