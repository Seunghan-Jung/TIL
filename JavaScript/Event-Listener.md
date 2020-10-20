# Event Listener

- Event

  웹 페이지에서 일어나는 모든 일(사건, 이벤트)

  `click`, `submit`, `keydown`, `mouseover`, `change`, ...

- `.addEventListenr(type, callback)`

  - `type` 이벤트 종류 (문자열)
  - `callback` : 이벤트 발생 시 수행할 콜백함수, 발생한 이벤트 정보가 담긴 Event 객체를 첫 번째 파라미터로 허용한다.

## .preventDefault()

각 태그의 고유한 이벤트가 브라우저에서 동작하지 않도록 막는 메소드

