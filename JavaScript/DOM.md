# DOM

DOM (Document Object Model)이란?



## 요소 찾기

- `document.querySelector(selector)`
  - `selector` : css 선택자
  - `selector`에 해당하는 html 요소를 찾아서 object 타입으로 반환
  - 해당하는 요소가 여러개라면 가장 첫 번째 요소를 반환
- `document.querySelectorAll(selector)`
  - `selector`에 해당하는 모든 요소를 `NodeList`로 반환
- `document.getElementById(id)`
  - `id` : 요소의 id 값
  - 해당 id의 요소는 유일하다고 가정되기 때문에 여러 요소를 반환하는 메서드는 존재하지 않음
- `document.getElementsByClassName(cls)`
  - `cls` : 클래스명 문자열
  - HTMLCollection 객체를 리턴
- `document.getElementsByTagName(tag)`
  - `tag`: 태그명 문자열
  - HTMLCollection 객체를 리턴

> ## `NodeList` VS `HTMLCollection`
>
> - HTMLCollection의 항목은 name, id 속성으로도 접근이 가능
>
> - NodeList의 항목은 인덱싱으로만 접근 가능
>
> - HTMLCollection은 DOM의 변화가 실시간으로 반영이 된다.(live)
>
> - 반면에 NodeList는 DOM의 변화가 반영되지 않는다. 정적이다. (non-live)
>
> - 문서가 만들어질 때 특별한 HTMLCollection 객체들이 만들어짐
>
>   | 속성             | 내용                            |
>   | ---------------- | ------------------------------- |
>   | document.forms   | form 태그 요소 모두             |
>   | document.images  | img 태그 요소 모두              |
>   | document.anchors | name 속성이 있는 a 태그         |
>   | document.links   | a 태그 요소 모두                |
>   | element.children | element 요소의 모든 자식 요소들 |
>
>   

## 요소 수정하기

- `HTMLElement.innerText`
  - 요소 안의 문자열
  - 하위 노드들의 `innerText`를 포함한다
  - `innerText`는 스타일링을 고려하여 보이는 내용만 출력
    - 예)`display:None`인 요소의 내용물은 출력되지 않는다
- `HTMLElement.innerHTML`
  - 요소 안의 HTML 문자열
- `HTMLElement.textContent`
  - `innerText`에 더해서 `<script>`와 `<style>`요소를 포함한 모든 요소의 내용을 포함

## 요소 생성하기

- `document.createElement(tagName)`

## 요소 추가하기

- `appendChild`
- `append`

> ### append VS appendChild
>
> | -                | append()    | appendChild()       |
> | ---------------- | ----------- | ------------------- |
> | 타입             | JS 메소드   | DOM 메소드          |
> | 파라미터         | 여러개 가능 | 1개                 |
> | 문자열 노드 추가 | 가능        | Element 노드만 가능 |
> | IE               | 미지원      | 지원                |
> | 리턴 값          | undefined   | 추가된 노드 반환    |

