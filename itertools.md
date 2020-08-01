# itertools 모듈

## itertools.product

`itertools.product(*iterable)`

수학에서 집합의 곱, cartesian product이다. 즉, 두 집합 간의 모든 조합을 만들어 준다.

두 집합 A = {1, 2, 3}, B = {11, 12, 13} 일 때 두 집합의 카르테시안 곱은 A X B는  
A X B = {(1, 11), (1, 12), (1, 13), (2, 11), (2, 12), (2, 13), (3, 11), (3, 12), (3, 13)} 이다.

```python
import itertools

A = [1, 2, 3]
B = [11, 12, 13]

result = itertools.product(A, B)

print(result)       # 그냥 print하면 안 나옴
print(list(result)) # list로 바꿔줘야 한다
```

```txt
<itertools.product object at 0x0000025A6B47AF48>
[(1, 11), (1, 12), (1, 13), (2, 11), (2, 12), (2, 13), (3, 11), (3, 12), (3, 13)]
```

여러개도 가능하다

```python
import itertools

A = [1, 2, 3]
B = [11, 12, 13]
C = ['a', 'b', 'c']
result = itertools.product(A, B, C)

print(result)
print(list(result))
```

```txt
<itertools.product object at 0x000001BEF4590318>
[(1, 11, 'a'), (1, 11, 'b'), (1, 11, 'c'), (1, 12, 'a'), (1, 12, 'b'), (1, 12, 'c'), (1, 13, 'a'), (1, 13, 'b'), (1, 13, 'c'), (2, 11, 'a'), (2, 11, 'b'), (2, 11, 'c'), (2, 12, 'a'), (2, 12, 'b'), (2, 12, 'c'), (2, 13, 'a'), (2, 13, 'b'), (2, 13, 'c'), (3, 11, 'a'), (3, 11, 'b'), (3, 11, 'c'), (3, 12, 'a'), (3, 12, 'b'), (3, 12, 'c'), (3, 13, 'a'), (3, 13, 'b'), (3, 13, 'c')]
```

## itertools.combination

`itertools.combination(iterable, n)`

수학의 조합(combination)의 모든 경우를 찾아준다.

`A = {1, 2, 3}` 에서 2가지를 뽑는 경우  
`(1, 2), (1, 3), (2, 3)` => 3가지

```python
import itertools

A = [1, 2, 3]

result = itertools.combinations(A, 2)

print(result)
print(list(result))
```

```txt
<itertools.combinations object at 0x0000013E039FAF48>
[(1, 2), (1, 3), (2, 3)]
```

### itertools.combination_with_replacement

중복조합

## itertools.accumulate

```python
import itertools

A = [1, 2, 3]

result = itertools.accumulate(A, lambda a, b: a + b)

print(result)
print(list(result)) #=> [1, 3, 6]
```
