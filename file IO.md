# open 함수

```python
open(filename, mode)
```

- filename : 내가 열고 싶은 파일의 경로와 이름을 적는다.
  - mode : `r` 읽기모드, `w` 쓰기모드. 아무것도 적지 않으면 기본적으로 읽기모드로 적용된다
  - encoding: 한글 때문에 파일이 정상적으로 dict로 변환이 안된 경우 `UTF8`을 적용하여 해결했다.



# JSON

> JavaScript Object Notation

json 형식은 `json` 모듈의 `json.load()`로 읽어서 딕셔너리로 파싱 할 수 있다.

```python
import json
# json 데이터를 json.load()를 이용해 python의 딕셔너리로 변환
dict_data = json.load(json_data)
```



# EOF

EOF는 End of File 파일의 끝을 의미한다. 파0일을 읽을 때 어떻게 파일의 끝을 판단할까?

## input() 으로

`input()`함수는 파일 끝에 다다르면 `EOFError`를 발생시킨다.

```python
while True:
    try:
        s = input()
    except EOFError:
        break # 끝에 다다르면 종료
        
    print(s)
```



## sys.stdin.readline()으로

`sys.stdin.readline()`은 끝에 다다르면 빈 문자열을 리턴한다.

```python
import sys

while True:
    try:
        s = sys.stdin.readline()
        
        if not s: # 빈 문자열이면 종료
            break
            
        print(s)
```



## sys.stdin.read()

`sys.stdin.read()`함수는 파일을 내용을 모두 한 번에 읽고 문자열로 리턴해준다.

```python
import sys

s = sys.stdin.read()

print(s)
```



관련문제: [BOJ11718](https://www.acmicpc.net/problem/11718)