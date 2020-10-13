# DOM

DOM (Document Object Model)

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



