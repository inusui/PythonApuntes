import requests
from bs4 import BeautifulSoup

req = requests.get('https://example.com')
soup = BeautifulSoup(req.text)

soup.select("title")[0].text
# Output: 'Example Domain' 
print(soup.select("title")[0].text)

