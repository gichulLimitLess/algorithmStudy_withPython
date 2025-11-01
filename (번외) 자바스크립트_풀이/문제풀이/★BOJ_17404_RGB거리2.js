// JS 입출력용 구문
const fs = require("fs");
const path = require("path");
const filePath = process.platform === "linux" ? "/dev/stdin" : path.join(__dirname, "input.txt");
const input = fs.readFileSync(filePath).toString().trim().split("\n");

/*
  [사고 과정]
  순환형 DP -> 시작점 고정!
*/
const n = Number(input[0]);
const rgb_cost = [];
for (let i = 0; i < n; i++) {
  const row = input[i + 1].split(" ").map(Number);
  rgb_cost.push(row);
}

let answer = Infinity;

// 2~N까지는, 안 겹치게 선택만 하면 됨! --> 1, N번 집이 안 겹치게 한다.
for (let i = 0; i < 3; i++) {
  const dp = Array.from(Array(n), () => [Infinity, Infinity, Infinity]);
  dp[0][i] = rgb_cost[0][i]; // 첫번째 색을 고정한다
  for (let j = 1; j < n; j++) {
    // 2~N번째까지 안 겹치게 쭉 채운다
    dp[j][0] = rgb_cost[j][0] + Math.min(dp[j - 1][1], dp[j - 1][2]);
    dp[j][1] = rgb_cost[j][1] + Math.min(dp[j - 1][0], dp[j - 1][2]);
    dp[j][2] = rgb_cost[j][2] + Math.min(dp[j - 1][0], dp[j - 1][1]);
  }
  for (let k = 0; k < 3; k++) {
    if (i !== k) {
      // 현재 고정된 첫번째 집의 색깔과 겹치지 않는 경우에만
      answer = Math.min(answer, dp[n - 1][k]);
    }
  }
}

console.log(answer); // 모든 집을 칠하는 비용의 최소 출력
