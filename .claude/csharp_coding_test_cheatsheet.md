# C# 코딩테스트 기초 문법 치트시트

> **대상**: C/C++ 경험자 (2년), Kotlin 경험자  
> **목표**: 프로그래머스 코딩테스트에서 메소드 구현에 필요한 C# 문법만 빠르게 습득  
> **전제**: 입출력은 신경 X, `solution` 메소드 내부 로직에만 집중

---

## 1. 기본 구조 (프로그래머스 기준)

프로그래머스는 보통 이런 틀로 주어집니다.

```csharp
using System;

public class Solution {
    public int solution(int[] arr, int k) {
        int answer = 0;
        // 여기에 로직 작성
        return answer;
    }
}
```

- `using System;` — C/C++의 `#include <iostream>` 같은 개념
- 자주 쓰는 추가 using: `using System.Collections.Generic;` (List, Dictionary 등), `using System.Linq;` (LINQ)
- 프로그래머스는 이 두 개를 기본으로 추가해주는 경우가 많지만, 없으면 직접 추가

---

## 2. 변수 선언 & 타입

```csharp
// 명시적 선언 (C/C++ 스타일)
int n = 10;
long big = 10000000000L;      // long은 리터럴 뒤에 L
double d = 3.14;
bool flag = true;              // Java/Kotlin과 동일 (C++의 bool)
char c = 'A';
string s = "hello";            // 소문자 string (C++의 std::string)

// 타입 추론 (Kotlin의 val/var 없음, 그냥 var)
var x = 10;                    // int로 추론
var list = new List<int>();    // 제네릭 길게 쓸 때 특히 유용

// 상수
const int MAX = 100;
```

### 숫자 변환
```csharp
int a = int.Parse("123");              // 문자열 → int (실패 시 예외)
int b;
bool ok = int.TryParse("123", out b);  // 안전한 변환
string s = 123.ToString();             // int → 문자열
double d = double.Parse("3.14");
```

---

## 3. 연산자 & 조건문

```csharp
// 연산자는 C/C++과 동일: + - * / % == != < > <= >= && || !
// 단, 정수 나눗셈 주의: 5 / 2 == 2

if (n > 0) {
    // ...
} else if (n == 0) {
    // ...
} else {
    // ...
}

// 삼항 연산자 (C와 동일)
int max = a > b ? a : b;

// switch (C와 유사하지만 break 필수)
switch (n) {
    case 1:
        Console.WriteLine("one");
        break;
    case 2:
    case 3:
        Console.WriteLine("two or three");
        break;
    default:
        Console.WriteLine("other");
        break;
}
```

---

## 4. 반복문

```csharp
// for (C 스타일 그대로)
for (int i = 0; i < n; i++) {
    // ...
}

// foreach (C++의 range-based for)
foreach (int x in arr) {
    // ...
}

// while / do-while (C와 동일)
while (condition) { ... }
do { ... } while (condition);

// break, continue 동일
```

---

## 5. 배열

```csharp
// 1차원 배열 (C의 배열과 비슷하지만 객체)
int[] arr = new int[10];               // 기본값 0으로 초기화
int[] arr2 = { 1, 2, 3, 4, 5 };        // 리터럴
int[] arr3 = new int[] { 1, 2, 3 };

arr.Length;                             // 길이 (메소드 아닌 프로퍼티, 괄호 X)
arr[0] = 5;

// 2차원 배열
int[,] grid = new int[3, 4];           // 3x4, 진짜 2차원
grid[0, 0] = 1;                         // 접근 방식 주의: [i, j]
int rows = grid.GetLength(0);          // 행 개수
int cols = grid.GetLength(1);          // 열 개수

// 가변 배열 (배열의 배열, C++의 vector<vector<int>>에 더 가까움)
int[][] jagged = new int[3][];
jagged[0] = new int[] { 1, 2 };
jagged[1] = new int[] { 3, 4, 5 };
// 접근: jagged[i][j], 길이: jagged[i].Length

// 배열 정렬
Array.Sort(arr);                        // 오름차순
Array.Reverse(arr);                     // 뒤집기 (내림차순 정렬 = Sort + Reverse)
Array.Sort(arr, (a, b) => b - a);      // 커스텀 정렬 (내림차순)
```

