const arr = [1, 30, 4, 21, 10000]
// 숫자 정렬할 때는 기본적으로 아래와 같이 정렬 시켜야 함
// --> js에서는 기본적으로 sort()를 쓰면, "문자열" 기준으로 정렬됨
arr.sort((a, b) => a-b); // 오름차순 정렬
arr.sort((a, b) => b-a); // 내림차순 정렬

// 오름차순 정렬 예시
const nums = [5, 2, 9, 1];
nums.sort((a, b) => a - b);
console.log(nums); // [1, 2, 5, 9]

// 내림차순 정렬 예시
const nums = [5, 2, 9, 1];
nums.sort((a, b) => b - a);
console.log(nums); // [9, 5, 2, 1]

// 객체 배열 정렬 --> 아래가, 프론트엔드/코테에서 가장 자주 나오는 형태
const users = [
  { name: "Junho", age: 24 },
  { name: "Min", age: 19 },
  { name: "Hana", age: 22 }
];

// 나이 기준 오름차순
users.sort((a, b) => a.age - b.age);
console.log(users);
// [{Min,19},{Hana,22},{Junho,24}]

// 문자열 기준 정렬하려면 localeCompare 사용
// localCompare는 앞이 뒤보다 작으면 음수 -> 오름차순
// '내림차순' 정렬하고 싶으면 a와 b의 순서를 바꾸면 된다
users.sort((a, b) => a.name.localeCompare(b.name)); // 오름차순 정렬
users.sort((a, b) => b.name.localeCompare(a.name)); // 내림차순 정렬

// ========= .reverse() 관련 =========
const array1 = ["one", "two", "three"];
console.log("array1:", array1);
// 기대 결과: "array1:" Array ["one", "two", "three"]

const reversed = array1.reverse();
console.log("reversed:", reversed);
// Expected output: "reversed:" Array ["three", "two", "one"]