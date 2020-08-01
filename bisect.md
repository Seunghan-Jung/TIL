# bisect 모듈

정렬된 리스트에 요소를 삽입할 때 정렬을 유지하게 도와주는 모듈

## .bisect

`bisect.bisect(sequence, item[, lo=0, hi=len(sequence)])`  

- `sequecne`: 요소를 넣을 sequential 자료구조 **(반드시 정렬되어 있어야 함)**
- `item`: 넣을 요소
- `lo`: 고려할 시작 인덱스. 기본 값 `0`
- `hi`: 고려할 마지막 인덱스. 기본 값 `len(sequence)`

`.bisect`는 두 가지로 나뉜다. 넣을 요소가 이미 리스트에 있을 때 원래 있던 요소의 왼쪽에 넣을지 오른쪽에 넣을지 정해야한다.  
`.bisect`와 `.bisect_right`는 원래 있던 요소의 오른쪽에 넣고  
`.bisect_left`는 왼쪽에 넣는다.

```python
import bisect

li = [1, 1, 2, 3, 3, 4]
print(li)

print('bisect')
for i in range(1, 4):
    print(f'{i}를 넣을 자리: {bisect.bisect(li, i)}')

print('bisect_right')
for i in range(1, 4):
    print(f'{i}를 넣을 자리: {bisect.bisect_right(li, i)}')

print('bisect_left')
for i in range(1, 4):
    print(f'{i}를 넣을 자리: {bisect.bisect_left(li, i)}')
```

```text
[1, 1, 2, 3, 3, 4]
bisect
1를 넣을 자리 : 2
2를 넣을 자리 : 3
3를 넣을 자리 : 5
bisect_right
1를 넣을 자리 : 2
2를 넣을 자리 : 3
3를 넣을 자리 : 5
bisect_left
1를 넣을 자리 : 0
2를 넣을 자리 : 2
3를 넣을 자리 : 3
```

### 다르게 생각해보기

`.bisect_left`를 다르게 생각해보면 넣을 아이템보다 크지 않은 첫 번째 요소의 인덱스를 찾는 것과 똑같다. 마찬가지로 `.bisect_right`는 넣을 아이템 보다 큰 첫 번재 요소의 인덱스를 찾는 것과 똑같다.

이것은 C++의 `lowerbound`와 `upperbound`와 역할이 똑같다.

## .insort

`bisect.insort(sequence, item[, lo=0, hi=len(sequence)])`  
`.bisect`로 찾은 자리에 해당 아이템을 넣는다.

마찬가지로 `.inosrt_left`와 `.insort_right`로 나뉘어져 있다. 하지만 실행한 결과는 같으니 무엇을 쓰든 상관 없다.
