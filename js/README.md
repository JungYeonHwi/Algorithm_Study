# string Property

- 문자 개수 반환 : String.length

```
let data = "Hello";
console.log(data.length) // 3
```

# string Method : 언제나 새로운 값으로 반환

- index에 해당하는 위치의 문자열을 반환 : String.charAt(number)

```
const str = 'Hello';
console.log(str.charAt(0)); // H
```

- 처음 발견된 위치 반환 : String.indexOf(searchstring, fromIndex)

```
const str = 'Hello World';
console.log(str.indexOf('l')) // 2
console.log(str.indexOf('u')) // 존재하지 않을 경우 -1
```

- 마지막으로 발견된 위치 반환 : String.lastIndexOf(searchstring, fromIndex)

fromIndex으로 이동하여 역방향으로 검색

```
const str = 'Hello World';
console.log(str.lastIndexOf('o', 5)); // 4
```

- 검색된 문자열 대체하여 새로운 문자열 반환 : String.replace(searchValue, replaceValue)

```
const str = 'Hello world';
str = str.replace('world', 'Lee');
console.log(str) // Hello Lee
```

- 문자열 내 구분한 후 분리된 각 문자열로 이루어진 배열로 반환 : String.split(separator, limit)

```
const str = 'How are you doing?';
console.log(str.split(' ')); // [ 'How', 'are', 'you', 'doing?' ]
```

- 문자열 부분 추출 : String.substring(star, end)

```
const str = 'Hello World';
const data = str.substring(1, 4);
console.log(data) // ell
```

- 문자열 부분 추출 : String.slice(star, end)

```
const str = 'Hello World';
const data = str.slice(1, 4);
console.log(data) // ell
```

- 소문자 변경 : String.toLowerCase()

- 대문자 변경 : String.toUpperCase()

- 공백 문자 양쪽 끝 제거 : String.trim()

```
const str = '   foo  ';
console.log(str.trim()); // 'foo'
```

- 숫자만큼 반복해서 연결한 새로운 문자열 반환 : String.repeat(count)

```
const str = "abc".repeat(2)
console.log(str) // abcabc
```

- 문자열 포함되어 있는지 검사 후 true/false로 반환 : String.includes(searchString, position)

```
const str = 'hello world';
str.includes('hello'); // true
str.includes('hello', 2) // false
```

- 첫번째 인수로 전체 스트링 길이를 지정하고, 만일 현재 문자열의 길이가 인수보다 짧다면, 그 빈 나머지를 두번째 인수값으로 채움 : String.padStart(targetLength, padString)

```
'abc'.padStart(10);         // "       abc"
'abc'.padStart(10, "foo");  // "foofoofabc"
```

# Array Method

- 배열 뒷부분 값 삭제 : pop

```
var arr = [ 1, 2, 3, 4 ];
arr.pop();
console.log( arr ); // [ 1, 2, 3 ]
```

- 배열 뒷부분에 값 삽입 : push

```
var arr = [ 1, 2, 3, 4 ];
arr.push( 5 );
console.log( arr ); // [ 1, 2, 3, 4, 5 ]
```

- 배열 앞부분에 값 삽입 : unshift

```
var arr = [ 1, 2, 3, 4 ];
arr.unshift( 0 );
console.log( arr ); // [ 0, 1, 2, 3, 4 ]
```

- 배열 앞부분에 값 삭제 : shift

```
var arr = [ 1, 2, 3, 4 ];
arr.shift();
console.log( arr ); // [ 2, 3, 4 ]
```

- 배열 특정 위치에 요소를 추가하거나 삭제 : splice( index, 제거할 요소 개수, 배열에 추가될 요소 )

```
var arr = [ 1, 2, 3, 4, 5, 6, 7 ];
arr.splice( 3, 2 );
console.log( arr ); // [ 1, 2, 3, 6, 7 ]   3번째 인덱스에서부터 2개 제거

var arr = [ 1, 2, 3, 4, 5, 6, 7 ];
arr.splice( 2, 1, "a", "b");
console.log( arr ); // [ 1, 2, "a", "b", 4, 5, 6, 7 ] 2번째 인덱스에서 1개 제거 후 "a"와 "b"를 추가
```

- 배열 시작부터 끝 위치에 대한 새로운 배열 객체 반환 : slice( startIndex, endIndex)

```
var arr = [ 1, 2, 3, 4, 5, 6, 7 ];
var newArr = arr.slice( 3, 6 );
console.log( 'slice',  newArr ); // [ 4, 5, 6 ]
```

- 배열 합치고 배열 반환 : concat()

```
var arr1 = [ 1, 2, 3 ];
var arr2 = [ 4, 5, 6 ];
var arr3 = arr2.concat( arr1 );
console.log( arr3 ); // [ 4, 5, 6, 1, 2, 3 ]
```

- 배열의 모든 요소가 제공한 함수로 구현된 테스트를 통과하는지를 테스트 : every

```
var arr =[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ];
var isEven = function( value ) {

  // value가 2의 배수이면 true를 반환한다.
  return value % 2 === 0;
};
console.log( arr.every( isEven ) ); // false  모든 요소가 true이면 true를 return 하고 그렇지 않으면 false
```

- 지정된 함수의 결과가 true일 때까지 배열의 각 원소를 반복 : some

```
var arr =[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ];
var isEven = function( value ) {

  // value가 2의 배수이면 true를 반환한다.
  return value % 2 === 0;
};
console.log( arr.some( isEven ) ); // true  하나라도 true이면 true를 return
```

- 배열 각 원소별로 지정된 함수 실행 : forEach

```
var arr =[ 1, 2, 3 ];
arr.forEach( function( value ) {
  console.log( value );   // 1 2 3
});
```

- 배열의 각 원소별로 지정된 함수를 실행한 결과로 구성된 새로운 배열을 반환 : map

```
var arr =[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ];
var isEven = function( value ) {
  return value % 2 === 0;
};
var newArr = arr.map( isEven );
console.log( newArr ); // [ false, true, false, true, false, true, false, true, false, true ]
```

- 지정된 함수 결과 값을 true로 만드는 원소들로만 구성된 별도 배열 반환 : filter

```
var arr =[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ];
var isEven = function( value ) {
  return value % 2 === 0;
};
var newArr = arr.filter( isEven );
console.log( newArr ); // [ 2, 4, 6, 8, 10 ]
```

- 누산기, 좌에서 우로 계산된 값 함수 적용 : reduce

```
var arr =[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ];
var value = arr.reduce( function( previousValue, currentValue, index ) {
  return previousValue + currentValue;
});
console.log( value ); // 55
```

- 배열 원소 뒤집기 : reverse

```
var arr =[ 1, 2, 3, 4 ];
arr.reverse();
console.log( arr ); // [ 4, 3, 2, 1 ]
```

- 배열 원소 순서대로 : sort

```
var arr = [ 13, 12, 11, 10, 5, 3, 2, 1 ];
arr.sort();
console.log( arr ); // [ 1, 10, 11, 12, 13, 2, 3, 5 ];
```

- 배열을 문자열로 바꾸어 반환 : toString

```
var arr =[ 1, 2, 3, 4 ];
console.log( arr.toString() ); // 1, 2, 3, 4
```

- 배열 원소 전부를 하나의 문자열로 합침 : join

```
var arr =[ 1, 2, 3, 4 ];
console.log(arr.join()); // 1,2,3,4

```
