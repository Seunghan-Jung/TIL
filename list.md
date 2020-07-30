# List

## List의 기본 특성

### iterable

### mutable

### ordered

## List 생성

### 첨자([]) 이용

```python
li = [1, 2, 3, 4]
```

#### list() 내장함수 이용

```python
li = list('1234')
print(li) #=> ['1', '2', '3', '4']
```

### List Comprehension

`[표현식 for 변수 in iterable (if 조건식)]`

`list(표현식 for 변수 in iterable (if 조건식))`

iterable 객체에서 조건식을 만족하는 요소만 사용한다.

## List에 요소 추가하기

### 더하기

### .append()

### .extend()

### .insert()

## List에서 요소 삭제하기

### 1. 원하는 요소 지우기

#### (1) .remove()

지우려는 값이 없으면 에러 발생

### 2. 가장 뒤에 있는 요소 지우기

#### (1) .pop()

### 3. 모두 지우기

#### (1) .clear()

## List에서 요소 찾기

### .index(x)

## List 정렬하기

### .sort()

```python
li = [3, 4, 1, 2]
sort(li)
print(li) #=> [1, 2, 3, 4]
```

### sorted() 내장함수

## List 뒤집기

### .reverse()

```python

```

### reversed() 내장함수

## List 복사하기

List는 일반적으로 참조형식이다

```python
A = [1, 2, 3, 4]
B = A

A[0] = 8
print(A) #=> [8, 2, 3, 4]
print(B) #=> [8, 2, 3, 4]
```

### (1) list() 함수 이용

```python
A = [1, 2, 3, 4]
B = list(A)


```

### (2) 슬라이싱 이용

```python
A = [1, 2, 3, 4, 5]
B = A[:]

A[0] = 8

print(A, B) #=> [8, 2, 3, 4, 5] [1, 2, 3, 4, 5]
```

#### 슬라이싱의 한계

중첩 리스트인 경우 안에 있는 리스트까지는 복사해오지 못한다

```python
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = A[:]

A[0][0] = 8

print(A) #=> [[8, 2, 3], [4, 5, 6], [7, 8, 9]]
print(B) #=> [[8, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### (3) copy 모듈 이용

#### - 얕은 복사

```python
import copy

A = [[1, 2], [3, 4]]
B = copy.copy(A)

A[0][0] = 8

print(A)
print(B)
```

#### - 깊은 복사

```python
import copy

A = [[1, 2], [3, 4]]
B = copy.deepcopy(A)

A[0][0] = 8

print(A)
print(B)
```
