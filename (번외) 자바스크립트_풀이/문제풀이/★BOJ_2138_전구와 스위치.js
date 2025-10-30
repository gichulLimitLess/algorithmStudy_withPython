// JS 입출력용 구문
const fs = require("fs");
const path = require("path");

const filePath = process.platform === "linux" ? "/dev/stdin" : path.join(__dirname, "input.txt");

const input = fs.readFileSync(filePath).toString().trim().split("\n");

/*
  [문제풀이]
  2트였는데 결국 이번에도 해결책을 생각해 내지 못함.
  -> 답지를 봤는데, 생각이 "많이" 필요한 문제였음
  -> "그리디"라는 것을 인지조차 못함
  -> dp로 풀면 안된다는 것만 알고 있었는데('전이'가 단방향이 아닌 것 같은 느낌이어서)..
    0번 스위치 누른 경우, 안 누른 경우를 분기로 끝까지 "그리디"로 수행해보면 될 듯?
*/
const n = Number(input[0]);
const now_status = input[1].split("").map(Number);
const goal_status = input[2].split("").map(Number);

// 토글
function toggle(state, idx) {
  for (let i = idx - 1; i <= idx + 1; i++) {
    if (i >= 0 && i < state.length) state[i] ^= 1;
  }
}

// 오른쪽으로 계속해서 진행
function greedySwitch(start, target, firstPressed) {
  const arr = [...start];
  let count = 0;

  if (firstPressed) {
    toggle(arr, 0);
    count++;
  }

  for (let i = 1; i < arr.length; i++) {
    if (arr[i - 1] !== target[i - 1]) {
      toggle(arr, i);
      count++;
    }
  }

  return arr.join("") === target.join("") ? count : Infinity;
}

// 수행
function solution(N, A, B) {
  const case1 = greedySwitch(A, B, false);
  const case2 = greedySwitch(A, B, true);
  const result = Math.min(case1, case2);
  console.log(result === Infinity ? -1 : result);
}

solution(n, now_status, goal_status);
