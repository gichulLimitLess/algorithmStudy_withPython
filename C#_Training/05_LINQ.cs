using System;
using System.Collections.Generic;
using System.Linq;

class LINQPractice
{
    static void Main()
    {
        int[] arr = { 3, 1, 4, 1, 5, 9, 2, 6 };
        Console.WriteLine($"원본: [{string.Join(", ", arr)}]\n");

        // 집계 함수
        Console.WriteLine("=== 집계 ===");
        Console.WriteLine($"Sum: {arr.Sum()}");
        Console.WriteLine($"Max: {arr.Max()}");
        Console.WriteLine($"Min: {arr.Min()}");
        Console.WriteLine($"Average: {arr.Average()}");
        Console.WriteLine($"Count: {arr.Count()}");
        Console.WriteLine($"Count(x > 3): {arr.Count(x => x > 3)}");

        // Where (필터) & Select (변환)
        Console.WriteLine("\n=== Where & Select ===");
        int[] filtered = arr.Where(x => x > 3).ToArray();
        Console.WriteLine($"Where(x > 3): [{string.Join(", ", filtered)}]");

        int[] doubled = arr.Select(x => x * 2).ToArray();
        Console.WriteLine($"Select(x * 2): [{string.Join(", ", doubled)}]");

        // 체이닝: 3보다 큰 것만 골라서 2배
        int[] chained = arr.Where(x => x > 3).Select(x => x * 2).ToArray();
        Console.WriteLine($"Where(>3).Select(*2): [{string.Join(", ", chained)}]");

        // 정렬 (원본 변경 X)
        Console.WriteLine("\n=== OrderBy ===");
        int[] asc = arr.OrderBy(x => x).ToArray();
        Console.WriteLine($"오름차순: [{string.Join(", ", asc)}]");

        int[] desc = arr.OrderByDescending(x => x).ToArray();
        Console.WriteLine($"내림차순: [{string.Join(", ", desc)}]");

        // 2차 정렬 예시
        string[] names = { "Bob", "Alice", "Eve", "Ann", "Ada" };
        string[] sortedNames = names.OrderBy(x => x.Length).ThenBy(x => x).ToArray();
        Console.WriteLine($"\n이름 정렬 (길이 -> 사전순): [{string.Join(", ", sortedNames)}]");

        // Distinct, Take, Skip
        Console.WriteLine("\n=== Distinct, Take, Skip ===");
        int[] unique = arr.Distinct().ToArray();
        Console.WriteLine($"Distinct: [{string.Join(", ", unique)}]");

        int[] first3 = arr.Take(3).ToArray();
        Console.WriteLine($"Take(3): [{string.Join(", ", first3)}]");

        int[] skip3 = arr.Skip(3).ToArray();
        Console.WriteLine($"Skip(3): [{string.Join(", ", skip3)}]");

        // First, Any, All
        Console.WriteLine("\n=== First, Any, All ===");
        int firstBig = arr.First(x => x > 3);
        Console.WriteLine($"First(x > 3): {firstBig}");

        Console.WriteLine($"Any(x > 10): {arr.Any(x => x > 10)}");
        Console.WriteLine($"All(x > 0): {arr.All(x => x > 0)}");

        // GroupBy
        Console.WriteLine("\n=== GroupBy ===");
        var groups = arr.GroupBy(x => x % 2 == 0 ? "짝수" : "홀수");
        foreach (var g in groups)
        {
            Console.WriteLine($"  {g.Key}: [{string.Join(", ", g)}]");
        }

        // 실전 예시: 가장 자주 나오는 원소
        Console.WriteLine("\n=== 실전: 최빈값 찾기 ===");
        int[] data = { 1, 3, 2, 3, 1, 3, 2, 1, 1 };
        var mode = data.GroupBy(x => x)
                       .OrderByDescending(g => g.Count())
                       .First();
        Console.WriteLine($"데이터: [{string.Join(", ", data)}]");
        Console.WriteLine($"최빈값: {mode.Key} ({mode.Count()}번)");

        // 실전 예시: 배열에서 상위 3개 합
        Console.WriteLine("\n=== 실전: 상위 3개 합 ===");
        int top3Sum = arr.OrderByDescending(x => x).Take(3).Sum();
        Console.WriteLine($"상위 3개 합: {top3Sum}  (9+6+5 = 20)");
    }
}
