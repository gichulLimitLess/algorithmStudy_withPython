// 프로그래머스에서 돌려야 정상적으로 돌아가는 코드입니다.
// 링크: https://school.programmers.co.kr/learn/courses/30/lessons/258711

function solution(edges) {
  const ans = new Array(4).fill(0);
  const obj = {};
  let total = 0;

  // in/out degree 기록
  for (let [from, to] of edges) {
    if (!obj[from]) obj[from] = [0, 0]; // [out, in]
    if (!obj[to]) obj[to] = [0, 0];
    obj[from][0] += 1;
    obj[to][1] += 1;
  }

  // 각 노드의 구조적 역할 분석
  for (let key in obj) {
    const [outCnt, inCnt] = obj[key];

    // 8자형 그래프: in/out 둘 다 많음
    if (outCnt >= 2 && inCnt >= 2) ans[3]++;

    // 막대형 그래프: out=0
    if (outCnt === 0) ans[2]++;

    // 생성 노드 후보: in=0 && out>=2
    if (inCnt === 0 && outCnt >= 2) {
      ans[0] = Number(key);
      total = outCnt;
    }
  }

  // 도넛 그래프 수 계산
  ans[1] = total - ans[3] - ans[2];

  return ans;
}
