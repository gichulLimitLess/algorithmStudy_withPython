// 프로그래머스에서 돌려야 정상적으로 돌아가는 코드입니다.
// 링크: https://school.programmers.co.kr/learn/courses/30/lessons/340211

/*
    운송 포인트 n개의 좌표를 담은 2차원 정수 배열 points
    로봇 x대의 운송 경로를 담은 2차원 정수 배열 routes
    Q. 모든 로봇이 운송을 마칠 때까지 발생하는 위험한 상황의 횟수?
*/
function solution(points, routes) {
  // 각 로봇의 시간별 위치를 저장할 history 배열 생성
  const history = Array.from(Array(routes.length), () => []);
  routes.forEach((route, idx) => {
    for (let i = 0; i < route.length - 1; i++) {
      // 각 로봇의 운송 경로를 보면서 작업 수행
      let [now_y, now_x] = points[route[i] - 1];
      let [nxt_y, nxt_x] = points[route[i + 1] - 1];
      /*
                세로축부터 이동을 수행해야 함
                세로축이 목표점에 도달했다면, 그때 가로축 좌표를 바꾸는 식으로
            */
      while (now_y != nxt_y) {
        if (now_y < nxt_y) {
          // 목표 포인트의 y좌표보다 현재가 작다면
          history[idx].push([now_y++, now_x]);
        } else if (now_y > nxt_y) {
          // 목표 포인트의 y좌표보다 현재가 크다면
          history[idx].push([now_y--, now_x]);
        }
      }
      while (now_x != nxt_x) {
        if (now_x < nxt_x) {
          // 목표 포인트의 x좌표보다 현재가 더 작다면
          history[idx].push([now_y, now_x++]);
        } else if (now_x > nxt_x) {
          // 목표 포인트의 y좌표보다 현재가 크다면
          history[idx].push([now_y, now_x--]);
        }
      }
    }
    // 위의 반복문 수행하면, 최종 목적지의 좌표 하나가 누락된다 --> 넣어준다
    let [last_y, last_x] = points[route.at(-1) - 1];
    history[idx].push([last_y, last_x]);
  });

  // 각 로봇에 대한 경로 history 길이 중, 길이가 가장 긴 것을 기준으로 잡고 반복문 수행
  let idx = 0;
  let answer = 0;
  let maxIdx = 0;
  history.forEach((element) => {
    // forEach문 돌면서, 가장 긴 친구에 대해서 인덱스 업데이트 해야 한다
    maxIdx = Math.max(maxIdx, element.length);
  });
  while (idx < maxIdx) {
    const check_map = new Map();
    for (const e of history) {
      // history 하나씩 보면서, 같은 시간대에 같은 좌표가 있나 확인
      // console.log("현재: ", e[idx], "현재 idx: ", idx);
      if (idx > e.length - 1) continue; // 검사할 필요 없는 경우
      if (check_map.has(e[idx].join(","))) {
        // 중복되는 거 있으면
        check_map.set(e[idx].join(","), check_map.get(e[idx].join(",")) + 1);
      } else {
        check_map.set(e[idx].join(","), 1);
      }
    }
    for (const value of check_map.values()) {
      if (value > 1) {
        // 중복되는 경우 (-> 한번의 시간에 중복되는 경우가 여러 개 있을 수 있으므로, 이런 식으로 찾아야 한다)
        answer++; // 중복되는 경우 +1
      }
    }
    idx++; // 비교할 idx++ 해준다
  }

  return answer; // 위험 상황의 횟수 return
}
