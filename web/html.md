# HTML

## HTML 문서의 구조

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <p>This is my page</p>
  </body>
</html>
```

1. `<!DOCTYPE html>`: 문서 형식을 나타냄
2. `<html></html>`: 
3. `<head>`: 검색 결과에 노출될 키워드, 홈페이지 설명, CSS 스타일 등
4. `<meta charset="utf-8">`: html 문서의 인코딩 설정
    - `UTF-8`: 전세계에서 사용되는 언어에 대한 대부분의 문자가 포함됩니다.
5. `<title>`: 페이지 제목이 설정되며 브라우저 탭에 표시된다.
6. `<body>`: 페이지에 표시되는 모든 콘텐츠가 포함된다.

## HTML 주석

`<!-- <p>I am!</p> -->`

## 1. 참과 거짓 속성(Boolean attributes)
  
`<input type="text">` : <input type="text">

`<input type="text" disabled>` : <input type="text" disabled>

`<input type="text" disabled="disabled">` : <input type="text" disabled>

## 2. 속성값의 따옴표

### 1) 따옴표 생략 가능

`<a href=https:www.mozilla.org/>favortie website</a>` : <a href=https:www.mozilla.org/>favortie website</a>

> 띄어쓰기가 있을 시에는 무조건 따옴표로 감싸야 한다.  
`<a href=https://www.mozilla.org/ title=The Mozilla homepage>favorite website</a>`  
<a href=https://www.mozilla.org/ title=The Mozilla homepage>favorite website</a>

  <br>

  <h3>2) 따옴표 안에 따옴표</h3>
  <xmp><a href="http://www.example.com" title="Isn't this fun?">A link to my example.</a></xmp> : <a href="http://www.example.com" title="Isn't this fun?">A link to my example.</a>
  <br>
  <xmp><a href='http://www.example.com' title='Isn&#39;t this fun?'>A link to my example.</a></xmp> : <a href='http://www.example.com' title='Isn&#39;t this fun?'>A link to my example.</a>

  <br>
  <br>
  <h4>HTML Entities</h4>
  
  <table class="table">
    <thead>
      <tr>
        <th scope="col">Literal character</th>
        <th scope="col">character reference equivalent</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>&lt;</td>
        <td><xmp>&lt;</xmp></td>
      </tr>
      <tr>
        <td>&gt;</td>
        <td><xmp>&gt;</xmp></td>
      </tr>
      <tr>
        <td>&quot;</td>
        <td><xmp>&quot;</xmp></td>
      </tr>
      <tr>
        <td>&apos;</td>
        <td><xmp>&apos;</xmp></td>
      </tr>
      <tr>
        <td><</td>
        <td><xmp>&amp;</xmp></td>
      </tr>

    </tbody>
  </table>

