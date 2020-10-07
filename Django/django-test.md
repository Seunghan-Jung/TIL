# django-test

django 프로젝트를 테스트 하는 방법

django에서 앱을 생성하면, 앱을 테스트하는 코드를 짜 넣는 `tests.py` 파일이 생긴다.  
이 파일을 작성하는 방법에 대한 글이다.

자세한 내용은 MDN 문서[Django 튜토리얼 파트 10: Django 웹 어플리케이션 테스트하기](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Testing)의 내용을 참고한다.

## A. 시작하기

1. 테스트에 사용할 모델을 작성

   - accounts/models.py

     ```python
     from django.db import models
     from django.contrib.auth.models import AbstractUser
     
     
     class User(AbstractUser):
         phone = models.CharField(max_length=11)
         
         def __str__(self):
             return f'User object ({self.pk})'
     
     ```

   - todos/models.py

     ```python
     from django.db import models
     from django.conf import settings
     
     class Todo(models.Model):
         content = models.CharField(max_length=50)
         user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     ```

   - 모델을 작성한 뒤 makemigrations 해준다.

     - 단, migrate는 안 해줘도 상관 없다.
     - test 시에는 프로젝트의 DB를 사용하는 것이 아니라 임시로 사용할 DB를 만들기 때문이다.

2. tests.py 작성하기

   ```python
   from django.test import TestCase
   
   # Create your tests here.
   
   ```

   tests.py의 초기의 상태는 위와 같은 모습이다. `django.test` 모듈의 `TestCase` 클래스를 상속 받는 클래스를 만들어야 한다. 기본적인 구조는 다음과 같다.

   ```python
   class YourTestClass(TestCase):
       @classmethod
       def setUpTestData(cls):
           print("setUpTestData: Run once to set up non-modified data for all class methods.")
           pass
   
       def setUp(self):
           print("setUp: Run once for every test method to setup clean data.")
           pass
       
   	def tearDown(self):
           # Clean up run after every test method.
           pass
       
       def test_false_is_false(self):
           print("Method: test_false_is_false.")
           self.assertFalse(False)
   
       def test_false_is_true(self):
           print("Method: test_false_is_true.")
           self.assertTrue(False)
   
       def test_one_plus_one_equals_two(self):
           print("Method: test_one_plus_one_equals_two.")
           self.assertEqual(1 + 1, 2)
   ```

   - `setUpTestData()`
     - TestCase 클래스는 `test*`라는 이름으로 시작하는 멤버 함수들을 순차적으로 실행하여 테스트를 진행
     - 이때, `setUpTestData()` 클래스 메소드는 이러한 테스트 함수들을 실행하기 전에 딱 한 번 실행되는 메소드
   - `setUp()`
     - 모든 테스트 함수들이 실행 되기 전에 반드시 실행되는 함수
   - `tearDown()`
     - 모든 테스트 메소드가 끝난 후에 실행되는 함수
   - `assert*()`
     - TestCase 클래스는 `assert*`로 시작하는 멤버 함수들을 가지고 있는데 이는 개발자의 의도대로 테스트가 되는지 확인해주는 함수이다. 의도와 맞지 않다면 해당 assert 함수가 있는 테스트는 실패하게 된다.
     - `assertTrue(exp, msg)` : exp가 True인지 확인
     - `assertFalse(exp, msg)` : exp가 False인지 확인
     - `assertEqual(first, second, msg)`: first와 second가 동일(`=`)한지 확인

   위 구조를 토대로 account 앱의 test 클래스를 만들어 보자

   ```python
   class AccountTest(TestCase):
       def setUp(self):
           User.objects.create_user(username='testuser', password='password')
           pass
   
       def tearDown(self):
           pass
   ```

   

