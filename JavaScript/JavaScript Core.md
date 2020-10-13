# JS core

## 변수

### let

값을 재할당 할 수 있는 변수를 선언하는 키워드

- 한 번만 선언할 수 있으며 여러 번 할당할 수 있다.

  ```js
  let x = 1
  x = 3
  ```

- 재선언할 경우 `SyntaxError`가 발생

  ```js
  let x = 10
  let x = 7 // SyntaxError
  ```

  ```
  SyntaxError: Identifier 'x' has already been declared
  ```

  - 크롬에서는 개발자의 편의를 위해 크롬 콘솔에서는 재선언이 허용되어 있다.
  - 같은 크로미움을 쓰는 엣지, 웨일에서 또한 가능하다

### const

값이 변하지 않는 상수를 선언하는 키워드

- 선언 시 반드시 값을 할당해주어야 함

  ```js
  const v = 10
  ```

- 초기화 해주지 않을 시 `SyntaxError` 발생

  ```js
  const v
  ```

  ```
  SyntaxError: Missing initializer in const declaration
  ```

#### var

- 함수 유효 범위를 가진다

- 가급적이면 `var`를 사용하지 않는다

  - hoisting 문제

    - var로 선언된 변수는 선언 이전에 참조할 수 있는 현상

      ```js
      console.log(name)
      var name = '홍길동'
      ```

      ```
      undefined
      ```

## 타입

### Number

```js
const n = 10 			// 자연수
const k = -8			// 정수
const pi = 3.14			// 실수
const t = 2.998e8		// e 표기
const inf = Infinity	// 무한 (-Infinity 도 가능)
const z = NaN			// Not a Number
```

### Empty Value

값이 존재하지 않음을 표현하는 타입

- `undefined`

  ```js
  let a
  console.log(a)	// undefined
  ```

- `null`

  ```js
  let a = null
  console.log(a) // null
  ```

- 둘 사이의 차이

  ```js
  typeof undefined	// "undefined"
  typeof null			// "object"
  ```

### String

- 문자열을 표현하는 방법

  ```js
  const str1 = '홑 따옴표 사용.'
  const str2 = "쌍 따옴표 사용."
  
  str1 + str2 // "홑 따옴표 사용쌍 따옴표 사용"
  ```

- 줄 바꿈은 허용하지 않음

  ```js
  const str3 = "줄 바꿈
  은 허락되지 않는다"
  ```

- 줄 바꿈은 `\n`

#### Template 문자열(ES6+)

