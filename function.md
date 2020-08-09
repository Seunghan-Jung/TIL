# 함수

## 일급 객체

- 일급객체가 될 조건
  - 변수나 데이터 구조 안에 담을 수 있다
  - 매개변수로 전달이 가능하다
  - 리턴값으로 사용될 수 있다

### 파이썬의 함수는 일급 객체이다

```python
def add_two(a, b):
    return a + b

def calculate(func, arg1, arg2):
    print('calculation:', func.__name__)
    print('result:', func(arg1, arg2))

calculate(add_two, 4, 10)
```

```python
calculation: add_two
result: 14
```

## 내장함수 목록 보기

`print(dir(__builtins__))`

```txt
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__IPYTHON__', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'display', 'divmod', 'enumerate', 'eval', 'exec', 'filter', 'float', 'format', 'frozenset', 'get_ipython', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```

## 함수의 기본 문법

```python
def 함수명(parameter1, parameter2):
    코드블럭
    return value
```

`return value`가 없다면 `None`을 리턴한다

## 함수의 입력과 인자

### 위치 인자

인자들의 순서에 따라 매개변수에 매칭 시킨다.

```python
def substract(a, b):
    return a - b

substract(10, 7) #=> 3
```

### 기본값 인자(default argument)

`param=기본값` 형태로 정의하여, 해당 인자에 값을 넘겨주지 않으면 기본값을 이용하게 된다

```python
def greeting(name='익명'):
    print('{}, 안녕'.format(name))
greeting('승한')
greeting() # 인자를 넘겨주지 않으면 기본 값 '익명'을 이용한다
```

```txt
승한, 안녕
익명, 안녕
```

기본 값이 있는 인자는 맨 뒤에 있어야 한다.

```python
def greeting(name='익명', age):
    print('나이 : %d, 이름 : %s'%(age, name))

greeting(10)
```

그렇지 않으면 아래와 같이 문법 오류가 난다

```txt
File "<ipython-input-45-fdba0f5df84b>", line 1
  def greeting(name='익명', age)
                                ^
SyntaxError: invalid syntax
```

### 키워드 인자

직접 변수의 이름으로 특정 인자를 전달

```python
def greeting(age, name='익명'):
    안녕
print('나이 : %d, 이름 : %s'%(age, name))

greeting(10, '승한') # 위치 인자 방식
greeting(name='승한', age=10) # 키워드 인자 방식
```

```txt
나이 : 10, 이름 : 승한
나이 : 10, 이름 : 승한
```

### 정해지지 않은 여러 개의 인자 처리

예) print 내장 함수
`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`
`*objects`에 여러 개의 인자가 들어갈 수 있다

```python
print('가', '나', '다', '라', '마', end='.', sep='|')
```

```txt
가|나|다|라|마.
```

### 인자 위치 정리

#### 함수 정의할 때

##### 1. 위치 인자는 기본값 있는 인자보다 앞에 있어야 한다

가능한 경우

`def fun(a, b, c=3):`

불가능한 경우

`def fun(a=1, b, c):`

`def fun(a, b=1, c, d=5):`

##### 2. 가변키워드인자는 무조건 맨 뒤에 있어야 한다

가능한 경우

`def fun(a, b, c=3, **kwargs)`

불가능한 경우

`def fun(a, b, **kwargs, c=3)`

##### 3. 가변 인자는 가변키워드보다 앞이면 어디든 올 수 있다.

즉, `2`번 조건만 만족하면 가변인자 위치는 신경 쓸 필요 없다.

**가능한 경우**

`def fun(*args, a, b):`

`def fun(a, *args, b):`

`def fun(a, b, *args):`

`def fun(a, b=1, *args):`

`def fun(a, b, *args, c=1)`

`def fun(a, b=1, *args, c=1)`

`def fun(a, *args, b=1, **kwargs)`

**불가능한 경우**

`def fun(a, b, **kwargs, *args)`

#### 함수 호출할 때 

##### 1. 위치 인자가 앞 키워드 인자가 뒤

가능한 경우

`fun(1, 2, a=3)`

`fun(1, 2, a=3, b=7)`

불가능한 경우

`fun(a=3, 1)`

`fun(a=3, 1, b=2)`
