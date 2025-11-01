// JS 입출력용 구문
const fs = require("fs");
const path = require("path");
const filePath = process.platform === "linux" ? "/dev/stdin" : path.join(__dirname, "input.txt");
const input = fs.readFileSync(filePath).toString().trim().split("\n");

/*
  보조 PD들이 만든 순서들을 입력 받았을 때..
  전체 가수의 순서를 정하는 프로그램? ---> 와.. 완전 위상정렬의 전형적인 형태
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
const graph = Array.from(Array(n + 1), () => []);
const indegree = Array(n + 1).fill(0);

// 그래프 연결 정보 및 indegree 추가
for (let i = 0; i < m; i++) {
  const infos = input[i + 1].split(" ").map(Number).slice(1);
  for (let j = 0; j < infos.length - 1; j++) {
    graph[infos[j]].push(infos[j + 1]);
    indegree[infos[j + 1]] += 1;
  }
}

// indegree가 0인 애들 우선 Queue에 집어 넣기
const queue = new Queue();
for (let i = 1; i < indegree.length; i++) {
  if (indegree[i] === 0) {
    queue.enqueue(i);
  }
}
const result = [];
cnt = 0;
while (!queue.isEmpty()) {
  const now = queue.dequeue();
  result.push(now);
  cnt += 1;
  for (const e of graph[now]) {
    // Queue에서 빼낸 애들과 연결된 애들 indegree 1씩 감소
    indegree[e] -= 1;
    if (indegree[e] === 0) {
      // 1 뺐는데, 그게 0이 되었다면
      queue.enqueue(e); // 새로이 넣는다
    }
  }
}

if (cnt !== n) {
  // 모두 Queue에 못 들어간 경우 --> 중간에 뭔가 Cycle이 있는 경우
  console.log(0);
} else {
  console.log(result.join("\n")); // 결과 출력
}
