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

// 노드 6개 (1~6)
const v = 6;
const parent = Array(v + 1).fill(0);
for (let i = 1; i <= v; i++) parent[i] = i;

console.log("초기 parent:", parent.slice(1)); // [1, 2, 3, 4, 5, 6]

// === union(1, 2)
union(parent, 1, 2);
// parent: [1, 1, 3, 4, 5, 6]
console.log("union(1, 2) 후:", parent.slice(1));

// === union(2, 3)
union(parent, 2, 3);
// parent: [1, 1, 1, 4, 5, 6]
console.log("union(2, 3) 후:", parent.slice(1));

// === union(4, 5)
union(parent, 4, 5);
// parent: [1, 1, 1, 4, 4, 6]
console.log("union(4, 5) 후:", parent.slice(1));

// === union(5, 6)
union(parent, 5, 6);
// parent: [1, 1, 1, 4, 4, 4]
console.log("union(5, 6) 후:", parent.slice(1));

// === union(1, 4)
union(parent, 1, 4);
// parent: [1, 1, 1, 1, 4, 4] → find_parent(4)=1 실행 시 자동 압축
find_parent(parent, 6); // 압축 발생 (6→4→1)
console.log("union(1, 4) + 경로 압축 후:", parent.slice(1));

// === 최종 집합 확인
for (let i = 1; i <= v; i++) {
  console.log(`노드 ${i}의 루트:`, find_parent(parent, i));
}
console.log("최종 parent:", parent.slice(1)); // 결과: [ 1, 1, 1, 1, 1, 1 ]
