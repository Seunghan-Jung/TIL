# css

## CSS Selector

### CSS 적용 우선순위

CSS 우선순위를 아래와 같이 그룹을 지어볼 수 있다.

- 중요도(Important)
- 우선 순위
  - 인라인 > id 선택자 > class 선택자 > 요소 선택자
- 소스 순서
  - 같은 우선 순위일 때 소스 순서가 뒤에 있는 것이 우선된다.

## CSS Display

### display

- display : inline-block
  - block과 inline 레벨 요소의 특징을 모두 갖는다.
  - inline처럼 한 줄에 표시 가능하며,
  - block처럼 width, height, margin 속성을 모두 지정할 수 있다.
- display: none
  - 해당 요소를 화면에 표시하지 않는다.

## CSS Position

CSS position 속성은 문서 상에서 요소를 배치하는 방법을 지정한다.

- static: 디폴트 값(기준 위치)
  - 기본적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될
- 아래는 좌표 프로퍼티를 사용하여 이동이 가능하다.
  - relative: static 위치를 기준으로 이동
  - absolute: 가장 가까이 있는 relative 부모 조상 요소를 기준으로 이동
  - fixed: 부모 요소와 관계 없이 브라우저를 기준으로 이동 (고정 위치)