- 백틱 (`) 으로 표현

- 줄바꿈 가능

  ```js
  const str5 = `안녕하세요.
  줄바꿈도 가능.`
  ```

- 변수 삽입 가능

  ```js
  const num = 100
  const str6 = `${num}개 있습니다.` // "100개 있습니다."
  ```

## 연산자

일반적으로 다른 언어와 큰 차이는 없으므로, JS 만의 특별한 점만 서술한다.

### 동등 연산자 & 일치 연산자

- 동등 연산자 `==`
  - 비교 대상이 서로 다른 타입일 경우, 비교하기 전에 가능하다면 같은 자료형으로 형변환하여 비교한다.
    - `0 == '0'` : 문자열 `'0'`이 숫자로 바뀌고 비교
    - `0 == []` : 둘다 null 로 비교
    - `'' == []` 
  - 이러한 형 변환은 예상치 못한 결과를 초래할 수 있기 때문에 **사용을 지양**
- **일치 연산자 `===`** 
  - 타입과 값 모두 일치하는지 비교
  - 엄격한 비교를 하기 때문에 **동등 연산자보다 권장**

## 반복문

### for of

- 배열에서 요소를 하나씩 순회하며 반복하는 반복문

- 매 요소는 블럭 내에서 새롭게 선언되기 때문에 반드시 변수 선언 키워드를 작성

  ```js
  const numbers = [0, 1, 2, 3]
  
  for (const number of numbers){
      console.log(number) // 0, 1, 2, 3
  }
  ```

- python의 `for`문, C++의 `for :` 등과 비슷하다

### for in

- Object의 Key를 순회하는 반복문이다. Array의 경우 index를 순회한다

  ```js
  const fruits = {a: 'apple', b: 'banana'}
  
  for (const key in fruits){
      console.log(key)			// a, b
      console.log(fruits[key])	// apple, banana
  }
  ```

  ```js
  const fruits = ['apple', 'banana']
  
  for (const idx in fruits){
      console.log(idx)			// 0, 1
      console.log(furits[idx])	// apple, banana
  }
  ```

- `Object.values()`

- `object.entries()`

## 함수

### 함수 표현식

- 이름이 없는 함수 **익명 함수(anonymous function)**

  ```js
  const sub = function (num1, num2) {
      return num1 - num2
  }
  
  sub(7, 2) // 5
  ```

- 기명(이름이 있는) 함수도 함수표현식이 가능하다

  ```js
  const mysub = function sub (num1, num2) {
      return num1 - num2
  }
  mysub(7, 2) // 5
  ```

### 함수 Hoisting

- `function` 키워드로 선언한 함수는 호이스팅 현상을 발생시킨다.

  ```js
  add(1, 3)	// 4
  
  function add(num1, num2) {
      return num1 + num2
  }
  ```

- 함수 표현식으로 정의된 함수를 변수에 담을 때는 변수 선언 키워드 `const`, `var` 등에 달려있다.

  ```js
  sub(3, 5)
  const sub = function (num1, num2) {
      return num1 - num2
  }
  ```

  ```
  Uncaught ReferenceError: Cannot access 'sub' before initialization
  ```

- var 변수는 호이스팅이 발생하지만 var 변수에 함수표현식을 담기 전에는 undefined이기 때문에 함수가 실행되지는 않는다.

  ```js
  sub(3, 5)
  var sub = function (num1, num2) {
      return num1 - num2
  }
  ```

  ```
  Uncaught SyntaxError: Identifier 'sub' has already been declared
  ```


### 화살표 함수(Arrow Function)

- 함수 선언 시 `function` 키워드와 중괄호를 생략하기 위해 고안된 단축 문법이다.

  ```js
  const arrow = function (name) {
      return `hello! ${name}`
  }
  
  // 1. function 키워드 삭제
  const arrow = (name) => { return `hello, ${name}` }
  
  // 2. 매개변수가 하나일 경우 '( )' 생략
  const arrow = name => { return `hello, ${name}` }
  
  // 3. 함수 바디가 하나의 표현식일 경우 '{ }' & return 생략
  const arrow = name => `hello, ${name}`
  
  // 4. 단, 표현식이 object 객체일 경우 '( )' 안쪽에 객체 표현
  const arrow = name => ({ message: `hello, ${name}`})
  ```

## 자료구조

### Array

- 기본 사용법

  ```js
  // 배열 선언
  const numbers = [1, 2, 3, 4]
  // 첨자([]) 인덱싱으로 접근
  numbers[0]
  // python 처럼 음의 인덱스는 지원하지 않는다.
  numbers[-1]
  // 배열의 길이
  numbers.length
  ```

- `.reverse`

  원본 배열을 뒤집고 원본을 리턴한다. (복사는 아님)

  ```js
  numbers.reverse() // [4, 3, 2, 1]
  numbers // [4, 3, 2, 1]
  ```

- `push`

  배열의 요소를 맨 뒤에 넣은 후 길이를 리턴한다.

  ```js
  numbers.push('a')	// 5
  numbers				// [1, 2, 3, 4, 'a']
  ```

- `pop`

  배열의 마지막 요소를 뺀 후 리턴

  ```js
  numbers.pop()	// 'a'
  numbers			// [1, 2, 3, 4]
  ```

- `unshift`

  배열에 요소를 맨 처음에 넣은 후 길이를 리턴

  ```js
  numbers.unshift('a')	// 5
  numbers					// ['a', 1, 2, 3, 4]
  ```

- `shift`

  배열에 첫 요소를 꺼낸 후 리턴

  ```js
  numbers.shift()	// 'a'
  numbers			// [1, 2, 3, 4]
  ```

- `.includes()`

  해당 요소가 있는지 없는지 확인

  ```js
  numbers.includes(1) // true
  numbers.includes(0) // false
  ```

- `indexOf`

  해당 첫번째 요소의 인덱스를 반환, 없으면 `-1`을 반환

  ```js
  numbers.push('a', 'a')
  numbers					// [1, 2, 3, 4, 'a', 'a']
  numbers.indexOf('a')	// 4
  numbers.indexOf('b')	// -1
  ```

- `.join(str)`

  요소들을 `str` 을 사이로 묶은 문자열 반환

  ```js
  numbers.join()		// '1,2,3,4,a,a'
  numbers.join('')	// '1234aa'
  numbers.join('-')	// '1-2-3-4-a-a'
  ```

#### Array Helper Method (ES6+)

- `forEach`

  - 문법

    ```js
    arr.forEach(callback(element, index, array))
    ```

    - `element` : 현재 요소
    - `index` : 현재 인덱스
    - `array` : 원본 배열

  - 예시

    ```js
    const colors = ['red', 'blue', 'green']
    
    colors.forEach(function(color){
        console.log(color)
    })
    ```

    ```
    red
    blue
    green
    ```

- `map`

  - 배열 내 모든 요소에 대해 주어진 callback 함수를 실행하며, 함수의 반환값을 요소로 하는 새로운 배열 반환한다. 배열을 다른 모스으로 바꿀 때 사용한다.

  - 문법

    ```js
    arr.map(callback(element, index, array))
    ```

  - 사용 예시

    ```js
    const nums = [1, 2, 3]
    
    const doubleNums = nums.map(function (num) {
        return num * 2
    })
    console.log(doubleNums)	// [2, 4, 6]
    ```

- `filter`

  - 주어진 callback 함수의 테스트를 만족하는 요소만으로 만든 새로운 배열을 반환한다. callback 함수를 통해 원하는 요소만 추릴 수 있다.

  - 문법

    ```js
    arr.filter(callback(element, index, array))
    ```

  - 사용예시

    ```js
    const products = [
        { name: 'cucumber', type: 'vegetable' },
        { name: 'banana', type: 'fruit' },
        { name: 'carrot', type: 'vegetable' },
        { name: 'apple', type: 'fruit' },
    ]
    
    const fruits = products.filter(function (product) {
        return product.type === 'fruit'
    })
    ```

- - `find`

    - 주어진 callback 함수의 테스트를 만족하는 첫번째 요소를 반환한다. 값이 없다면 undefined를 반환한다.
  
    - 문법
  
      ```js
      arr.find(callback(element, index, array))
      ```
  
    - 사용 예시
  
      ```js
      const avengers = [
          { name: 'Tony Stark', age: 45 },
          { name: 'Steve Rogers', age: 32 },
          { name: 'Thor', age: 40 },
      ]
      
      const avenger = avengers.find(function (avenger) {
          return avenger.name === 'Tony Stark'
      })
      
      console.log(avenger) // { name: 'Tony Stark', age: 45 }
      ```
  
  - `some`
  
    - 배열 안의 하나의 요소라도 callback 함수의 테스트를 만족하면 true를 반환, 아닐 경우 false를 반환한다. 단, 빈 배열에서 호출 시 false를 반환한다.
  
    - 문법
  
      ```js
      arr.some(callback(element, index, array))
      ```
  
    - 사용 예시
  
      ```js
      const requests = [
          { url: '/photos', status: 'complete' },
          { url: '/albums', status: 'pending' },
          { url: '/users', status: 'failed' },
      ]
      
      const inProgress = request.some(function (request) {
          return request.status == 'pending'
      })
      
      console.log(inProgress) // true
      ```
  
  - `every`
  
    - 배열 안의 모든 요소가 callback 함수의 결과 값이 `true`라면 `true`를 반환, 아닐 시 `false` 반환.
  
    - 문법
  
      ```js
      arr.every(callback(element, index, array))
      ```
  
    - 사용 예시
  
      ```js
      const users = [
          { id: 21, submitted: true },
          { id: 33, submitted: false },
          { id: 712, submitted: true },
      ]
      
      const hasSubmitted = users.every(function (user) {
          return user.submitted
      })
      
      console.log(hasSubmitted) // false
      ```
  
  - `reduce`
  
    - 문법
  
      ```js
      arr.reduce(callback(acc, element, index, array), initialValue)
      ```
  
      - acc : 이전 까지의 누적 값
      - initialValue 누적 값의 초기 값 (생략 시 첫번째 요소가 초기값)
  
    - 사용 예시
  
      ```js
      const scores = [90, 90, 80, 77]
      
      const totalScore = scores.reduce(function (sum, score) {
          return sum + score
      }, 0)
      
      console.log(totalScore) // 337
      ```
  

### Object

- 선언

  ```js
  const me = {
      name: '홍길동',
      'phone number': '01012345678',
      appleProducts: {
          ipad: '2018pro',
          iphone: '7+',
          macbook: '2019pro',
      },
  }
  ```

- 요소 접근

  `.key` 또는 `['key']` 로 접근

  ```js
  me.name		// 홍길동
  me['name']	// 홍길동
  ```

  - Key를 식별자로 활용할 수 없는 경우 반드시 []로 접근해야 한다.

    ```js
    // key에 공백이 포함되어 있는 경우
    me['phone number']	
    ```

- Object 축약 문법

  - 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 아래와 같이 축약이 가능하다.

    ```js
    const name = '김아무개'
    const score = '80'
    
    const student = {
        // name: name
        // score: score,
        name,
        score,
    }
    
    console.log(student)	// { name: '김아무개', score: '80'}
    ```


#### JSON

javascript Object 형태를 가지는 문자열

파싱을 통해 Object 변환할 수 있다.

- JSON -> Object

  `JSON.stringify(jsondata)`

- Object -> JSON

  `JSON.parse(object)`

