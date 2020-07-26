# String



## Raw String

웹크롤링을 통해서나 json을 파싱해서 얻은 문자열을 python String으로 바꿀 때 이스케이프 문자(`\n`, `\t` 등)가 포함되어 있는 경우가 종종 있어서 원래 의도와 다르게 문자열이 저장 되는 경우가 있다. 이럴 때 `raw_string`으로 처리하면 편리하다

```python
str1 = 'aaa\naaa'
str2 = r'aaa\naaa' 

print(str1)
# aaa
# aaa

print(str2)
# aaa\naaa => r string은 \n 
```



## str() 과 repr()



`str()`은 객체를 단순히 문자열로 표현

`repr()`은 객체를 우리 인간이 이해할 수 있는 문자열로 표현