const s1 = new Set([1, 2, 3, 3, 2]);
console.log(s1); // Set(3) {1, 2, 3}

const s2 = new Set();
s2.add(1);
s2.add(2);
s2.add(2); // 중복 무시
console.log(s2); // Set(2) {1, 2}

console.log(s2.has(1)); // true
s2.delete(1); // 값 삭제
console.log(s2.has(1)); // false

const s3 = new Set([1, 2, 3]);
console.log(s3.size); // 3

s3.clear();
console.log(s3.size); // 0

const s4 = new Set(["a", "b", "c"]);
for (const v of s4) console.log(v);
// a b c

s4.forEach((v) => console.log(v));
// a b c

/* 순회 및 “Set → Array (혹은 그 반대로) 변환 (+중복 제거)” */
// Set -> Array 변환
const s5 = new Set([1, 2, 3]);
const arr1 = [...s];
console.log(arr1); // [1, 2, 3]

// Array -> Set 변환 (중복 제거)
const arr2 = [1, 2, 2, 3, 3];
const unique = [...new Set(arr2)]; // Python에서.. list(set(arr))와 동일
console.log(unique); // [1, 2, 3]
