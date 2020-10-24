# Prefix Sum (부분합)

perfix sum, 누적합, 부분합 등으로 불림

## 파이썬으로 부분합 쉽게 구하기

itertools 모듈의 `accumurate` 클래스를 이용하면 쉽게 누적합을 구할 수 있다.

```python
from itertools import accumurate

li = [1, 2, 3, 4, 5]

print(*accumurate(li)) # 1, 3, 6, 10, 15
```

### 1차원

`accumurate` 를 이용해서 누적합 리스트 psum을 구할 수 있다.

`psum[i]`를 정의하는 방식은 사람 마다 다르다

- 처음부터 i 까지의 합
- 처음부터 i - 1 까지의 합

필자는 후자를 사용하는 편이다.

```python
from itertools import accumertate

li = [1, 2, 3, 4, 5]

psum = [0] + list(accumurate(li)) # [0, 1, 3, 6, 10 15]
```

### 2차원

`accumurate`에 더해 `zip`을 이용하면 2차원 누적합도 구현할 수 있다.

1. 각 행의 누적합을 구한다

   ```python
   li = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
   li = [[0] + list(accumurate(li[r])) for r in range(len(li))]
   ```

2. 행의 누적합 리스트에서 `zip`을 이용해 각 열의 누적합을 구한다.

   ```python
   li = [[0] + list(accumurate(col)) for col in zip(*li)]
   ```

3. 마지막으로 다시 `zip`을 이용해 되돌린다.

   ```python
   li = [*zip(*li)]
   ```

4. 결과

   ```python
   [
       (0, 0, 0, 0), 
       (0, 1, 3, 6), 
       (0, 4, 10, 18), 
       (0, 9, 21, 36)
   ]
   ```

5. `zip`을 사용해서 내부가 튜플이긴 한데, `map`을 이용해서 내부도 리스트로 바꿔주면 된다.

   ```python
   li = [*map(list, li)]
   # [[0, 0, 0, 0], [0, 1, 3, 6], [0, 4, 10, 18], [0, 9, 21, 36]]
   ```

사실 2차원 부터는 for 루프로 구현하는게 더 이해하기 쉬울지도 모르겠다... `zip`이 섞이니까 헷갈릴 가능성이 높다.

- for 루프로 구현한 2차원 부분합

  ```python
  li = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
  
  psum = [[0] * 4 for _ in range(4)]
  
  for i in range(1, 4):
      row_sum = 0
      for j in range(1, 4):
          row_sum += li[i-1][j-1]
          psum[i][j] = psum[i-1][j] + row_sum
  
  print(psum)
  # [[0, 0, 0, 0], [0, 1, 3, 6], [0, 4, 10, 18], [0, 9, 21, 36]]
  ```

  

