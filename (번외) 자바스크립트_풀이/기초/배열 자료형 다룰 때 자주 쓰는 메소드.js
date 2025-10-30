/*
    기본 메소드들:
    pop() -> 맨 뒤에 요소 꺼내기 (O(1) 걸림)
    push() -> 맨 뒤에 요소 추가 (O(1) 걸림)
    ===================================
    shift() -> 맨 앞에 요소 꺼내기 (O(n) 걸림)
    unshift() -> 맨 앞에 요소 추가 (O(n) 걸림)
*/
/* 1. forEach() */
const arr = [1, 2, 3];
arr.forEach(x => console.log(x * 2));
// 출력: 2 4 6


/* 2. map() */
const arr = [1, 2, 3];
const doubled = arr.map(x => x * 2);
console.log(doubled); // [2, 4, 6]


/* 3. filter() */
const arr = [1, 2, 3, 4, 5];
const evens = arr.filter(x => x % 2 === 0);
console.log(evens); // [2, 4]


/* 4. reduce() */
const arr = [1, 2, 3, 4];
const sum = arr.reduce((acc, cur) => acc + cur, 0);
console.log(sum); // 10

const maxVal = arr.reduce((acc, cur) => Math.max(acc, cur));
console.log(maxVal); // 4


/* 5. find() --> 조건을 만족하는 "첫번째" 원소만 반환 */
const arr = [5, 10, 15, 20];
const res = arr.find(x => x > 12);
console.log(res); // 15


/* 6. some(), every() --> 배열이 조건을 만족하는지 판단: Boolean 반환 */
const arr = [1, 3, 5];
console.log(arr.some(x => x % 2 === 0)); // false (하나도 짝수 아님)
console.log(arr.every(x => x % 2 !== 0)); // true (모두 홀수)


/* 7. 특정 값 존재 여부 판단 (Python의 in과 동일) */
const arr = ["apple", "banana", "cherry"];
console.log(arr.includes("banana")); // true
console.log(arr.includes("grape"));  // false