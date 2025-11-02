// 스택 오버플로 위험이 없는 "반복문" 형태로 작성 -> Path Compression 또한 수행하는 버전
function find_parent(parent, x) {
  let root = x;
  while (parent[root] !== root) {
    // 1. 현재 root가 root랑 같지 않다면 (자기 자신이 아니라면)
    root = parent[root]; // 타고 올라가서, 궁극적인 부모를 찾는다
  }
  // 2. 경로 압축 밑에서부터 위로 하나씩 수행
  while (parent[x] !== root) {
    let next = parent[x];
    parent[x] = root; // 궁극적으로 찾은 부모를 현재 parent에 넣는다
    x = next; // 지금 x 위에 있는 애를 찾으러 떠난다
  }
  if (parent[x] !== x) {
    parent[x] = find_parent(parent, parent[x]); // 경로 압축
  }
  return root; // 궁극적인 부모를 return 해준다
}

function union(parent, a, b) {
  const x = find_parent(parent, a);
  const y = find_parent(parent, b);
  if (x < y) {
    // 보통 크기가 작은 애가 부모로 설정함
    parent[y] = x;
  } else {
    parent[x] = y;
  }
}

// 크루스칼 알고리즘 (cost-first edge list)
function kruskal(v, edges) {
  // 1. 부모 배열 초기화
  const parent = Array(v + 1).fill(0);
  for (let i = 1; i <= v; i++) parent[i] = i;

  // 2. 비용 기준 오름차순 정렬
  edges.sort((a, b) => a[0] - b[0]);

  let totalCost = 0;
  const mstEdges = [];

  // 3. 간선 순회
  for (const [cost, a, b] of edges) {
    if (find_parent(parent, a) !== find_parent(parent, b)) {
      // 부모가 겹치지 않는 경우 --> 사이클로 탐지되지 않는 경우에만
      union(parent, a, b);
      totalCost += cost;
      mstEdges.push([a, b, cost]);
    }
  }

  return { totalCost, mstEdges, parent };
}

// 예시 실행
const v = 4;
const edges = [
  [1, 1, 2],
  [3, 1, 3],
  [2, 1, 4],
  [4, 2, 4],
  [5, 3, 4],
];

const result = kruskal(v, edges);

console.log("MST 총 비용:", result.totalCost);
console.log("MST 구성 간선:", result.mstEdges);
console.log("최종 parent 배열:", result.parent.slice(1));

/*
  [출력 결과]
  MST 총 비용: 6
  MST 구성 간선: [ [ 1, 2, 1 ], [ 1, 4, 2 ], [ 1, 3, 3 ] ]
  최종 parent 배열: [ 1, 1, 1, 1 ]
*/