---

## 6. 자주 쓰는 자료구조

### List<T> — C++의 vector
```csharp
List<int> list = new List<int>();
list.Add(5);                           // push_back
list.Insert(0, 10);                    // 특정 위치 삽입
list.Remove(5);                        // 값으로 제거 (처음 찾은 것)
list.RemoveAt(0);                      // 인덱스로 제거
list.Count;                            // 크기 (Length 아님!)
list[0];                                // 인덱싱
list.Contains(5);                      // 포함 여부
list.IndexOf(5);                       // 인덱스 찾기 (없으면 -1)
list.Sort();                           // 정렬
list.Sort((a, b) => b - a);            // 내림차순
list.Reverse();
list.ToArray();                        // int[]로 변환

// 초기화
List<int> init = new List<int> { 1, 2, 3 };
```

### Dictionary<K, V> — C++의 unordered_map
```csharp
Dictionary<string, int> map = new Dictionary<string, int>();
map["apple"] = 3;                      // 추가/수정
map.Add("banana", 5);                  // 이미 있으면 예외
map.ContainsKey("apple");
map.Remove("apple");
map.Count;

// 안전한 조회
if (map.TryGetValue("apple", out int value)) {
    // value 사용
}

// 순회
foreach (var kv in map) {
    Console.WriteLine($"{kv.Key}: {kv.Value}");
}
foreach (var key in map.Keys) { ... }

// 카운팅 패턴 (자주 씀!)
if (!map.ContainsKey(key)) map[key] = 0;
map[key]++;
```

### HashSet<T> — C++의 unordered_set
```csharp
HashSet<int> set = new HashSet<int>();
set.Add(1);                            // 이미 있어도 예외 X, 그냥 false 반환
set.Contains(1);
set.Remove(1);
set.Count;

// 배열에서 중복 제거
var unique = new HashSet<int>(arr);
```

### Stack<T>
```csharp
Stack<int> stack = new Stack<int>();
stack.Push(1);
int top = stack.Pop();                 // 꺼내면서 반환
int peek = stack.Peek();               // 안 꺼내고 보기
stack.Count;
```

### Queue<T>
```csharp
Queue<int> queue = new Queue<int>();
queue.Enqueue(1);
int front = queue.Dequeue();
int peek = queue.Peek();
queue.Count;
```

### PriorityQueue<T, TPriority> — 우선순위 큐 (C++ priority_queue)
```csharp
// .NET 6+ 에서 사용 가능 (프로그래머스 최신 환경 OK)
var pq = new PriorityQueue<string, int>();
pq.Enqueue("A", 3);                    // (값, 우선순위) — 우선순위 숫자 작을수록 먼저
pq.Enqueue("B", 1);
pq.Enqueue("C", 2);

string first = pq.Dequeue();           // "B" (우선순위 1)
pq.Count;
pq.Peek();

// 최대 힙으로 쓰려면 우선순위에 -를 붙임
pq.Enqueue(val, -val);
```

---

## 7. 문자열

```csharp
string s = "hello world";

s.Length;                              // 길이 (프로퍼티)
s[0];                                  // 'h' (char)
s.Substring(0, 5);                     // "hello" (시작, 길이)
s.Substring(6);                        // "world" (시작부터 끝까지)
s.IndexOf("world");                    // 6 (없으면 -1)
s.Contains("world");
s.StartsWith("hello");
s.EndsWith("world");
s.Replace("world", "C#");              // "hello C#"
s.ToUpper();
s.ToLower();
s.Trim();                              // 앞뒤 공백 제거
s.Split(' ');                          // ["hello", "world"] (string[])
s.Split(',', ' ');                     // 여러 구분자

// 문자열 ↔ char 배열
char[] chars = s.ToCharArray();
string s2 = new string(chars);

// 문자열 합치기
string joined = string.Join(",", arr); // "1,2,3"
string joined2 = string.Join("", list);

// 문자열 보간 (Kotlin의 $)
int n = 5;
string msg = $"값은 {n}입니다";
string msg2 = $"합계: {a + b}";

// char 판별
char.IsDigit('5');                     // true
char.IsLetter('A');
char.IsUpper('A');
char.IsLower('a');
char.IsWhiteSpace(' ');

// char ↔ int
int num = '5' - '0';                   // 5 (C와 동일)
char c = (char)('a' + 3);              // 'd'
```

