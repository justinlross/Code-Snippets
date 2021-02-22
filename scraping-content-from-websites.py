import glob

from bs4 import BeautifulSoup
import requests

requestVar = requests.get('https://www.google.com/') # scrape the content of Google

print(requestVar.text)