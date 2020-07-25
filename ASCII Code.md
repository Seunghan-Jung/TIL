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



### 정수를 문자로!

**`chr()`함수를 이용**

```python
i = 65 # 아스키코드 65는 문자 'A'

ch = chr(i) 
print(type(ch)) # <class 'str'>
print(ch) # A
```



### 응용하기

**n번째 알파벳 구하기**

```python

while True:
    n  = int(input('1부터 26까지의 수를 입력해주세요 : '))
    if n >= 1 and n <= 26:
        break
    

result = chr(ord('a') + (n - 1))
print(f'{n}번째 알파벳은 {result}입니다.')
```



**주어진 알파벳이 몇번째 알파벳인지 구하기**

```python
while True:
    n = input('알파벳 소문자를 입력해주세요: ')
    if len(n) == 1:
        res = ord(n) - ord('a') + 1
        
        if res >= 1 and res <= 26:
            print(f'{n}은 {res}번째 알파벳입니다')
            break
          

```

