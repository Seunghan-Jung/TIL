# Django 시작하기

## Django 설치

`pip install django`

특정 버전으로 받기 : `pip install django==3.0.8`

## Django 프로젝트 생성

`django-admin startproject project_name`

`project_name` 이라는 이름의 프로젝트 폴더를 생성하고 그 안에 프로젝트를 만들어 준다.

만일, 프로젝트 폴더를 생성하는 것을 원치 않고 현재 디렉토리에 바로 프로젝트를 생성하고자 한다면 명령어의 마지막에 현재 경로를 뜻하는 `.`을 써주면 된다.

`django-admin startproject project_name .`

## Django 서버 시작

django 프로젝트를 생성하면 프로젝트 경로 안에 `manage.py`가 생긴다.

`python manage.py runserver`

## 애플리케이션(앱) 생성

`python manage.py startapp app_name`

`app_name`의 이름의 앱을 생성

