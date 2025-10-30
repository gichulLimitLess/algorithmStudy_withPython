/*
  리스트 회전 
  --> 90도, 180도, 270도 버전 있음
  90도 버전: rotated_90()
  180도 버전: rotated_180()
  270도 버전: rotated_270()
*/
function rotated_90(a) {
  const n = a.length; // 기존(a)의 세로
  const m = a[0].length; // 기존(a)의 가로
  const result = Array.from(Array(m), () => Array(n).fill(0)); // 배열의 가로, 세로 길이 뒤바뀌는 거 주의
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      result[j][n - 1 - i] = a[i][j];
    }
  }
  return result;
}

function rotated_180(a) {
  const n = a.length; // 기존(a)의 세로
  const m = a[0].length; // 기존(a)의 세로
  const result = Array.from(Array(n), () => Array(m).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      result[n - 1 - i][m - 1 - j] = a[i][j];
    }
  }
  return result;
}

function rotated_270(a) {
  const n = a.length; // 기존(a)의 세로
  const m = a[0].length; // 기존(a)의 가로
  const result = Array.from(Array(m), () => Array(n).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      result[m - 1 - j][i] = a[i][j];
    }
  }
  return result;
}

const a = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
];

console.log(rotated_90(a));
console.log(rotated_180(a));
console.log(rotated_270(a));
