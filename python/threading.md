# threading 모듈

## 스레드

파이썬은 하나의 스레드로 시작한다. 이를 메인 스레드라 한다. 메인 스레드가 실행 중 `input()` 같이 진행을 멈추고 입력을 받아야 하는 등의 blocking function을 만나면 그 함수가 실행이 끝날 때 까지 기다려야 한다.  
이때 우리는 스레드를 하나 더 만들어서 다른 함수를 병렬적으로 실행 시킬 수 있다.

## 스레드 생성 및 실행

`threading.Tread(target=function, args)`

- `function`
  - thread가 실행시킬 함수
- `args`
  - 함수로 넘길 인자들

스레드를 실행시키려면 `.start()` 인스턴스 메서드를 호출한다

```python
import threading

def fun(a + b):
    print('thread start')

    print('thread end')
    return a + b

print('main start')

thread = threading.Thread(target=fun, args=(1, 2)) # 스레드 생성
thread.start() # 스레드 실행

print('main end')
```

```python
main start
thread start
thread end
main end
```

스레드는 어떤 것이 먼저 끝날지 상황에 따라 다르다.  
그래서 계속 실행 시켜보면 아래와 같이 메인 스레드가 먼저 끝나기도 한다

```txt
main start
thread start
main end
thread end
```

## 스레드 간 변수 공유

### 전역변수를 이용

스레드들은 전역변수를 공유할 수 있다.

```python
import threading

ans = 0

def fun(a, b):
    global ans
    threading
    ans = a + b # 전역변수 값 갱신

thread = threading.Thread(target=fun, args=(1, 2))
thread.start()
print(ans)
```

```txt
3
```

그러나 서브 스레드가 전역변수 값을 갱신하기도 전에, 메인 스레드에서 `print(ans)` 문장을 실행하게 되면 0이 출력되어 의도와 다르게 나올 수 있다.

다음은 일부러 서브스레드가 메인스레드보다 늦게 끝나도록 한 코드다.

```python
import threading

ans = 0

def fun(a, b):
    global ans
    # 'Main' 스레드가 실행되는 동안 반복문에 갇힘
    while threading.Thread(name='Main').isAlive():
        pass
    ans = a + b

threading.currentThread().setName('Main') # 메인 스레드에 'Main' 이름 설정

thread = threading.Thread(target=fun, args=(1, 2))
thread.start()
print(ans)
```

```txt
0
```

이러한 상황을 막기위해 `.join` 인스턴스 메서드를 활용한다.  
`thread.join()`을 실행하면 `thread` 스레드가 종료될 때까지 대기한다.

```python
import threading

ans = 0

def fun(a, b):
    global ans

    for _ in range(100000000): # 반복문 1억번 실행
        pass
    ans = a + b

thread = threading.Thread(target=fun, args=(1, 2))
thread.start()
thread.join() # 서브 스레드가 종료될 때까지 대기
print(ans)
```

```python
3
```

## 스레드 실행 순서 제어

- `.start()` : 스레드 실행
- `.isAlive()` : 스레드가 실행 중이면 `True` 아니면 `False`
- `.join()` : 해당 스레드가 종료 될 때까지 대기

## 데몬 스레드란?

원래 서브 스레드는 메인 스레드가 종료되더라도 자신이 끝날 때까지 계속 실행된다.  
그러나 **데몬 스레드**는 <u>메인 스레드가 종료되면 자신도 즉시 종료되는 스레드</u>다.

### 데몬 스레드 만들기

`.setDaemon(daemonic: bool)` 인스턴스 메서드 이용

```python
thread.setDaemon(True)
```

다시 일반 스레드로 되돌리려면

```python
thread.setDaemon(False)
```

### 일반 스레드

```python
import threading

def fun(a, b):
    # 'Main' 스레드가 실행되는 동안 반복문에 갇힘
    while threading.Thread(name='Main').isAlive():
        pass
    print(a + b)
    print('서브 스레드 끝남')

threading.currentThread().setName('Main') # 메인 스레드에 'Main' 이름 설정

thread = threading.Thread(target=fun, args=(1, 2))
thread.start()
print('메인 스레드 끝남')
```

```python
메인 스레드 끝남
3
서브 스레드 끝남
```

### 데몬 스레드

```python
import threading

def fun(a, b):
    # 'Main' 스레드가 실행되는 동안 반복문에 갇힘
    while threading.Thread(name='Main').isAlive():
        pass
    print(a + b)
    print('서브 스레드 끝남')

threading.currentThread().setName('Main') # 메인 스레드에 'Main' 이름 설정

thread = threading.Thread(target=fun, args=(1, 2))
thread.setDaemon(True) # 데몬 스레드로 설정
thread.start()
print('메인 스레드 끝남')
```

```python
메인 스레드 끝남
```

메인 스레드가 끝난 뒤 데몬 스레드는 나머지를 실행시키지 못하고 즉시 종료된다.
