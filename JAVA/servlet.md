# Servlet

- 일반 자바 프로그램과는 다르게 톰캣 같은 JSP/Servlet 컨테이너에서 싱행된다.

- 스레드 방식으로 실행된다.
  - 컨테이너의 종류에 관계없이 실행된다. (플랫폼 독립적)``

## 서블릿 매핑

- web.xml
- @WebServlet 어노테이션

2.x 버전까지는 web.xml파일이 자동으로 생성되지만 3.1 버전 부터 어노테이션을 지원하기 때문에 web.xml 파일이 자동으로 생성되지 않는다. (생성하려면 프로젝트 생성시 생성하기 체크를 해야한다)

## 요청 받기

- `.getParameter`
- `.getParameterValues`
- 

## 응답 하기

### MIMI-TYPE

서버에서 웹 브라우저로 데이터를 전송할 때는 어떤 종류의 데이터를 전송하는지 웹 브라우저에게 알려주어야 한다.(데이터 종류를 미리 알면 더 빠르게 처리가 가능)

이러한 데이터 종류들을 **MIM-TYPE**이라 한다.

- MIME-TYPE의 종류
  - HTML로 전송시 : `text/html`
  - 일반 텍스트 전송 : text/plain
  - XML 데이터로 전송 : `application/xml`
  - JSON 데이터 전송 : `application/json`
- 이러한 데이터의 종류들은 톰캣 컨테이너의 web.xml 파일에 정의되어 있다.

### 응답하기

## doHandel() 메서드

