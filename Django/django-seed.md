# django-seed

[참고문서](https://pypi.org/project/django-seed/)

장고에서 더미 데이터를 만드는데 사용하는 패키지

## 설치

```bash
$ pip install django-seed
```

## 설정

설치 후 반드시 settings.py의 `INSTALLED_APPS`에 등록해주어야한다.  
**여기서는 대시(`-`)가 아니라 언더스코어(`_`)임에 유의하자**

```python
INSTALLED_APPS = [
    ...,
    'django_seed',
]
```

## 사용하기

`api`라는 앱에 15개의 seed 만들기

```bash
python manage.py seed api --number=15
```

