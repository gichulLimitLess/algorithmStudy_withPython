function find_parent(parent, x) {
  if (parent[x] !== x) {
    parent[x] = find_parent(parent, parent[x]); // 경로 압축
  }
  return parent[x];
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
