using System;
using System.Collections.Generic;

class LambdaAndUtils
{
    static void Main()
    {
        // ===== 람다 =====
        Console.WriteLine("=== 람다 ===\n");

        Func<int, int> square = x => x * x;
        Func<int, int, int> add = (a, b) => a + b;
        Action<string> print = s => Console.WriteLine($"  > {s}");

        Console.WriteLine($"square(5) = {square(5)}");
        Console.WriteLine($"add(3, 7) = {add(3, 7)}");
        print("Action은 반환값 없는 람다!");

        // 블록 람다
        Func<int, int> transform = x =>
        {
            int r = x * 2;
            return r + 1;
        };
        Console.WriteLine($"transform(10) = {transform(10)}");

        // 정렬에 람다 활용
        Console.WriteLine("\n=== 정렬 + 람다 ===");
        var items = new List<(string name, int score)>
        {
            ("Alice", 85),
            ("Bob", 92),
            ("Charlie", 78),
            ("Diana", 92),
            ("Eve", 85)
        };

        // 점수 내림차순, 같으면 이름 오름차순
        items.Sort((a, b) =>
        {
            if (a.score != b.score) return b.score - a.score;
            return a.name.CompareTo(b.name);
        });

        Console.WriteLine("점수 내림차순 (같으면 이름순):");
        foreach (var (name, score) in items)
            Console.WriteLine($"  {name}: {score}");

        // ===== Math 유틸 =====
        Console.WriteLine("\n=== Math 유틸 ===\n");

        Console.WriteLine($"Math.Abs(-5) = {Math.Abs(-5)}");
        Console.WriteLine($"Math.Max(3, 7) = {Math.Max(3, 7)}");
        Console.WriteLine($"Math.Min(3, 7) = {Math.Min(3, 7)}");
        Console.WriteLine($"Math.Pow(2, 10) = {Math.Pow(2, 10)}  (double!)");
        Console.WriteLine($"(int)Math.Pow(2, 10) = {(int)Math.Pow(2, 10)}  (int 캐스팅)");
        Console.WriteLine($"Math.Sqrt(16) = {Math.Sqrt(16)}");
        Console.WriteLine($"Math.Floor(3.7) = {Math.Floor(3.7)}");
        Console.WriteLine($"Math.Ceiling(3.2) = {Math.Ceiling(3.2)}");
        Console.WriteLine($"Math.Round(3.5) = {Math.Round(3.5)}");
        Console.WriteLine($"Math.Round(4.5) = {Math.Round(4.5)}  (은행원 반올림 주의!)");

        // int.MaxValue / MinValue
        Console.WriteLine($"\nint.MaxValue = {int.MaxValue}");
        Console.WriteLine($"int.MinValue = {int.MinValue}");
        Console.WriteLine($"long.MaxValue = {long.MaxValue}");

        // ===== 튜플 =====
        Console.WriteLine("\n=== 튜플 ===\n");

        (int x, int y) pos = (3, 4);
        Console.WriteLine($"pos = ({pos.x}, {pos.y})");

        // 리스트 안에 튜플 (코딩테스트에서 좌표 저장 등에 자주 사용)
        var points = new List<(int x, int y)>();
        points.Add((1, 2));
        points.Add((3, 4));
        points.Add((5, 6));

        Console.WriteLine("좌표들:");
        foreach (var (px, py) in points)
            Console.WriteLine($"  ({px}, {py})");

        // ===== 디버깅 출력 팁 =====
        Console.WriteLine("\n=== 디버깅 출력 ===\n");

        int[] arr = { 1, 2, 3, 4, 5 };
        Console.WriteLine($"배열: [{string.Join(", ", arr)}]");

        var list = new List<int> { 10, 20, 30 };
        Console.WriteLine($"리스트: [{string.Join(", ", list)}]");

        var dict = new Dictionary<string, int> { ["a"] = 1, ["b"] = 2 };
        Console.WriteLine("딕셔너리:");
        foreach (var kv in dict)
            Console.WriteLine($"  {kv.Key}: {kv.Value}");
    }
}
