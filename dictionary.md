# Dictionary

key와 value 쌍을 저장하는 자료구조

key의 `해시함수`값을 이용한다

## Dictionary의 성질

### mutable

### iterable

### unordered

## 딕셔너리 생성

`{key1 : value1, key2 : value2, ...}` 형태로 생성

여기서 `key`는 `immutable`(변경 불가능)한 객체만 가능하다. 즉, mutable한 `list`나 `dictionary`는 불가능하다

반면에 `value`는 모든 객체가 가능하다

```python
d = {1:'엄마', 2:'아빠', 3:'나'}

## 빈 딕셔너리 생성 방법
empty_dict1 = {}
empty_dict2 = dict()
```

## 접근

### (1) 첨자를 이용

첨자 `[key]`를 이용해 요소에 접근한다.

```python
d = {1:'나', '응가':7, 1.1:'바보'}

print(d[1])
print(d['응가'])
print(d[1.1])
```

해당 key가 없으면 KeyError 발생

### (2) .get(key[, default])

해당 key가 없으면 `None` 반환

## Item 추가하기

### (1) 첨자 이용

첨자 `[]`를 이용해

### (2) update()를 이용

## Item 삭제하기

### (1) pop()

## Dictionary to List

### (1) key들의 리스트 만들기

#### .keys()

### (2) Value들의 리스트 만들기

#### .values()

### (3) Item들의 리스트 만들기

#### .items()

## 딕셔너리 순회하기

### (1) key를 이용

일반적으로 for문을 순회하면 `key`값을 가져온다

```python
D = {'구미' : 75, '서울' : 250, '대전' : 150, '광주' : 75}

for key in D:
    print(key, D[key])
```

위는 다음과 같은 결과다

```python
for key in D.keys():
    print(key, D[key])
```

### (2) Value만 이용
