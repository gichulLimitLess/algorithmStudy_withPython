/*
  '정렬된 리스트'에서..
    --> 값이 특정 범위에 속하는 원소의 개수 구하기
    --> JS 에서는 "이분탐색"을 통해 직접 찾아야 함
    --> bisect_left()와 bisect_right()를 적절히 활용해서 count_by_range() 함수.. 아래처럼 쉽게 구현 가능
*/

// 아래쪽(왼쪽) 인덱스 찾기 (Python에서의 bisect_left)
function lowerBound(arr, target) {
  let start = 0;
  // 여기에서, end를 arr.length로 설정 함으로서 target이 "존재하지 않는다"를 의미할 수 있음
  let end = arr.length;
  while (start < end) {
    const mid = Math.floor((start + end) / 2);
    if (arr[mid] >= target) {
      // arr[mid]가 target보다 크거나 같다면, 계속해서 end를 mid 값으로 갱신
      end = mid;
    } else {
      start = mid + 1;
    }
  }
  return start;
}

// 위쪽(오른쪽) 인덱스 찾기 (Python에서 bisect_right)
function upperBound(arr, target) {
  let start = 0;
  let end = arr.length;
  while (start < end) {
    const mid = Math.floor((start + end) / 2);
    if (arr[mid] > target) {
      // arr[mid]가 target보다 크다면, 계속해서 end를 mid 값으로 갱신
      // --> 이렇게 하면, end는 결과적으로 target 맨 오른쪽 index의 바로 다음 인덱스 가리킬 것임
      end = mid;
    } else {
      start = mid + 1;
    }
  }
  return start;
}

// 범위를 이용해서 개수 세는 함수 --> "정렬된" 리스트여야 함
function count_by_range(arr, target) {
  const left = lowerBound(arr, target);
  const right = upperBound(arr, target);
  if (left === right) {
    // 이 경우는, 없는 경우 --> 하나라도 있으면, 차이가 나거든
    return [-1, -1];
  }
  return [left, right - 1]; // [왼쪽, 오른쪽]
}

// 테스트 -> 우선 오름차순 정렬
const num_list = [1, 2, 9, 10, 2, 2, 3, 3, 5].sort((a, b) => a - b);
console.log(num_list); // [1, 2, 2, 2, 3, 3, 5, 9, 10]
const [left, right] = count_by_range(num_list, 2); // "정렬된 리스트"에서 2의 양 끝 인덱스 찾기
console.log("왼쪽: ", left, "오른쪽: ", right); // 결과: "왼쪽: 1, 오른쪽: 3"

const [left2, right2] = count_by_range(num_list, 11); // "정렬된 리스트"에서 11의 양 끝 인덱스 찾기
console.log("왼쪽: ", left2, "오른쪽: ", right2); // 결과: "왼쪽: -1, 오른쪽: -1"
