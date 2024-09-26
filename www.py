import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    """Scrape data from a given URL."""
    try:
        
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        
        
        title = soup.find('title').text if soup.find('title') else 'No title found'
        body = ' '.join([p.text for p in soup.find_all('p')])
        
        
        return {'url': url, 'title': title, 'body': body.strip()}
    except requests.exceptions.RequestException as e:
       
        return {'url': url, 'title': 'Failed to load', 'body': str(e)}


url = 'https://swiftsafe.com/'


reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')


urls = []
for link in soup.find_all('a'):
    url = link.get('href')
    if url.startswith('http'):
        urls.append(url)


with open('urls.txt', 'w') as file:
    for url in urls:
        file.write(url + '\n')

print("URLs saved to 'urls.txt'.")


for url in urls:
    data = scrape_url(url)
    print(data)