### StringBuilder — 문자열 많이 조작할 때
```csharp
// string은 불변이라 += 반복하면 성능 나쁨
var sb = new System.Text.StringBuilder();
sb.Append("hello");
sb.Append(' ');
sb.Append("world");
sb.AppendLine("!");                    // 줄바꿈 포함
string result = sb.ToString();
sb.Length;
sb.Clear();
```

---

## 8. LINQ — 써두면 진짜 편함

`using System.Linq;` 필요. 배열/List/컬렉션 위에서 체이닝 가능.

```csharp
int[] arr = { 3, 1, 4, 1, 5, 9, 2, 6 };

arr.Sum();                             // 31
arr.Max();                             // 9
arr.Min();                             // 1
arr.Average();                         // 3.875 (double)
arr.Count();                           // 8 (Length와 같음)
arr.Count(x => x > 3);                 // 조건 만족 개수: 3

// 필터 & 변환
arr.Where(x => x > 2).ToArray();       // [3, 4, 5, 9, 6]
arr.Select(x => x * 2).ToList();       // [6, 2, 8, 2, 10, 18, 4, 12]

// 정렬 (원본 변경 X, 새 시퀀스 반환)
arr.OrderBy(x => x).ToArray();                // 오름차순
arr.OrderByDescending(x => x).ToArray();      // 내림차순
arr.OrderBy(x => x.Length).ThenBy(x => x);   // 2차 정렬

// 중복 제거 & 기타
arr.Distinct().ToArray();
arr.Reverse();                                // 주의: IEnumerable 확장이라 .ToArray() 필요할 수 있음
arr.Take(3).ToArray();                        // 앞 3개
arr.Skip(3).ToArray();                        // 앞 3개 빼고
arr.First(x => x > 3);                        // 조건 만족 첫 원소
arr.Any(x => x > 10);                         // 하나라도 조건 만족?
arr.All(x => x > 0);                          // 전부 조건 만족?

// 그룹핑
var groups = arr.GroupBy(x => x % 2);         // 짝수/홀수로 그룹
foreach (var g in groups) {
    Console.WriteLine($"{g.Key}: {string.Join(",", g)}");
}
```

> **주의**: LINQ 결과는 대부분 `IEnumerable<T>`라서 배열/리스트로 바꾸려면 `.ToArray()`, `.ToList()`가 필요합니다.

---

## 9. 클래스 & 객체 (간단히)

```csharp
public class Point {
    public int X;                      // 필드 (public이면 외부에서 접근 가능)
    public int Y;
    
    public Point(int x, int y) {       // 생성자
        X = x;
        Y = y;
    }
    
    public int DistanceSq(Point other) {
        int dx = X - other.X;
        int dy = Y - other.Y;
        return dx * dx + dy * dy;
    }
}

// 사용
Point p = new Point(1, 2);
int d = p.DistanceSq(new Point(4, 6));

// 간단한 묶음이 필요할 때: 튜플도 좋음
(int x, int y) pos = (3, 4);
Console.WriteLine(pos.x);

// 리스트 안에 튜플
var points = new List<(int, int)>();
points.Add((1, 2));
foreach (var (x, y) in points) { ... }
```

---

## 10. 람다 & 함수형 문법

```csharp
// 람다 (Kotlin의 {} 대신 =>)
Func<int, int> square = x => x * x;            // int → int
Func<int, int, int> add = (a, b) => a + b;     // int, int → int
Action<string> print = s => Console.WriteLine(s); // 반환 없음

// 블록 람다
Func<int, int> f = x => {
    int r = x * 2;
    return r + 1;
};

// 정렬 커스텀
arr.OrderBy(x => x % 10);              // 일의 자리 기준
list.Sort((a, b) => a.CompareTo(b));   // 오름차순
list.Sort((a, b) => b - a);            // 내림차순 (정수일 때)
```

