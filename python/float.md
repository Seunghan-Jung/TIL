# float

## 실수 크기 비교

실수 연산은 근사값이기 때문에 정확하지 않아서 크기 비교가 원하던 대로 되지 않는다.

```python
a = 3.5
b = 3.2

print(a - b)
print('a - b == 0.3 :', a - b == 0.3)
```

```txt
0.2999999999999998
a - b == 0.3 : False
```

### (1) sys 모듈의 epsilon 이용

```python
import sys
abs(a - b) <= sys.float_info.epsilon
```

### (2) math 모듈의 isclose 이용 (python 3.5 이상)

```python
import math
math.isclose(a, b)
```
