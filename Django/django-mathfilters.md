# django-mathfilters

## 설치 및 설정

- 설치

  ```bash
  $ pip install django-mathfilters
  ```

- 설정

  settings.py의 `INSTALLED_APPS`에 `mathfileters`를 추가

  ```python
  # settings.py
  INSTALLED_APPS = [
      ...
      mathfilters,
  ]
  ```

## 사용하기

사용하고자 하는 템플릿에서 반드시 load 해주어야 한다.

```html
{% load mathfilters %}
```

- filter 종류
  - `addition` : 
  - `sub`
  - `mul`
  - `div`
  - `intdiv`
  - `abs`
  - `mod`

