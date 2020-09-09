# XML

사전에 정의된 tag가 없음

## 구조 및 문법

### Well Formed

XML이 아래의 문법들을 잘 따랐을 때 XML이 `well formed` 하다고 한다.

- 문서 시작  
    `<?xml version="1.0" encoding="UTF-8"?>`
- Root element & Tree 구조

    ```xml
    <Favorite>
      <Sports sort="field">
        <Football></Football>
      </Sports>
    </Favorite>
    ```

- 시작 종료 tag가 반드시 존재하고 일치.
- 대소문자 구별
- attribute: "" & "
- 주석: `<!-- ?-->`
- white space: 보존

### namespace

XML은 자유로운 tag의 생성이 가능하기 때문에 서로 중복되는 tag가 발생할 수 있으므로, 이 경우 namespace로 구별한다.

```xml
<root 
  xmlns:java="http://..."
  xmlns:c="http://..."
>
  <java:variable></java:variable>
  <c:variable></c:variable>
</root>
```

### Valid

XML 문서가 vaild 하기 위해서는 각 tag 및 해당 tag의 유효값을 별도의 문서로 구성한 후 명시적으로 지정해 주어야 한다.

이 파일을 DTD (Document Type Definition) 이라고 한다.

XML 문서에 이 문서가 기초하는 DTD를 명시하고 문서의 모든 요소가 DTD를 만족하면 `Valid`하게 된다.

## XML 파싱

XML 문서에 적용된 tag를 구별하고 데이터를 구별하는 것

### XML Parser 라이브러리

두 가지 종류가 있다.

1. SAX : 문서를 쭉 읽으면서 tag의 발생별로 처리하는 방법
2. DOM : 문서를 다 읽고 난 후, 문서 구조 전체를 자료구조에 저장하여 탐색하면서 처리하는 **방법**

#### javax.xml 패키지

#### org.w3c 패키지