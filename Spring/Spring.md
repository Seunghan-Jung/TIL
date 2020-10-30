# Spring

## SpringFramework 등장배경

- 1/5
  - EJB를 사용하면 애플리케이션 작성을 쉽게 할 수 있다.
  - Low Level의 트랜잭션이나 상태관리, 멀티쓰레딩, 리소스 풀링과 같은 복잡한 Low Level의 API 따위를 이해하지 못하더라도 아무 문제없이 애플리케이션을 개발할 수 있다.
- ㅇ
  - EJB 현실에서의 반영은 어렵다
    - 코드 수정 후 반영하는 과정 자체가 거창해 기능은 좋지만 복잡한 스펙으로 인한 **개발의 효율성이 떨어짐**
    - 어플리케이션을 테스트하기 위해서는 반드시 EJB 서버가 필요하다
    - Entity Bean / Session Bean / Message-Driven Bean
- d
  - 웹사이트가 점점 커지면서 엔터프라이즈급의 서비스가 필요
    - 세션빈에서 Transaction 거ㅘㄴ리가 용이
    - 로긴, 분산처리, 보안 등
  - 자바 진영에서는 EJB가 엔터프라이즈 급 서비스로 각광을 받게 됨
    - EJB스펙에 정의된 인터페이스에 따라 코드를 작성하므로 기존에 작성되 POJO를 변경해야 함
    - 컨테이너에 배포를 해야 테스트가 가능해 개발 속도가 저하된
    - 배우기 어렵고, 설정해야 할 부분이 많음
    - EJB는 RMI를 기반으로 하는 서버이므로 무거운 Container
  - Rod Johnson이 'Expert One-on-One J2EE Development without EJB'라는 저서에서 EJB를 사용하지 않고 엔터프라이즈 애플리케이션을 개발하는 방법을 소개함(**스프링의 모태**)
    - AOP나 DI같은 새로운 프로그래밍 방법론으로 가능
    - POJO를 전언적인 프로그래밍 모델이 가능해짐
- 4/5
  - 점차 POJO + 경량 프레임워크를 사용하기 시작
  - POJO
    - 특정 프레임워크나 기술에 의존적이지 않은 자바 객체
    - 특정 기술에 종속적이지 않기 때문에 생산성, 이식성 향상
    - Plain : componenet interface를 상속받지 않는 특징 (특정 프레임워크에 종속되지 않는)
    - Old : EJB 이전의 Java Class를 의미
  - 경량 프레임워크
    - EJB가 제공하는 서비스를 지원해 줄 수 있는 프레임워크 등장
    - Hibernate, JDO, iBatis(MyBatis), Spring
- 5/5
  - POJO + framework
    - EJB서버와 같은 거창한 컨테이너가 필요 없다
    - 오픈소스 프레임워크라 사용이 무료
    - 각종 기업용 어플리케이션 개발에 필요한 상당히 많은 라이브러리가 지원.
    - 스프링 프레임워크는 모든 플랫폼에서 가능하다
    - 스프링은 웹 분야 뿐만이 아니라 어플리케이션 등 모든 분야에 적용이 가능한 다양한 라이브러리가 있다.

## Spring Framework

### IoC & Controller

DL (dependency lookup)

