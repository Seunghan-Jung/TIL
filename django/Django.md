# Django

Django v3.1

`pip list`로 확인

## 설치하기

```bash
pip install django

# 특정 버전으로 받기
pip install django==3.0.8
```

## 시작하기

`django-admin startproject first_webex`  
`first-webex` 라는 이름으로 프로젝트 생성

- `first_webex`: 프로젝트 설정 파일들이 들어 있음.
- `manage.py`: 장고 명령어를 실행하기 위한 파일

`python manage.py runserver`: 장고 서버 실행

장고 프로젝트는 application의 집합체로 동작

- 실제로 어떠한 역할을 해주는 친구가 바로 app.
- 하나의 프로젝트는 여러 개의 어플리케이션을 가질 수 있음.
  - 어플리케이션: 하나의 역할 및 기능 당ㄴ위로 쪼개진 형태.
    - 회원관리/글 작성, 수정, 삭제/데이터를 수집 분석/...
    - 어플리케이션을 이렇게 나뉘어야 한다 같은 기준은 없음
    - 작은 프로젝트라면 어플리케이션을 따로 나누지 않아도 된다.

- 애플리케이션 생성
  `python manage.py startapp [앱이름]` 생성
  - 해당 앱 이름으로 폴더가 생성됨
  - 바로 할 일
    - `settings.py`에 내가 생성한 app을 등록
    - `installed_app`에 가장 윗줄에 등록해준다.
    - `language_code = 'ko-kr'` 소문자로
    - `time_zone = 'Asia/Seoul`

MTV(MVC 패턴)

- Model: 장고에서는 Model
- View: 장고에서는 Template
- Controller: 장고에서는 View

- 3대장: 우리가
  - urls.py
  - views.py
  - templates (html들)

path('url 패턴/', 실행되어야 하는 views에 있는 함수, 해당 path의 별명)

- 많이 놓치즌 ㄴ부분: url패턴뒤에 슬러쉬

- views.py에서 해야할 일
  - 함수를 정의(첫번째 인자로 request 필수!!! 꼭!!! 필수!!)
  - return은 꼭 필요.
    - render: 주로 template과 함께 response할 때 사용되는 함수

- template에서 해야할 일
  - 폴더 명은 반드시 templates인 것을 확인

## Django Template Languague

- django emplate system에서 사용하는 built-in template system이다
- 조건 반복 치환 필터 변수 등의 기능을 제공
- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것
- 파이썬 처럼 if, for을 사용할 수 있지만 이거는 단순히 python 코드로 실행되는 것이 아닙니다.

Syntax

- variable: {{}}
- filter: {{variable|filter}}
- tags: {% tag %}

- Template Variable
  - html과 같은 template에서 views.py에서 준비한 변수를 가져다가 쓰는 방법
  - render() 세번째 인자로 `{key: value}`와 같이 딕셔너리 형태로 넘겨주면 Template에서 key를 이용하여 value를 가져올 수 있다.
    ```python
    content = {'key': value}
    return render(request, 'index.html', context)
    ```

- Variable Routing(동적 라우팅)
  - url 주소 일부를 변수 처럼 사용해서 동적인 주소를 만드는 것.
    주소 요청:https://127.0.0.1:8000/hello/문자열
    urls.py

    ```python
    path('hello/<str(type):name(저장되는 변수명)>/', views.hello)
    ```

    views.py

    ```python
    def hello(request, name(저장되는 변수명)):
      print(name)
      context = {
        'name': name,
      }
      return render(request, 'hello.html', context)
    ```

    template(hello.html)

    ```html
    <body>
    이름은 : {{ name }} <!-- context의 key 값을 사용하면 value를 출력한다. -->
    </body>
    ```

- DTL (tag와 filter)
  - 로직을 표현할 때는: `{% for %}`
  - 값을 표현 할 때는: `{{ }}`
  - 주석으로 나타내고 싶을 때는 : `{# #}` or `{% comment %}`

    ```html
    <!-- <h1> {#{ i * 2 }#}</h1> -->
    {% comment %} <h1>{{ i * 2 }}</h1> {% comment %}
    ```

  - for 태그
    - 반복을 위한 태그

      ```html
      {% for 임시변수 in iterable한 객체 %}
      {% endfor %}
      ```

    - for empty

      ```html
      {% for 임시변수 in iterable한 객체 %}
        값이 하나라도 있으면 여기가 실행
      {% empty %}
        비어있다면 출력
      {% endfor %}
      ```

    - if 태그
      - 조건을 구분하기 위해 사용

## 템플릿 시스템 설계 철학

