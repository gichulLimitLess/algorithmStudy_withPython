// 바닥까지 하강
const arr = [
  [0, 1, 0],
  [1, 0, 1],
  [0, 1, 0],
  [0, 0, 1],
  [0, 1, 0],
];

console.log("기존");
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

function gravity(arr) {
  const n = arr.length; // arr의 "세로"
  const m = arr[0].length; // arr의 "가로"
  for (let i = 0; i < m; i++) {
    // 모든 "열"에 대해서
    let write = n - 1;
    for (let j = n - 1; j > -1; j--) {
      // 밑에서부터 위로 하나씩 보면서 간다
      if (arr[j][i] === 1) {
        // 해당 칸에 요소가 있는 경우
        if (write == j) {
          // 여전히 맨 밑을 가리키고 있다면 --> ex) 맨 밑에 '0'이 아닌 경우, 위로 올려서 쌓아야 함
          write -= 1;
          continue;
        }
        [arr[write][i], arr[j][i]] = [arr[j][i], arr[write][i]];
        write -= 1;
      }
    }
  }
}

gravity(arr);
console.log("변화");
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}
