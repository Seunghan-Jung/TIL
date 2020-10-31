# JSP

- JSP 변환 과정

  - 변환 단계 : 컨테이너가 JSP 파일을 .java 파일로 변환
  - 컴파일 단계 : .java 파일을 .class 파일로 컴파일
  - 실행 단계 : .class 파일을 실행하여 그 결과를 브라우저로 전송

  hello2.jsp는 hello2_jsp 라는 클래스로 변환된다

- JSP 페이지 구성요소

  - 디렉티브 태그
  - 스크립트 요소 : 주석문, 스크립트릿, 표현식, 선언식
  - 표현 언어 (EL)
  - 내장 객체
  - 액션 태크
  - 커스텀 태그

## 디렉티브 태그

### 페이지 디렉티브 태그

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
```

페이지 디렉티브 태그는 위 처럼 `<%@ page 속성1="값1" 속성2="값2" ... %>` 형식이다.

- 페이지 디렉티브 태그로 설정하는 여러 가지 JSP 속성

  | 속성         | 기본값       | 설명                                                         |
  | ------------ | ------------ | ------------------------------------------------------------ |
  | info         | 없음         | 페이지를 설명해주는 문자열                                   |
  | language     | "java"       |                                                              |
  | contentType  | "text/html"  |                                                              |
  | import       | 없음         | 다른 패키지의 클래스를 임포트                                |
  | session      | "true"       | HttpSessiong 객체의 사용 여부                                |
  | buffer       | "8kb"        | JSP 페이지 출력시 사용할 버퍼 크기를 지정                    |
  | autoFlush    | "true"       | JSP 페이지의 내용이 출력되기 전 버퍼가 다 채워질 경우 동작을 지정 |
  | errorPage    | "false"      | JSP 페이지 처리 도중 예외가 발생할 경우 예외 처리 담당 JSP 페이지를 지정 |
  | isErrorPage  | "false"      | 현재 JSP페이지가 예외 처리 담당 페이지인지를 지정            |
  | pageEncoding | "ISO-8859-1" | JSP 페이지에서 사용하는 문자열 인코딩을 지정                 |
  | isELIgnored  | "true"       | JSP 2.0버전에서 추가된 기능으로 EL 사용 유무를 지정          |

### 인클루드 디렉티브 태그

화면마다 공통으로 존재하는 네비게이션이나 푸터를 페이지마다 작성하지 않고 이들을 하나의 JSP로 만들고 다른 JSP에서 인크루드(포함)할 수 있도록 하는 태그

```jsp
<%@ include file="duke_image.jsp" %>
```

## JSP 스크립트 요소

- 선언문 : JSP에서 변수나 메서드를 선언할 때 사용
- 스크립트릿 : JSP에서 자바 코드를 작성할 때 사용
- 표현식 : JSP에서 변수의 값을 출력할 때 사용

### 선언문

```jsp
<%!
   String name = "듀크";
   public String getName(){ return name;}
%> 
```

### 스크립트릿

```jsp
<% String age=request.getParameter("age"); %>  
```

### 표현식

```jsp
<h1>안녕하세요 <%=name %>님!!</h1>
<h1>나이는 <%=age %>살입니다!!</h1>
<h1>키는 <%=180 %>cm입니다!!</h1>
<h1>나이+10은 <%=Integer.parseInt(age)+10 %>살입니다!!</h1>
```

### 주석

```jsp
<%-- <h1>안녕하세요 <%=name %>님!!</h1>
   <h1>나이는 <%=age %>살입니다!!</h1>
   <h1>키는 <%=180 %>cm입니다!!</h1>
   <h1>나이+10은 <%=Integer.parseInt(age)+10 %>살입니다!!</h1> --%>
```

## 내장 객체

- .jsp 가 변환된 .java 파일에 선언되어 있는 내장 객체들

```java
final javax.servlet.jsp.PageContext pageContext;
javax.servlet.http.HttpSession session = null;
final javax.servlet.ServletContext application;
final javax.servlet.ServletConfig config;
```

- JSP에서 제공하는 내장 객체들

  | 내장 객체   | 서블릿 타입                            | 설명                                |
  | ----------- | -------------------------------------- | ----------------------------------- |
  | request     | javax.servlet.http.HttpServletRequest  |                                     |
  | response    | javax.servlet.http.HttpServletResponse |                                     |
  | out         | javax.servlet.jsp.JspWriter            |                                     |
  | session     | javax.servlet.http.HttpSession         |                                     |
  | application | javax.servlet.ServletContext           |                                     |
  | pageContext | javax.servlet.jsp.PageContext          | JSP 페이지에 대한 정보를 저장       |
  | page        | java.lang.Object                       | JSP 페이지의 서블릿 인스턴스를 저장 |
  | config      | javax.servlet.ServletConfig            | JSP 페이지에 대한 설정 정보를 저장  |
  | exception   | java.lang.Exception                    | 예외 발생 시 예외 처리              |

- request 내장 객체 이용하기

  ```jsp
  <%
  	request.setAttribute("name", "홍길동");
  	request.setAttribute("address", "서울시 강남구");
  %>
  ```

- session 내장 객체 이용하기

  ```jsp
  <%
  	String name = (String)session.getAttribute("name");
  	session.setAttribute("address", "서울시 강남구");
  %>
  ```

- application 내장 객체 이용하기

  ```jsp
  <%
  	String name = (String)application.getAttribute("name");
  	application.setAttribute("address", "서울시 강남구");
  %>
  ```

  

