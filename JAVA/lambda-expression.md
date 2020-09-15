# Lambda Expression 람다 표현식

## 표현 방식

| 표현                        | 설명          | 특징    |
| --------------------------- | ------------- | ------- |
| `(p1, p2) -> {statements;}` | 기본          |         |
| `p1 -> {statements;}`       | parameter 1개 | () 생략 |
| `(p1, p2) -> statement`     | statement 1개 | {} 생략 |
| `() -> {statements;}`       | no parameter  | () 필수 |
| `p1 -> {return ...;}`       | return        |         |

## Anonymous Class 익명 클래스

인터페이스

```Java
@FunctionalInterface
public interface MyFuncIF{
    public int add(int i, int j);
}
```

구현 클래스

```java
public class MyFuncIFImpl implements MyFuncIF {
	@Override
	public int add(int i, int j) {
		return i + j;
	}
}
```

```java
public class MyFuncIFTest {
	public static void main(String[] args) {
        
        // 일반적인 방법
		{
			int a = 10, b = 20;
			MyFuncIF obj = new MyFuncIFImpl();
			int result = obj.add(a,  b);
			System.out.println(result);
		}
		
        // 익명 클래스
		{
			int a = 10, b = 10;
			MyFuncIF obj = new MyFuncIF() {
				
				@Override
				public int add(int i, int j) {
					return i + j;
				}
			};
			
			int result = obj.add(a, b);
			System.out.println(result);
		}
		
        // 람다를 이용
		{
			int a = 10, b = 20;
			MyFuncIF obj = (i, j) -> i + j;
			int result = obj.add(a, b);
			System.out.println(result);
		}
		
        // 람다를 이용한 또 다른 예
		{
			MyFunc.m((i, j) -> i + j);
			MyFunc.m((i, j) -> i);
		}
	}

}

class MyFunc{
	static void m(MyFuncIF p) {
		System.out.println(p.add(5, 3));
	}
}

```

## Comparator

```java
class Node{
    int v;
    public Node(int v){
        this.v = v;
    }
}
```

```java
List<Node> list = new ArrayList<Node>();
list.add(new Node(3));
list.add(new Node(4));
list.add(new Node(1));

Collections.sort(list, (n1, n2) -> n2.v - n1.v);

for(Node n : list){
    System.out.println(n.v);
}
```