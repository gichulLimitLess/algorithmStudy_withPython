/* 순열 함수 */
const num_list = [1, 3, 5];
const visited = Array(num_list.length).fill(false);

// 순열 진행하는 함수 permutations
function permutations(r, depth, res) {
  if (depth === r) {
    // 기저 조건 --> 원하는 갯수만큼 골랐을 때
    console.log(res);
    return;
  }
  for (let i = 0; i < num_list.length; i++) {
    if (!visited[i]) {
      // 방문 안 했을 경우에만
      visited[i] = true; // 방문 처리하고
      permutations(r, depth + 1, [...res, num_list[i]]); // JS에서는, 이렇게 새로운 배열 만들어서 넘겨줘야 한다!
      visited[i] = false; // 끝났으면 방문 처리 해제
    }
  }
}

permutations(3, 0, []);

/* 조합 함수 */
function combinations(r, start, depth, res) {
  if (depth === r) {
    // 기저 조건 --> 원하는 갯수만큼 골랐을 때
    console.log(res);
    return;
  }
  for (let i = start; i < num_list.length; i++) {
    combinations(r, i + 1, depth + 1, [...res, num_list[i]]);
  }
}

combinations(2, 0, 0, []);
