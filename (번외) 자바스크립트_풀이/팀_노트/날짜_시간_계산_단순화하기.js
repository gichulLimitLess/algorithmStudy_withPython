/*
    1. 시간(HH:MM) 계산 기본형
    --> 문자열 시간 차이를 계산할 때는 반드시 '분 단위'로 변환하라
    [팁]
    - 무조건 split(':')로 파싱
    - 뺄셈 결과가 음수일 가능성이 있으면 abs() 고려
    - 23:59 기준 보정 시 23*60+59 = 1439 활용
*/
function to_minutes(time_str) {
  // 'HH:MM' 문자열을 분 단위로 변환
  const [h, m] = time_str.split(":").map(Number);
  return h * 60 + m;
}

function diff_minutes(t1, t2) {
  // 시간 차이 계산 (단위: 분)
  return Math.abs(to_minutes(t1) - to_minutes(t2));
}

// 예시
console.log(diff_minutes("05:34", "07:59")); // 결과: 145(분)

/*
    2. 날짜(YYYY-MM-DD) 계산 기본형
    --> "윤년 제외 / 매달 30일" 문제에서 자주 쓰이는 형태
    [팁]
    - "날짜 차이" 문제에서 datetime 대신 이거 쓰면 안전
    - 시간 제한 1초 내에서 O(1) 계산
    - abs() 써서 순서 무관하게 처리 가능
*/

function to_days(date_str) {
  // 'YYYY-MM-DD' 문자열을 총 일수로 변환 (윤년 제외, 매달 30일)
  const [y, m, d] = date_str.split("-").map(Number);
  return y * 360 + m * 30 + d;
}

function diff_days(d1, d2) {
  return Math.abs(to_days(d1) - to_days(d2));
}

// 예시
console.log(diff_days("2025-01-01", "2025-01-11")); // 결과: 10(일)

/*
  3. 달별 일수 고려(윤년 제외) 버전
    --> 날짜가 조금 더 현실적으로 주어질 때 (ex. 1월~12월 실제 일수)
    [팁]
    - 윤년을 고려하지 않아도, 실제 문제에서는 대부분 이 정도까지만 요구
    - sum()은 O(12) -> 사실상 O(1)
    - 코테에 "윤년 무시" 명시되어 있으면 아래 코드 그대로 써도 된다
*/

function to_days_real(date_str) {
  const [y, m, d] = date_str.split("-").map(Number);
  const month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  let m_acc_days = 0;
  for (let i = 0; i < m - 1; i++) {
    // 코드가 조금 길어 지더라도, 내겐 이게 더 직관적이다 (특히 이 경우엔!)
    // reduce()는 빈 배열의 경우 오류가 뜨니까 이게 더 명확한 표현일 수 있다!
    m_acc_days += month_days[i];
  }

  return y * 360 + m_acc_days + d;
}

function diff_days_real(d1, d2) {
  return Math.abs(to_days_real(d2) - to_days_real(d1));
}

// 예시
console.log(diff_days_real("2025-01-01", "2025-03-01")); // 결과: 59(일)

/*
  4. 시간 + 날짜 복합형 (ex. 주차장, 근무시간, 로그 누적)
    --> 날짜/시간 둘 다 문자열로 주어지는 복합 시뮬레이션 문제에서 유용
    [활용 포인트]
    - 날짜가 넘어가는 시간 계산에 완벽하게 대응 (ex. "23:59 ~ 00:10")
    - 주차요금, 출퇴근 기록, 장비 작동 시간 등 시뮬레이션 문제에 매우 유용
*/
function to_minutes_full(datetime_str) {
  const [date, time] = datetime_str.split(" ");
  const [y, m, d] = date.split("-").map(Number);
  const [h, min] = time.split(":").map(Number);

  // 하루는 24 * 60 === 1440분
  return (y * 360 + m * 30 + d) * 1440 + h * 60 + min; // 단위는 "분"
}

function diff_minutes_full(d1, d2) {
  return Math.abs(to_minutes_full(d2) - to_minutes_full(d1));
}

// 예시
console.log(diff_minutes_full("2025-10-08 23:59", "2025-10-09 00:10")); // 결과: 11(분)

/*
  [최종 정리]
    날짜/시간 문제 = 문자열 파싱 + 단위 통일 + 조건 경계 처리
    1. 문자열을 수 단위(분/일)로 변환해라
    2. 경계값(23:59, 00:00)은 항상 엣지케이스로 확인해라
    3. "윤년 무시/매달 30일"은 계산 단순화의 신호다 -> 수식화로 접근해라
*/
