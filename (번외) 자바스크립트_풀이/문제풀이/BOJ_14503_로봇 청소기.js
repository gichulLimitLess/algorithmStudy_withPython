// JS 입출력용 구문
const fs = require("fs");
const path = require("path");
const filePath = process.platform === "linux" ? "/dev/stdin" : path.join(__dirname, "input.txt");
const input = fs.readFileSync(filePath).toString().trim().split("\n");

/*
  [사고 과정]
  그동안 풀었던 시뮬레이션 문제에 비해서는 그리 어렵지 않은 시뮬레이션 문제
  --> Queue(BFS)를 활용해서, 문제에서 주어진 instruction을 그대로 따르면 될 듯 하다
*/
class Queue {
  constructor() {
    this.q = [];
    this.head = 0;
  }
  enqueue(x) {
    this.q.push(x);
  }
  dequeue() {
    return this.q[this.head++];
  }
  isEmpty() {
    return this.head >= this.q.length;
  }
}

const [n, m] = input[0].split(" ").map(Number);
const [r, c, d] = input[1].split(" ").map(Number);
const board = [];
for (let i = 0; i < n; i++) {
  // 방의 정보 입력받기
  const row = input[i + 2].split(" ").map(Number);
  board.push(row);
}

const queue = new Queue(); // Queue를 사용할 것임
queue.enqueue([r, c, d]);
board[r][c] = 2; // 현재 로봇 청소기가 위치한 곳은 "청소한 곳"이라 표기
let cnt = 0; // 청소한 칸의 갯수 저장
cnt++;

const dy = [-1, 0, 1, 0];
const dx = [0, 1, 0, -1];

while (!queue.isEmpty()) {
  // --> board의 모든 칸 탐색 (O(2500))
  const [y, x, d] = queue.dequeue();
  let isAllCleaned = true; // "현재 칸의 주변 4칸" 청소 여부 저장
  // 청소 여부 확인
  for (let i = 0; i < 4; i++) {
    const ny = y + dy[i];
    const nx = x + dx[i];
    if (board[ny][nx] === 0) {
      // "청소하지 않은 빈 칸"이 있는 경우
      isAllCleaned = false;
      break;
    }
  }

  // "현재 칸의 주변 4칸 중 청소가 되지 않은 빈 칸이 없는 경우"
  if (isAllCleaned) {
    const ny = y + dy[(d + 2) % 4]; // 현재 방향에서 반대 방향으로 이동("후진")
    const nx = x + dx[(d + 2) % 4];
    if (board[ny][nx] === 1) {
      // 뒤쪽 칸이 "벽"이라서 후진 못하는 경우
      break; // 작동 중지
    } else {
      // "후진" 자체는 가능한 경우
      if (board[ny][nx] === 0) {
        // 뒤로 갔는데, 거기가 만약 "청소 안 한 구역"이라면
        board[ny][nx] = 2; // 청소한 칸으로 표시
        cnt++; // 청소한 칸 개수 증가
      }
      queue.enqueue([ny, nx, d]); // 후진한 상태 저장
    }
  } else {
    // 빈 칸이 있는 경우
    const ny = y + dy[(d + 3) % 4]; // 현재 방향에서 반시계 방향으로 90도 회전
    const nx = x + dx[(d + 3) % 4];
    if (board[ny][nx] === 0) {
      // 바라보는 방향 기준으로 앞쪽 칸이 "청소되지 않은 빈 칸"이면
      board[ny][nx] = 2; // 청소한 칸으로 표시
      cnt++; // 청소한 칸 개수 증가
      queue.enqueue([ny, nx, (d + 3) % 4]);
    } else {
      // 그게 아니면.. --> 방향만 틀은 상태를 Queue에 저장하긴 해야 함
      queue.enqueue([y, x, (d + 3) % 4]);
    }
  }
}

console.log(cnt); // 로봇이 작동을 중지할 때까지 청소하는 칸 개수 출력
