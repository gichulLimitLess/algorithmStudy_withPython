using System;

class Variables
{
    static void Main()
    {
        Console.WriteLine("=== 1. 변수 선언 & 타입 ===\n");

        // 명시적 선언
        int n = 10;
        long big = 10000000000L;
        double d = 3.14;
        bool flag = true;
        char c = 'A';
        string s = "hello";

        Console.WriteLine($"int: {n}, long: {big}, double: {d}");
        Console.WriteLine($"bool: {flag}, char: {c}, string: {s}");

        // var 타입 추론
        var x = 42;
        var msg = "타입 추론!";
        Console.WriteLine($"\nvar x = {x} (타입: {x.GetType()})");
        Console.WriteLine($"var msg = {msg} (타입: {msg.GetType()})");

        // 상수
        const int MAX = 100;
        Console.WriteLine($"\nconst MAX = {MAX}");

        // 숫자 변환
        Console.WriteLine("\n=== 숫자 변환 ===");
        int a = int.Parse("123");
        Console.WriteLine($"int.Parse(\"123\") = {a}");

        int b;
        bool ok = int.TryParse("abc", out b);
        Console.WriteLine($"int.TryParse(\"abc\") -> ok={ok}, b={b}");

        ok = int.TryParse("456", out b);
        Console.WriteLine($"int.TryParse(\"456\") -> ok={ok}, b={b}");

        string numStr = 789.ToString();
        Console.WriteLine($"789.ToString() = \"{numStr}\"");

        // 연산자 주의사항
        Console.WriteLine("\n=== 연산자 주의 ===");
        Console.WriteLine($"5 / 2 = {5 / 2}        (정수 나눗셈 -> 2)");
        Console.WriteLine($"5.0 / 2 = {5.0 / 2}    (실수 나눗셈 -> 2.5)");
        Console.WriteLine($"5 % 3 = {5 % 3}        (나머지 -> 2)");

        // 삼항 연산자
        int val = 7;
        string result = val > 5 ? "크다" : "작거나 같다";
        Console.WriteLine($"\n{val} > 5 ? -> {result}");

        // switch
        Console.WriteLine("\n=== switch ===");
        int num = 2;
        switch (num)
        {
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
    }
}
