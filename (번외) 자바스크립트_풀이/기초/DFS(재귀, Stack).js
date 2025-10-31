/* 1. DFS 구현 - "재귀" 방식 */
function dfs(node, graph, visited) {
  visited[node] = true;
  console.log(node); // 방문 시 처리 (예: 출력)

  for (const next of graph[node]) {
    if (!visited[next]) {
      dfs(next, graph, visited);
    }
  }
}

const graph = [
  [], // 0번 인덱스 사용 안 함
  [2, 3],
  [1, 4],
  [1, 4],
  [2, 3],
];
const visited = Array(graph.length).fill(false);
dfs(1, graph, visited);

/*
	[출력]
	1
	2
	4
	3
*/

/* 2. DFS 구현 - "Stack" 방식(반복문 사용) */
function dfsStack(start, graph) {
  const visited = Array(graph.length).fill(false);
  const stack = [start];

  while (stack.length > 0) {
    const node = stack.pop();
    if (visited[node]) continue; // 이미 방문한 곳이면, 더 이상 방문하지 않는다
    visited[node] = true;
    console.log(node);

    // 인접 노드 역순으로 push (그래야 탐색 순서 동일 --> 이건 "그려서" 이해해라)
    for (let i = graph[node].length - 1; i >= 0; i--) {
      const next = graph[node][i];
      if (!visited[next]) stack.push(next);
    }
  }
}

const graph2 = [[], [2, 3], [1, 4], [1, 4], [2, 3]];
dfsStack(1, graph2);