- 장고는 템플릿 시스템이 표현을 제어하는 도구이자 표현에 관련된 로직일뿐이라고 생각한다.
- 템플릿 시스템에서는 이러한 기본 목표를 넘어서는 기능을 지원해서는 안 된다.

<<<<<<< HEAD
## Model

- DB에 데이터를 저장하고 가져오는 것
- SQL ( select * from table;)
- ORM
  - 쿼리를 python에서 object로 사용할 수 있게 해줌
- `model.py`에 모델 클래스를 정의를 해서 사용할 수 있음
  - class: 테이블명(models.Model):
    
    `title = models.CharField(max_length=100)`

    - 자주 사용하는 필드명
    - CharField/ DatetimeField / TextField / IntegerField / BooleanField / ...
    - Django 공식 문서 Model field라고 구글링
  
### DB 생성

- 클래스를 다 정의를 하면 **반드시 해야 할 일!!**
  - makemigrations
    - python manage.py makemigrations [app 이름]
    - DB에 적용하기 위한 설계도를 제작.
    - app 이름을 뒤에 적으면 해당 app에 있는 models.py의 내용만 설게도를 만듦.
- migrate
  - python manage.py migrate [app 이름]
  - 만들어진 설계도를 가지고 DB에 테이블을 생성.
  - app 이름을 적으면 해당 app에 있는 migration 파일을 db에 적용 시킴
- showmigrations
- sqlmigrate

### DB 사용

- DB api

### CharField(max_length=None)

- 길이의 제한이 있는 문자열을 넣을 때 사용
- max_length가 필수 인자
- 필드의 최대 길이, 데이터베이스와 django의 유효성 검사

### TextField()

- 글자의 수가 많을 때 사용
- `<textarea>`

### DateTimeField()

- 최초 생성 일자: `auto_now_add=True`
  - django ORM이 최초 데이터 입력시에만 현재 날짜와 시간으로 갱신
  - 테이블에 어떤 데이터를 최초로 넣을 때
- 최종 수정 일자: `auto_now=True`
  - django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신

## Migrations

### makemigrations

- 모델을 변경한 것에 기반한 새로운 마이그레이션(설계도)를 만들 때 사용
- 모델을 활성화 하기 전에 DB 설게도를 작성
- 생선된 마이그레이션 파일은 데이터베이스 스키마를 위한 버전관리 시스템이라고 생각

### migrate

- 작성된 마이그레이션 파일들 기반으로 실제 DB에 반영
- db.sqlite3라는 데이터베이스 파일에 테이블을 생성
- 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸

### sqlmigrate

- 해당 마이그레이션 파일이 sql 문으로 어떻게 해석되어서 동작할지 미리 확인하기 위한 명령어

### showmigrations

- 마이그레인션 파일들의 migrate 여부를 확인하기 위한 명령어

### Model의 중요 3단계

1. models.py: 변경사항 발생
2. makemigrations: 설계도 만들기
3. migrate: DB에 적용

## CRUD

### CREATE

데이터를 작성하는 3가지 방법

1. dd
    - `article = Article()`: 모델 클래스로부터 인스턴스 생성
    - `article.title = 'first'` :article 인스턴스로 클래스 변수에 접근해 해당 인스턴스 변수를 변경
    - `article.save()`: DB에 실제로 저장

2. 두번째
    - 클래스 인스턴스 생성 시 keword 인자를 함께 작성
    - `article = Article(title='second', content='django')`: 클래스로 인스턴스 생성 시 키워드 인자를 함께 작성
    - `article.save()`: DB에 실제로 저장

3. 세번째
    - create() 메소드를 사용하면 쿼리셋 객체를 생성하고 save하는 로직이 한번의 step으로 가능
    - `Article.objects.create(title='third', content='django!!')`

### READ

1. all()
    - Queryset return
    - 리스트는 아니지만 리스트와 거의 비슷하게 동작(조작할 수 있음)

2. get()
    - 객체가 없으면 `DoesNotExits` 에러가 발생
    - 객체가 여러개일 경우는 `MultipleObjectReturned` 에러가 발생
    - 위와 같은 특징을 가지고 있기 때문에 unique 혹은 Not Null 특징을 가지고 있으면 사용할 수 있다.

3. filter()

### UPDATE

1. 인스턴스의 변수 값을 변경
2. save() 메소드를 호출하여 DB에 반영
=======
## 템플릿 확장하기

1. base.html 생성하기
2. base.html을 settings.py에 등록하기
3. 상속하려는 템플릿에서 첫번째 줄에 {% extends 'base.html' %} 선언하기
4. {% block 블럭명 %}{% endblock %} 사이에 코드 작성하기
>>>>>>> 1018ef836f8e78fa169ad7b179ea4aa68645051d
