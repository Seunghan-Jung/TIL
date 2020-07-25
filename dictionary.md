# Dictionary

key와 value 쌍을 저장하는 자료구조 

key의 `해시함수`값을 이용한다



## 생성

`{key1 : value1, key2 : value2, ...}` 형태로 생성



```python
d = {1:'엄마', 2:'아빠', 3:'나'}

# 빈 딕셔너리 생성 방법
empty_dict1 = {}
empty_dict2 = dict()
```



## 접근

첨자 `[]`를 이용해 요소에 접근한다.

```python
d = {1:'나', '응가':7, 1.0:'바보'}

print(d[1])
print(d['응가'])
print(d[1.0])
```



## Item 추가하기

첨자 `[]`를 이용해 