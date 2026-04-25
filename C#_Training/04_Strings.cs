using System;
using System.Text;

class Strings
{
    static void Main()
    {
        Console.WriteLine("=== 문자열 기본 ===\n");

        string s = "hello world";
        Console.WriteLine($"원본: \"{s}\"");
        Console.WriteLine($"Length: {s.Length}");
        Console.WriteLine($"s[0]: '{s[0]}'");

        Console.WriteLine($"Substring(0,5): \"{s.Substring(0, 5)}\"");
        Console.WriteLine($"Substring(6): \"{s.Substring(6)}\"");
        Console.WriteLine($"IndexOf(\"world\"): {s.IndexOf("world")}");
        Console.WriteLine($"Contains(\"world\"): {s.Contains("world")}");
        Console.WriteLine($"StartsWith(\"hello\"): {s.StartsWith("hello")}");
        Console.WriteLine($"EndsWith(\"world\"): {s.EndsWith("world")}");

        Console.WriteLine($"Replace: \"{s.Replace("world", "C#")}\"");
        Console.WriteLine($"ToUpper: \"{s.ToUpper()}\"");
        Console.WriteLine($"ToLower: \"{s.ToLower()}\"");

        string padded = "  hello  ";
        Console.WriteLine($"Trim: \"{padded.Trim()}\"");

        // Split & Join
        Console.WriteLine("\n=== Split & Join ===");
        string csv = "apple,banana,cherry";
        string[] parts = csv.Split(',');
        Console.WriteLine($"Split: [{string.Join(" | ", parts)}]");
        Console.WriteLine($"Join: \"{string.Join(" - ", parts)}\"");

        // char 배열 변환
        Console.WriteLine("\n=== char[] 변환 ===");
        char[] chars = "abcde".ToCharArray();
        Array.Reverse(chars);
        string reversed = new string(chars);
        Console.WriteLine($"\"abcde\" 뒤집기: \"{reversed}\"");

        // 문자열 보간
        Console.WriteLine("\n=== 문자열 보간 ($) ===");
        int a = 10, b = 20;
        Console.WriteLine($"{a} + {b} = {a + b}");

        // char 판별
        Console.WriteLine("\n=== char 판별 ===");
        char[] testChars = { '5', 'A', 'z', ' ', '!' };
        foreach (char c in testChars)
        {
            Console.WriteLine($"  '{c}' -> Digit:{char.IsDigit(c)}, Letter:{char.IsLetter(c)}, Upper:{char.IsUpper(c)}, Lower:{char.IsLower(c)}, Space:{char.IsWhiteSpace(c)}");
        }

        // char <-> int
        Console.WriteLine("\n=== char <-> int ===");
        int num = '7' - '0';
        Console.WriteLine($"'7' - '0' = {num}");
        char letter = (char)('a' + 3);
        Console.WriteLine($"(char)('a' + 3) = '{letter}'");

        // StringBuilder
        Console.WriteLine("\n=== StringBuilder ===");
        var sb = new StringBuilder();
        sb.Append("hello");
        sb.Append(' ');
        sb.Append("world");
        sb.AppendLine("!");
        sb.Append("StringBuilder는 문자열을 많이 조작할 때 성능이 좋습니다.");
        Console.WriteLine(sb.ToString());
        Console.WriteLine($"Length: {sb.Length}");

        // 실전 예시: 문자열에서 숫자만 추출
        Console.WriteLine("\n=== 실전: 숫자만 추출 ===");
        string mixed = "abc123def456";
        var digits = new StringBuilder();
        foreach (char c in mixed)
        {
            if (char.IsDigit(c))
                digits.Append(c);
        }
        Console.WriteLine($"\"{mixed}\" -> \"{digits}\"");
    }
}
