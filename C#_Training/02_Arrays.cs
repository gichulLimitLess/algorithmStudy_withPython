using System;
using System.Linq;

class Arrays
{
    static void Main()
    {
        Console.WriteLine("=== 1차원 배열 ===\n");

        int[] arr = new int[5];  // 기본값 0
        Console.WriteLine($"new int[5] -> [{string.Join(", ", arr)}]");

        int[] arr2 = { 3, 1, 4, 1, 5, 9 };
        Console.WriteLine($"리터럴 배열 -> [{string.Join(", ", arr2)}]");
        Console.WriteLine($"arr2.Length = {arr2.Length}");
        Console.WriteLine($"arr2[0] = {arr2[0]}, arr2[5] = {arr2[5]}");

        // 정렬
        Console.WriteLine("\n=== 배열 정렬 ===");
        int[] sorted = (int[])arr2.Clone();  // 원본 보존용 복사
        Array.Sort(sorted);
        Console.WriteLine($"오름차순: [{string.Join(", ", sorted)}]");

        Array.Reverse(sorted);
        Console.WriteLine($"Reverse:  [{string.Join(", ", sorted)}]");

        int[] custom = (int[])arr2.Clone();
        Array.Sort(custom, (a, b) => b - a);  // 커스텀 내림차순
        Console.WriteLine($"커스텀 내림차순: [{string.Join(", ", custom)}]");

        // 2차원 배열
        Console.WriteLine("\n=== 2차원 배열 (int[,]) ===");
        int[,] grid = new int[3, 4];
        grid[0, 0] = 1;
        grid[1, 2] = 5;
        grid[2, 3] = 9;

        int rows = grid.GetLength(0);
        int cols = grid.GetLength(1);
        Console.WriteLine($"크기: {rows} x {cols}");

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                Console.Write($"{grid[i, j],3}");
            }
            Console.WriteLine();
        }

        // 가변 배열 (jagged)
        Console.WriteLine("\n=== 가변 배열 (int[][]) ===");
        int[][] jagged = new int[3][];
        jagged[0] = new int[] { 1, 2 };
        jagged[1] = new int[] { 3, 4, 5 };
        jagged[2] = new int[] { 6 };

        for (int i = 0; i < jagged.Length; i++)
        {
            Console.WriteLine($"jagged[{i}] (길이 {jagged[i].Length}): [{string.Join(", ", jagged[i])}]");
        }

        // foreach 반복
        Console.WriteLine("\n=== foreach ===");
        foreach (int x in arr2)
        {
            Console.Write($"{x} ");
        }
        Console.WriteLine();
    }
}
