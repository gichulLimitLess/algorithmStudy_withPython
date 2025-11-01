// JS 입출력용 구문
const fs = require("fs");
const path = require("path");
const filePath = process.platform === "linux" ? "/dev/stdin" : path.join(__dirname, "input.txt");
const input = fs.readFileSync(filePath).toString().trim().split("\n");

/*
  [사고 과정]
  일단, 앞뒤로 1씩 차이 나는지 일일이 분석해 보려면..
  --> '완탐'으로 풀려면, 각 자리 별로.. 1~9까지 모든 수 탐색해야 함 -> 9^100?
  --> 바로 떠올려야 할 것은.. DP

  [상태 정의 & 점화식 세우기]
  dp[i][j] = i번째 자리의 수가 숫자 j일 때, 가능한 계단 수의 개수 (손으로 예시들 그려보면서 어떤 상태가 좋을지 정의)
  dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
  dp[0][0] = 0 --> 첫번째 자리가 0인 것은 계단 수가 아니다
*/

const n = Number(input[0]);
const dp = Array.from(Array(n), () => Array(10).fill(0));
const INF = 1000000000;

// 초기값 설정
dp[0][0] = 0;
for (let i = 1; i < 10; i++) {
  dp[0][i] = 1 % INF;
}

// 상태 전이 (--> 선형 DP, 2차원 배열을 채워 나간다 / O(100*10))
for (let i = 1; i < n; i++) {
  for (let j = 0; j < 10; j++) {
    if (j === 9) {
      dp[i][j] = dp[i - 1][j - 1];
    } else if (j === 0) {
      dp[i][j] = dp[i - 1][j + 1];
    } else {
      dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % INF;
    }
  }
}

let answer = 0;
for (let i = 0; i < 10; i++) {
  answer += dp[n - 1][i] % INF;
}

console.log(answer % INF);
