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

## flexbox

- 배치 방향 설정 (메인축 방향 변경)
  - flex-direction
  - flexbox는 단방향 레이아웃이기 때문
- 메인축 방향 정렬
  - justify-content
- 교차축 방향 정렬
  - align-items

- content: 여러 줄
- items: 한 줄
- self: flex item 개별 요소

- justify-content:
  - flex-start, flex-end, center, space-between, space-around, space-evenly
- align-items:
  - flex-start, flex-end, center

부모 container에 flex 선언시

1. item은 행으로 나열된다.
2. ㅇㄹㄹ

## float

- 한 요소가 정상 흐름으로 부터 빠져 텍스트 및 인라인 요소가 그 주위를 감싸는 자기 컨테이너의 좌, 우측을 따라 배치되어야 함을 지정

- clear
  - 선행 floating 요소가 또는 그 아래로 내려가야 하는지(normal flow로 돌아가는)를 지정할 때 사용되는 속성
- flex box 및 그리드 레이아웃과 같은 기술이 나오기 전에 float은 열 레이아웃을 만드는 데 사용되었다.
- mdn에서는 더 새롭고 나은 레이아웃 기술(flex, grid)이 나와서 현재 레거시한 레이아웃 기술로 분류
- 결국은 텍스트 블록 내에서 float한 이미지를 위한 역할로 돌아감.
- 그래도 네이버에서는 여전히 사용되고 있음을 확인할 수 있음.

## Flex (Flexible box module)

- flex 인터페이스 내의 아이템 간 공간 배분과 정렬 기능을 제공하기 위한 1차원 레이아웃 모델
- 즉,
  - justify: 메인 축(기본: x축)
  - align: cross 축(기본: y축)
  - content: 여러 줄
  - items: 한 줄 설정
  - self: 개별 요소 설정
- display: flex
  - **정렬하려는 부모 요소에 선언**
  - inline-flex

- flex-direction: 쌓이는 방향 설정(메인 축 결정)
  - row(기본 값): 좌 -> 우
  - row-reverse: 우 -> 좌
  - col: 위 -> 아래
  - col-reverse: 아래 -> 위

- justify-content: 메인 방향축 요소들을 어떻게 배치할지 설정
  - flex-start(기본 값): (좌 상단 부터 시작하므로) 좌측 상단 부터 차례로 배치됨.
  - flex-end: 끝나는 점 부터 배치 (아이템의 순서는 그대로 정렬만 우측)
  - center: 메인축 정중앙
  - space-between: 좌우 정렬(양 끝 아이템은 양끝에 배치하고 균등하게 아이템을 위치)
  - space-around: 아이템 좌우에 동일한 공간을 부여
  - space-evenly: 균등 정렬

- align-items: cross 축 요소를 어떻게 배치할 지 결정
  - stretch: 기본값, 공간을 아이템으로 가득 채움.
  - flex-start, flex-end, center
  - baseline: item 내부의 text 밑을 기준선으로 맞춤.

- align-self: cross 축 각 개별 아이템을 어떻게 배치할 지 결정.
  - 설정 값은 위와 동일(기본값: auto)

- order: 정렬
  - 기본 값: 0 (모든 아이템)
  - 작은 숫자일수록 앞에 배치

- flex-grow: 메인 축에서 남는 공간을 각 항목에게 분배하는 방법
  - 각 아이템에 값을 줘서 그 공간 만큼 할당(비율 X)
  - 음수는 불가능