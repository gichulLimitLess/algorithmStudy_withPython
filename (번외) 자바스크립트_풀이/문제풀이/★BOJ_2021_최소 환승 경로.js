/*
  [사고 과정: Step-by-Step COT]

  🧩 1. 문제 구조 파악
  - 최소 환승 횟수를 구해야 함.
  - 즉, 이동 "횟수"가 아니라 "환승" 단위임 → 환승이 BFS의 depth 단위가 되어야 함.
  - 같은 노선 안의 이동은 환승이 아님. 
    따라서 BFS 한 단계는 "노선 간 전환(환승)"으로 정의해야 함.

  🧩 2. 데이터 구조 설계
  - 역(node) ↔ 노선(line)의 연결 구조를 따로 관리해야 함.
  - 이유: 하나의 역이 여러 노선에 속할 수 있음.
  - 따라서 "노선 간 연결"은 "공통된 역"을 통해서만 일어남.
  
  (즉, 환승이 일어나는 포인트는 '역'이 아니라 '노선 간 연결'이다.)
*/

const fs = require("fs");
const path = require("path");
const filePath = process.platform === "linux" ? "/dev/stdin" : path.join(__dirname, "input.txt");
const input = fs.readFileSync(filePath).toString().trim().split("\n");

// Queue 클래스 (기처리 스타일 그대로)
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

/* 1️⃣ 입력 처리 */
const [n, l] = input[0].split(" ").map(Number); // 역 개수, 노선 개수
const lines = []; // 각 노선이 지나가는 역 목록
const stationToLines = Array.from({ length: n + 1 }, () => []); // 역 → 포함된 노선 목록

// 각 노선 정보 입력
for (let i = 0; i < l; i++) {
  const arr = input[i + 1].split(" ").map(Number);
  arr.pop(); // 마지막 -1 제거
  lines.push(arr);
  // 각 역이 어떤 노선에 속하는지 기록
  for (const st of arr) stationToLines[st].push(i);
}

const [start, end] = input[l + 1].split(" ").map(Number);

/*
  🧩 3. 예외 처리
  - 시작역과 도착역이 같으면 환승할 필요가 없음.
*/
if (start === end) {
  console.log(0);
  process.exit(0);
}

/*
  🧩 4. BFS 초기 설정
  - 노선 단위로 탐색.
  - 이유: 환승 = 노선 간 전이 → 노선이 BFS의 노드 단위.
  - BFS queue에 들어가는 요소: [노선번호, 환승횟수]
*/
const visitedLine = Array(l).fill(false); // 노선 방문 여부
const visitedStation = Array(n + 1).fill(false); // 역 방문 여부
const q = new Queue();

for (const line of stationToLines[start]) {
  q.enqueue([line, 0]); // 시작역에 포함된 모든 노선을 0회 환승 상태로 push
  visitedLine[line] = true;
}
visitedStation[start] = true;

let answer = -1;

/*
  🧩 5. BFS 탐색 시작
  - 한 단계 = "환승 1회"
  - 같은 노선 내에서 역을 순회하며 도착역을 찾는다.
  - 만약 다른 노선과 연결된 역(station)을 만나면 → 그 노선으로 넘어갈 수 있다 (환승 +1)
*/
while (!q.isEmpty()) {
  const [curLine, transfer] = q.dequeue(); // 현재 노선, 환승 횟수

  for (const st of lines[curLine]) {
    // 현재 노선이 지나가는 모든 역을 순회
    if (st === end) {
      // 도착역을 발견하면 종료
      answer = transfer;
      q.q.length = 0; // 큐 비워서 즉시 종료
      break;
    }

    // 아직 방문하지 않은 역이라면
    if (!visitedStation[st]) {
      visitedStation[st] = true;

      // 해당 역을 통해 환승 가능한 다른 노선으로 이동
      for (const nextLine of stationToLines[st]) {
        if (!visitedLine[nextLine]) {
          visitedLine[nextLine] = true;
          q.enqueue([nextLine, transfer + 1]); // 환승 1회 증가
        }
      }
    }
  }
}

/*
  🧩 6. 결과 출력
  - 환승 횟수를 출력하되, 시작역이 이미 도착역인 경우엔 0
*/
console.log(answer);
