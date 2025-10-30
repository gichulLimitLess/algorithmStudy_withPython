// JS 입출력용 구문
const fs = require("fs");
const path = require("path");

const filePath = process.platform === "linux" ? "/dev/stdin" : path.join(__dirname, "input.txt");

const input = fs.readFileSync(filePath).toString().trim().split("\n");

/*
--> 해당 Query가 팰린드롬인 경우에는 1, 아닌 경우에는 0 출력
  [펠린드롬?]
  -> n이 최대 2000, 각 질문마다 펠린드롬인지 일일이 확인하면.. 최대 O(N*M = 20억) / 당연히 시간 터짐
  --> 이럴 때 쓰는거? DP!
  --> DP로 풀기 위해서는 먼저.. 상태 정의 & 점화식 설정!

  <상태 정의>
  dp[i][j] = i번째 수부터 j번째까지 수가 팰린드롬인지 여부 저장 (팰린드롬: 1, 아니면: 0)
*/

// 입력 받기
const n = Number(input[0]); // 수열 크기 n
const num_list = input[1].split(" ").map(Number); // 수열 정보
const m = Number(input[2]); // 질문의 개수 m

const dp = Array.from(Array(n), () => Array(n).fill(0));

// 1개짜리는 자기 자신이 그냥 팰린드롬
for (let i = 0; i < n; i++) {
  dp[i][i] = 1;
}

// 2개짜리는 앞뒤가 같으면 팰린드롬, 아니면 0
for (let i = 0; i < n - 1; i++) {
  if (num_list[i] === num_list[i + 1]) {
    dp[i][i + 1] = 1;
  }
}

/*
  3개짜리부터는, 자기 중간에 있는 sub 수열이 팰린드롬이고, 양 끝이 같은 놈이어야 팰린드롬
  ex) 
  if num_list[i] == num_list[j] and dp[i-1][j-1] == 1:
    dp[i][j] = 1
  else:
    dp[i][j] = 0
  --> i를 0,1,2 순으로 순회하면.. 아직 채워지지 않은 dp[i+1][j-1] 값을 참조하게 됨
    -> i의 전이 순서를 반대로 돌려야 함!
*/
for (let i = n - 3; i >= 0; i--) {
  // 시작점 관련
  for (let j = i + 2; j < n; j++) {
    // 끝점 관련
    // --> 자기 중간에 있는 sub 수열이 팰린드롬이고, 양 끝 값이 같은 놈이여야 팰린드롬
    if (num_list[i] === num_list[j] && dp[i + 1][j - 1] === 1) {
      dp[i][j] = 1;
    } else {
      // 아니면 팰린드롬 아님
      dp[i][j] = 0;
    }
  }
}

// JS에서는 출력을 빠르게 해줘야 한다 (--> Python에서 print() 일일이 찍었던 거랑은 다른 느낌으로 가야 함)
let output = "";
for (let i = 3; i < m + 3; i++) {
  // 질문의 개수만큼 쿼리 수행
  const [s, e] = input[i].split(" ").map(Number);
  output += dp[s - 1][e - 1] + "\n"; // 답 바로 출력 (--> dp 테이블에서 꺼내온다)
}

console.log(output.trim()); // 한 번에 출력한다
