# Random

JAVA에서 난수(random number)를 발생시키는 방법

## 1. Math.random() 메소드

Math 클래스는 java.lang 패키지에 있으므로 별도로 import할 필요가 없다. 그리고 random 메소드는 static 메소드이므로 Math 객체를 생성하지 않고 사용할 수 있다. 이 메소드는 현재 시간을 seed 값으로 한다.

```java
double d = Math.random();

System.out.println(d); // 0.312341421415
```

Math.random()은 0.0 이상 1.0 미만의 double 값을 반환한다.

## 2. java.util.Random 클래스

```java
import java.util.Random;

Random rand = new Random();

int N = 10;
int i = rand.nextInt(); // int 전 범위의 난수
int j = rand.nextInt(N); // 0 이상 N 미만의 난수
```
