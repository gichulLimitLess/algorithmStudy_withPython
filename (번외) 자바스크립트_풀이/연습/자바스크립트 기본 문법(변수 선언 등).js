/* 변수 선언 */
const x = 10;
let y = 5;
y = y + 2; // 가능
// x = 20; // ❌ TypeError (const 재할당 불가)



/* 조건문 */
if (조건식) {
  // 실행문
} else if (다른조건) {
  // 실행문
} else {
  // 나머지 경우
}



/* 반복문 */
// 전통적인 for문
for (let i = 0; i < n; i++) {
  console.log(i);
}

// 배열 순회
const arr = [10, 20, 30];
for (let num of arr) console.log(num); // 값 기반 (-> '값' 기반은 of)
for (let idx in arr) console.log(idx); // 인덱스 기반 (-> '인덱스' 기반은 in)
arr.forEach((v, i) => console.log(i, v)); // 고차함수

//while문
let i = 0;
while (i < 5) {
	console.log(i);
	i++;
}



/* 논리 & 삼항 연산자 */
console.log(false && true); // false
console.log(true && true);  // true
console.log(true || false); // true
console.log(false || true); // true
console.log(!true);   // false
console.log(!false);  // true
console.log(!0);      // true

// 코테에서 짧게 조건 분기할 때 자주 사용됨
const result = (x > 0) ? 'positive' : 'non-positive';



