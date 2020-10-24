# datetime 모듈

## datetime 클래스

- 현재 날짜 및 시간

  ```python
  from datetime import datetime
  
  now = datetime.now()
  print(now) # 2020-10-24 13:00:11.234032
  ```

- 특정 날짜 및 시간

  `datetime(year:int, month:int, day:int, hour:int=..., minute:int=..., second: int=..., microsecond:in=...)`

  년(year), 월(month), 일(day) 는 필수 인자이고, 시간은 선택이다.

  시간을 입력하지 않으면 각각 0으로 초기화 된다.

  ```python
  from datetime import datetime
  
  time = datetime(1994, 3, 30) # 1994-03-30 00:00:00
  ```

- 날짜 간의 차이 계산

  datetime 클래스는 `-` 연산이 구현되어 있다. datetime 객체 끼리 `-` 연산을 하면 날짜의 차이를 계산해준다. (`timedelta` 객체로 리턴)

  ```python
  from datetime import datetime
  
  day1 = datetime(1994, 3, 30)
  day2 = datetime.now()
  
  print(day2 - day1)	# 9705 days, 17:24:56.935479
  print(day1 - day2)	# -9706 days, 6:35:03.064521
  print(type(day2 - day1))	# <class 'datetime.timedelta'>
  ```

## timedelta 클래스

- 시간의 양(?)을 나타내는 클래스

  예)

  - 1일
  - 3일 13시간
  - 10시간 10분

  `timedelta(days:float=..., seconds:float=..., microseconds:float=..., milliseconds:float=..., minutes:float=..., hours:float=..., weeks:float=...)`

  좋은 점은 소수점 까지도 지원한다.

  ```python
  from datetime import timedelta
  
  delta1 = timedelta(hours=300)
  delta2 = timedelta(days=1.7)
  delta3 = timedelta(weeks=2)
  
  print(delta1)	# 12 days, 12:00:00
  print(delta2)	# 1 day, 16:48:00
  print(delta3)	# 14 days, 0:00:00
  print(timedelta())	# 0:00:00
  ```

- timedelta를 이용해 일정 시간 후 또는 전을 계산할 수 있다.

  ```python
  now = datetime.now()
  delta = timedelta(days=10, hours=10, minutes=10)
  
  print(now)
  print(now + delta)
  print(now - delta)
  ```

  ```
  2020-10-24 17:38:49.995851
  2020-11-04 03:48:49.995851
  2020-10-14 07:28:49.995851
  ```

  

