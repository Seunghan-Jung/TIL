# requests

## .get()

`.get(url[, params])` url로 파라미터와 함께 GET 방식으로 요청을 보낸다.

```python
import requests

url = 'https://www.naver.com/'
response = requests.get(url)

print(response)       #=> 
print(type(response))
```
## 