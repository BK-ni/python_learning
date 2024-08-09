import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Beauty/index1.html"
headers = {"Cookie": "over18=1"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())