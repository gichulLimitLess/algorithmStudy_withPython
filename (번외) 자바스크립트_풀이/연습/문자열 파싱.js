/*
    JS에서의 문자열은 Python처럼 불변이다.
    즉, str[0] = 'a' 같은 건 동작하지 않는다.
*/

const s = "a, b, c";
console.log(s.split(",")) // ['a', 'b', 'c']

const s = "Hello   world  JS";
console.log(s.trim().split(/\s+/));
// ["Hello", "world", "JS"]

const s = "   hello world   ";
console.log(s.trim());      // "hello world"
console.log(s.trimStart()); // "hello world   "
console.log(s.trimEnd());   // "   hello world"

const arr = ["a", "b", "c"]
console.log(arr.join("-")); // "a-b-c"

const s = "apple banana apple";
console.log(s.replace("apple", "orange"));
// "orange banana apple" (첫 번째만 교체)

const s = "javascript";
console.log(s.indexOf("script")); // 4
console.log(s.indexOf("java"));   // 0
console.log(s.indexOf("py"));     // -1 (없으면 -1)
console.log(s.includes("script")); // true --> includes()는 Python의 in 느낌으로 쓰면 편하다

// slice()는 배열에서도 동일하게 사용 가능
const s = "abcdefg";
console.log(s.slice(2, 5));     // "cde"

const s = "hello";
console.log(s.split('').reverse().join('')); // "olleh"

// 문자열에서 특정 문자 개수 세기 테크닉
// 'a' 갯수 세기
const s = "banana";
const count = s.split('a').length-1;
console.log(count); // 3


// 문자열을 배열처럼 사용할 수 있다 like Python
const s = "abc";
for (const ch of s) console.log(ch); // a b c
console.log(s[1]); // "b"