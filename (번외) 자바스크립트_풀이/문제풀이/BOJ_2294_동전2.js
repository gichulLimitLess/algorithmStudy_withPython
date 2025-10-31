// JS 입출력용 구문
const fs = require("fs");
const path = require("path");

const filePath = process.platform === "linux" ? "/dev/stdin" : path.join(__dirname, "input.txt");

const input = fs.readFileSync(filePath).toString().trim().split("\n");

/*
  [사고 과정]
  -> 각 갯수에 따라서, 합계 동전 가치 다 계산하면, nC1+nC2+.. 절대 시간 내에 구할 수 없다
  -> 한 상태로 가는 경우가 "여러 개" -> DP로 풀어야 겠다
  -> 상태 정의: dp[i] = i의 가치를 만들기 위해 사용하는 동전의 최소 개수
  -> 전이식: dp[i] = min(dp[i-coin]+1, dp[i]) (i-coin이 0보다 크거나 같을때만!)
*/
// n가지 종류의 동전, 가치의 합 k
const [n, k] = input[0].split(" ").map(Number);
const coins = [];
for (let i = 0; i < n; i++) {
  // 동전 정보 집어넣기
  coins.push(Number(input[i + 1]));
}

// dp[i] = i의 가치를 만들기 위해 사용하는 동전의 최소 개수
const dp = Array(k + 1).fill(-1);
dp[0] = 0; // 초기화

// dp 테이블 채우기 수행
for (let i = 1; i < k + 1; i++) {
  for (const coin of coins) {
    // 동전 하나씩 돌아가며 탐색
    if (i - coin >= 0 && dp[i - coin] != -1) {
      // i-coin이 유효한 범위이고, 그곳에 있는 값이 "유효한 경로"임을 표시해야 함
      if (dp[i] === -1) {
        // 처음 적는 경우라면
        dp[i] = dp[i - coin] + 1;
      } else {
        // 기존에 계산된 값이 있으면 -> 지금 고른 동전의 가치만큼 더하기 이전의 상태가 존재하는 경우에만
        dp[i] = Math.min(dp[i - coin] + 1, dp[i]);
      }
    }
  }
}

// 정답 출력
console.log(dp[k]);
