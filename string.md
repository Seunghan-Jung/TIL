# String

**immutable**, **ordered**, **iterable**

## 문자열 관련 메소드 보기

`dir('string')`

## 문자열 대체하기

### .replace()

`string.replace(old, new [, count])`

```python
dd
```

## 문자열 벗기기

### .strip()

| strip   | rstrip    | lstrip  |
| ------- | --------- | ------- |
| 양쪽 다 | 오른쪽 만 | 왼쪽 만 |

## String to List

### split()

`split(char=' ')` 문자 char를 기준으로 문자열을 쪼개어 리스트로 반환

```python
'1 2 3 4 5'.split() => [1, 2, 3, 4, 5]
```

## List to String

### str()

```python
str([1, 2, 3, 4]) #=> '[1, 2, 3, 4]'
```

### join()

```python
' '.join([1, 2, 3, 4]) #=> '1 2 3 4'
```

## 대소문자 변경

### capitalize()

```python
'i am a boy'.capitalize() #=> 'I am a boy'
```

### title()

```python
'i am in the house'.title() #=> 'I Am A Boy'
```

### upper()

```python
'i am a boy'.upper() #=> 'I AM A BOY'
```

### lower()

```python
'I Am A Boy'.lower() #=> 'i am a boy'
```

### swapcase()

```python
'I am a Boy'.swapcase() #=> 'i AM A bOY'
```

## 문자열 검증

### istitle()

### isalpha()

### isspace()

### isupper() / islower()

### isdecimal()

순수 int로 형 변환이 가능한 문자열?

### isdigit()

윗 첨자도 숫자로 인식

### isnumeric()

분수의 특수 기호, 특수 로마자도 숫자로 인식

> **주의**
>
> 해당 decimal, digit, numeric은 float 형태의 문자열은 false로 반환

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