import requests #help us to get the url directed
from bs4 import BeautifulSoup #it will help to feach data from the URL

URL = "https://www.amazon.in/Bose-Comfort-Wireless-Headphone-Silver/dp/B0756GB78C"
#product URL

headers = {"user-Agents" : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'}

#product Title

page = requests.get(URL,headers = headers)
soup = BeautifulSoup(page.content , 'html.parser')

title = soup.find(class_ = "a-size-large product-title-word-break")

print(title)
