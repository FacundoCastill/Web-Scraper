import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', class_='text')

        for index, quote in enumerate(quotes, 1):
            text = quote.text.strip()
            print(f"Cita {index}: {text}")
    else:
        print(f"No se pudo acceder a la página. Código: {response.status_code}")

if __name__ == "__main__":
    target_url = 'http://quotes.toscrape.com/page/1/'
    scrape_quotes(target_url)