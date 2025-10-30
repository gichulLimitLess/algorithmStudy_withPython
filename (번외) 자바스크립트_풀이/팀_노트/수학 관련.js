// 최대공약수 구하기
function gcd(a, b) {
  while (b !== 0) {
    // b가 0이 될 때까지 반복 --> "유클리드 호제법" 사용
    const r = a % b; // 나머지를 구함
    a = b; // b를 a로
    b = r; // 나머지(r)을 b로 갱신
  }
  return a; // b가 0이 되면, 그 순간의 a가 GCD
}

console.log(gcd(24, 18));
console.log(gcd(18, 24)); // --> a가 b보다 크다고 가정 안해도 된다. (알아서 내부 연산에서 순서 조정되기 때문)

// 에라토스테네스의 체 (--> 소수 빠르게 구하기)
function aeratosthenes(end) {
  const isPrime = Array(end + 1)
    .fill(true)
    .fill(false, 0, 2); // 소수 판별
  for (let i = 2; i < Math.floor(Math.sqrt(end)) + 1; i++) {
    if (isPrime[i]) {
      // 소수라면
      j = 2;
      while (i * j <= end) {
        isPrime[i * j] = false;
        j += 1;
      }
    }
  }
  return isPrime
    .map((value, index) => {
      if (value) return index; // 소수인 것만 돌려준다
    })
    .filter((value) => value !== undefined);
}

console.log(aeratosthenes(10)); // [2, 3, 5, 7]

/*
  "에라토스테네스의 체" 알고리즘의 시간 복잡도는 O(NloglogN)
      -> 사실상 선형 시간에 가까울 정도로 매우 빠르다
      -> 하지만, 메모리가 많이 필요하다는 단점이 있다 (리스트 할당해야 되서..)
      -> 이 알고리즘을 이용해야 하는 문제에서는.. 보통 N이 100만 이내로 주어지는 경우가 많음
  ex) N = 100만, O(NloglogN) => 약 O(100만*4)
*/
