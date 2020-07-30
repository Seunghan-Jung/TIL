# map

`map(function, iterable)`

각 요소를  `function` 값으로 변경한다

`map object`로 반환하므로 list로 형변환 해야 한다.

```python
def square(num):
    return num ** 2

numbers = [1, 2, 3, 4]
double_li = list(map(square, numbers))

print(double_li) #=> [1, 4, 9, 16]
```



```python
INPUT = '1 2 3 4 5'
numbers = INPUT.split()
new_numbers = (map(int, numbers))

```



# filter

`filter(function, iterable)`

리턴 값이 `true`인 요소들만 뽑아준다. 

`filter object`로 반환하므로 list로 형변환 해야 한다.



```python
def ispositive(num):
    if num > 0:
        return True
    else:
        return False

numbers = [1, 2, -4, 3, -9, 11.1, -0.3]
positive_numbers = list(filter(ispositive, numbers))

print(positive_numbers)
```



# zip(*iterable)

복수의 iterable한 객체들의 각 요소들을 tuple 쌍으로 묶어 준다.

```python
girls = ['jane', 'john', 'kane', 'june']
boys = ['justin', 'david', 'kim']

couple = list(zip(girls, boys))
print(couple) #=> [('jane', 'justin'), ('john', 'david'), ('kane', 'kim')]
```

만일 인자로 들어온 iterable 객체들의 길이가 다르면 **짧은 객체를 기준으로** 묶어준다.



### 만약 긴 것을 기준으로 묶고 싶다면?

`itertools` 내장 모듈의 `zip_longest` 함수를 사용하면 긴 것을 기준으로 합쳐준다.



