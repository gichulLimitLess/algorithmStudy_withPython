const s = new Set([1, 2, 3, 3, 2]);
console.log(s); // Set(3) {1, 2, 3}

const s = new Set();
s.add(1);
s.add(2);
s.add(2); // 중복 무시
console.log(s); // Set(2) {1, 2}

console.log(s.has(1)); // true
s.delete(1);           // 값 삭제
console.log(s.has(1)); // false

const s = new Set([1, 2, 3]);
console.log(s.size); // 3

s.clear();
console.log(s.size); // 0

const s = new Set(["a", "b", "c"]);
for (const v of s) console.log(v);
// a b c

s.forEach(v => console.log(v));
// a b c

/* 순회 및 “Set → Array (혹은 그 반대로) 변환 (+중복 제거)” */
// Set -> Array 변환
const s = new Set([1, 2, 3]);
const arr = [...s];
console.log(arr); // [1, 2, 3]

// Array -> Set 변환 (중복 제거)
const arr = [1, 2, 2, 3, 3];
const unique = [...new Set(arr)]; // Python에서.. list(set(arr))와 동일
console.log(unique); // [1, 2, 3]