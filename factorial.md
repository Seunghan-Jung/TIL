# Factorial

팩토리얼을 계산하는 방법
$$
n! = 1 \times 2 \times\ 3 \times \cdots \times (n - 1) \times n
$$

$$
(주의) 0! = 1
$$

## 재귀함수

```python
def factorial(n):
    if n == 0:
        return 1

    return factorial(n - 1) * n
```

## 반복문

```python
def factorial(n):
    res = 1

    for k in range(1, n + 1):
        res *= k

    return res
```

## math.factorial(n) 사용

```python
import math

print(math.factorial(n))
```
