// Queue 클래스 생성
class Queue {
  constructor() {
    this.q = [];
    this.head = 0;
  }
  enqueue(x) { this.q.push(x); } // queue에 요소 삽입
  dequeue() { return this.q[this.head++]; } // queue에 요소 제거
  isEmpty() { return this.head >= this.q.length; } // 비어 있는지 확인
}

function bfs(start, graph) {
  const visited = Array(graph.length).fill(false);
  const q = new Queue();
  q.enqueue(start);
  visited[start] = true;

  while (!q.isEmpty()) {
    const node = q.dequeue();
    console.log(node);
    for (const next of graph[node]) {
      if (!visited[next]) {
        visited[next] = true;
        q.enqueue(next);
      }
    }
  }
}