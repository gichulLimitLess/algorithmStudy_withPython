/* 1. 파이썬에서 몫 나누기(//)는 어떻게? */
// Math.floor() - 내림(floor) 기반 --> 이게 Python에서 '//' 연산자랑 동일한 역할 함! (단, 항상 음수 방향으로 내린다)
console.log(Math.floor(7 / 3));  // 2
console.log(Math.floor(-7 / 3)); // -3

// Math.trunc() - 소수점 버림(truncate) 기반
console.log(Math.trunc(7 / 3));  // 2
console.log(Math.trunc(-7 / 3)); // -2


/* 2. 나머지(%) 연산자 */
console.log(7 % 3);   // 1
console.log(-7 % 3);  // -1 (Python과 다르게 음수 유지)


/* 3. 기타 연산자들 */
// JS는 소수점 표현 오차가 발생할 수 있음을 유의하자
// --> ex) 0.1 + 0.2 === 0.3 → false
console.log(7 / 3);  // 2.3333333333333335

// 거듭제곱 연산자
console.log(2 ** 3);  // 8

// 반올림, 올림, 내림, 버림
console.log(Math.round(3.5)); // 4
console.log(Math.ceil(3.1));  // 4
console.log(Math.floor(3.9)); // 3
console.log(Math.trunc(-3.9)); // -3