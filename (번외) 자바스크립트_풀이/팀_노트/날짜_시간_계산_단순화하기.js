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
