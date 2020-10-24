# complex 복소수

## 복소수 생성

`complex([real=0[, imag=0]])`

```python
print(complex(10, 4))
print(10+4j)
print(complex('10+4j'))
```

```python
(10+4j)
(10+4j)
(10+4j)
```

### 주의

문자열로 복소수 생성시 `+` 또는 `-` 양쪽에 공백을 두지 않아야 한다. 공백이 있을 시 `ValueError` 발생

```python
complex('10 + 4j')
```

```python
Traceback (most recent call last):
  File "test.py", line 15, in <module>
    print(complex('10 + 4j'))
ValueError: complex() arg is a malformed string
```

## 실수부와 허수부

`complex` 클래스의 인스턴스 변수 `.real` 과 `.imag`은 각각 실수부와 허수부로 float 타입이다.

```python
c = 10+4j

print(c.real)
print(c.imag)
```

```python
10.0
4.0
```

## 켤레 복소수 만들기

### .conjugate()

해당 complex 객체의 켤레 복소수를 리턴한다.

```python
c = 10+4j
print(c.conjugate()) #=> (10-4j)
```
