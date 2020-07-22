import requests
from bs4 import *

url = 'https://www.daum.net/'

response = requests.get(url).text

data = BeautifulSoup(response, 'html.parser')

select = data.select('#wrapSearch > div.slide_favorsch > ul > li > a')

print(select)

for item in select:
    print(item.text)
