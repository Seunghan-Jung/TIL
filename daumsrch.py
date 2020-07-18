import requests
from bs4 import *

url = 'https://www.daum.net/?nil_profile=daum&nil_src=search'

response = requests.get(url).text

data = BeautifulSoup(response, 'html.parser')

select = data.select('#wrapSearch > div.slide_favorsch > ul > li > a')

for item in select:
    print(item.text)