---

## 11. 자주 쓰는 유틸

```csharp
Math.Abs(-5);                          // 5
Math.Max(a, b);
Math.Min(a, b);
Math.Pow(2, 10);                       // double 반환! (1024.0)
Math.Sqrt(16);                         // 4.0
Math.Floor(3.7); Math.Ceiling(3.2); Math.Round(3.5);

// int.MaxValue, int.MinValue (무한대 대신)
int INF = int.MaxValue;
long LINF = long.MaxValue;
```

---

## 12. 디버깅 출력

```csharp
Console.WriteLine(x);                  // printf + \n
Console.WriteLine($"값: {x}, 합: {a+b}");
Console.Write(x);                      // 줄바꿈 없음

// 배열 찍기
Console.WriteLine(string.Join(", ", arr));
Console.WriteLine($"[{string.Join(",", list)}]");
```

---

## 13. C/C++/Kotlin 써본 사람이 잘 실수하는 포인트

| 실수 | 올바른 것 |
|---|---|
| `arr.length` | `arr.Length` (대문자, 프로퍼티) |
| `list.size()` | `list.Count` |
| `str.length()` | `str.Length` |
| `HashMap<K,V>` | `Dictionary<K,V>` |
| `map.get(k)` | `map[k]` 또는 `TryGetValue` |
| `new ArrayList<>()` | `new List<int>()` |
| `str.charAt(0)` | `str[0]` |
| 메소드 소문자 시작 | **C#은 메소드/프로퍼티 대문자 시작** (PascalCase) |
| `null` 바로 비교 | `obj != null` 또는 `obj is null` |
| `Math.pow`가 int 반환? | `Math.Pow`는 **double 반환**, 캐스팅 필요 |
| `5 / 2 == 2.5` | 정수끼리면 `2`, `5.0 / 2` 해야 `2.5` |

---

## 14. 템플릿 (내일 바로 쓸 뼈대)

### 기본
```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        
        // 로직
        
        return answer;
    }
}
```

### BFS 뼈대
```csharp
public int solution(int[,] grid) {
    int rows = grid.GetLength(0);
    int cols = grid.GetLength(1);
    bool[,] visited = new bool[rows, cols];
    
    var queue = new Queue<(int, int)>();
    queue.Enqueue((0, 0));
    visited[0, 0] = true;
    
    int[] dx = { -1, 1, 0, 0 };
    int[] dy = { 0, 0, -1, 1 };
    
    while (queue.Count > 0) {
        var (x, y) = queue.Dequeue();
        
        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];
            
            if (nx < 0 || ny < 0 || nx >= rows || ny >= cols) continue;
            if (visited[nx, ny]) continue;
            // 조건 체크
            
            visited[nx, ny] = true;
            queue.Enqueue((nx, ny));
        }
    }
    
    return 0;
}
```

### 카운팅 (Dictionary)
```csharp
public int solution(string[] words) {
    var count = new Dictionary<string, int>();
    foreach (var w in words) {
        if (!count.ContainsKey(w)) count[w] = 0;
        count[w]++;
    }
    
    // 가장 많이 나온 것
    var top = count.OrderByDescending(kv => kv.Value).First();
    return top.Value;
}
```

---

## 마지막 체크리스트 ✅

- [ ] `Length` / `Count` 구분 (배열/문자열 = Length, List/Dictionary = Count)
- [ ] 메소드/프로퍼티는 **대문자 시작**
- [ ] `Dictionary` 조회는 `TryGetValue` 또는 `ContainsKey` 체크
- [ ] LINQ 결과는 `.ToArray()` / `.ToList()` 로 마무리
- [ ] `Math.Pow`는 double 반환 (int 필요하면 `(int)` 캐스팅)
- [ ] 문자열 많이 조작하면 `StringBuilder`
- [ ] 정렬 커스텀: `(a, b) => a - b` (오름차순) / `b - a` (내림차순)

**화이팅! 예능이니까 즐기고 와요 🔥**
