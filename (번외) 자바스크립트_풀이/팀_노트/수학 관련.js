// 최대공약수 구하기
function gcd(a, b) {
  while (b !== 0) {
    // b가 0이 될 때까지 반복
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
