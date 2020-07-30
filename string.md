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

#### 주의

해당 decimal, digit, numeric은 float 형태의 문자열은 false로 반환

## Raw String

웹크롤링을 통해서나 json을 파싱해서 얻은 문자열을 python String으로 바꿀 때 이스케이프 문자(`\n`, `\t` 등)가 포함되어 있는 경우가 종종 있어서 원래 의도와 다르게 문자열이 저장 되는 경우가 있다. 이럴 때 `raw_string`으로 처리하면 편리하다

```py
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

## 아스키(ASCII) 코드

| 10진수 | Symbol | 10진수 | Symbol | 10진수 | Symbol | 10진수 | Symbol |
| :----: | :----: | ------ | :----: | :----: | :----: | :----: | :----: |
|   65   |   A    |        |   N    |   97   |   a    |        |   n    |
|   66   |   B    |        |   O    |        |   b    |        |   o    |
|   67   |   C    |        |   P    |        |   c    |        |   p    |
|   68   |   D    |        |   Q    |        |   d    |        |   q    |
|   69   |   E    |        |   R    |        |   e    |        |   r    |
|   70   |   F    |        |   S    |        |   f    |        |   s    |
|   71   |   G    |        |   T    |        |   g    |  116   |   t    |
|   72   |   H    |        |   U    |        |   h    |        |   u    |
|   73   |   I    |        |   V    |        |   i    |        |   v    |
|   74   |   J    |        |   W    |        |   j    |        |   w    |
|   75   |   K    |        |   X    |        |   k    |        |   x    |
|   76   |   L    |        |   Y    |        |   l    |        |   y    |
|   77   |   M    | 90     |   Z    |        |   m    |        |   z    |

### 문자를  정수로

**`ord()`함수를 이용**

```python
ch = 't' # 't'는 아스키 코드 116

# i = int(ch) # Error! : int() 함수는 't'를 정수로 바꿀 수 없다!
i = ord(ch)

print(type(i)) # <class 'int'>
print(i) # 116
```

### 정수를 문자로

**`chr()`함수를 이용**

```python
i = 65 # 아스키코드 65는 문자 'A'

ch = chr(i)
print(type(ch)) # <class 'str'>
print(ch) # A
```

### 응용하기

#### n번째 알파벳 구하기

```python
while True:
    n  = int(input('1부터 26까지의 수를 입력해주세요 : '))
    if n >= 1 and n <= 26:
        break

result = chr(ord('a') + (n - 1))
print(f'{n}번째 알파벳은 {result}입니다.')
```

#### 주어진 알파벳이 몇 번째 알파벳인지 구하기

```python
while True:
    n = input('알파벳 소문자를 입력해주세요: ')
    if len(n) == 1:
        res = ord(n) - ord('a') + 1

        if res >= 1 and res <= 26:
            print(f'{n}은 {res}번째 알파벳입니다')
            break

```

### 더 알아보기

#### 이스케이프 문자로 아스키 코드 문자 출력하기

| 10진수(Dec) | 16진수(Hex) | 8진수(Oct) | 문자 |
| :---------: | :---------: | :--------: | :--: |
|     65      |     41      |    101     |  A   |
|             |             |            |      |
|             |             |            |      |
|             |             |            |      |
|             |             |            |      |
|             |             |            |      |
|             |             |            |      |
|             |             |            |      |
|             |             |            |      |
|             |             |            |      |
|             |             |            |      |
|             |             |            |      |
|             |             |            |      |

`\x(16진수)`  또는 `\(8진수)`로 문자를 표현할 수 있다.

```python
print('\x41') # A
print('\101') # A
```
