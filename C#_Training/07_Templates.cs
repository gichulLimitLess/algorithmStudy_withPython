using System;
using System.Collections.Generic;
using System.Linq;

class Templates
{
    // ===== BFS 템플릿 =====
    static int BFS(int[,] grid)
    {
        int rows = grid.GetLength(0);
        int cols = grid.GetLength(1);
        bool[,] visited = new bool[rows, cols];

        var queue = new Queue<(int r, int c, int dist)>();
        queue.Enqueue((0, 0, 0));
        visited[0, 0] = true;

        int[] dr = { -1, 1, 0, 0 };
        int[] dc = { 0, 0, -1, 1 };

        while (queue.Count > 0)
        {
            var (r, c, dist) = queue.Dequeue();

            // 도착 조건
            if (r == rows - 1 && c == cols - 1)
                return dist;

            for (int d = 0; d < 4; d++)
            {
                int nr = r + dr[d];
                int nc = c + dc[d];

                if (nr < 0 || nc < 0 || nr >= rows || nc >= cols) continue;
                if (visited[nr, nc]) continue;
                if (grid[nr, nc] == 0) continue;  // 0은 벽

                visited[nr, nc] = true;
                queue.Enqueue((nr, nc, dist + 1));
            }
        }

        return -1;  // 도달 불가
    }

    // ===== DFS 템플릿 (재귀) =====
    static bool[,] dfsVisited;
    static int[,] dfsGrid;
    static int component = 0;

    static void DFS(int r, int c)
    {
        int rows = dfsGrid.GetLength(0);
        int cols = dfsGrid.GetLength(1);
        dfsVisited[r, c] = true;
        component++;

        int[] dr = { -1, 1, 0, 0 };
        int[] dc = { 0, 0, -1, 1 };

        for (int d = 0; d < 4; d++)
        {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr < 0 || nc < 0 || nr >= rows || nc >= cols) continue;
            if (dfsVisited[nr, nc]) continue;
            if (dfsGrid[nr, nc] == 0) continue;

            DFS(nr, nc);
        }
    }

    // ===== 카운팅 (Dictionary) 템플릿 =====
    static string MostFrequent(string[] words)
    {
        var count = new Dictionary<string, int>();
        foreach (var w in words)
        {
            if (!count.ContainsKey(w)) count[w] = 0;
            count[w]++;
        }

        var top = count.OrderByDescending(kv => kv.Value).First();
        return $"\"{top.Key}\" ({top.Value}번)";
    }

    // ===== 이진 탐색 템플릿 =====
    static int BinarySearch(int[] arr, int target)
    {
        int left = 0, right = arr.Length - 1;

        while (left <= right)
        {
            int mid = left + (right - left) / 2;

            if (arr[mid] == target) return mid;
            else if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }

        return -1;  // 못 찾음
    }

    static void Main()
    {
        // BFS 테스트
        Console.WriteLine("=== BFS: 최단 경로 ===\n");
        int[,] maze = {
            { 1, 1, 0, 1 },
            { 0, 1, 0, 1 },
            { 0, 1, 1, 1 },
            { 0, 0, 0, 1 }
        };
        Console.WriteLine("미로 (1=길, 0=벽):");
        for (int i = 0; i < maze.GetLength(0); i++)
        {
            for (int j = 0; j < maze.GetLength(1); j++)
                Console.Write($"{maze[i, j]} ");
            Console.WriteLine();
        }
        int dist = BFS(maze);
        Console.WriteLine($"(0,0) -> (3,3) 최단 거리: {dist}\n");

        // DFS 테스트: 섬 개수 세기
        Console.WriteLine("=== DFS: 섬 개수 세기 ===\n");
        dfsGrid = new int[,] {
            { 1, 1, 0, 0, 1 },
            { 1, 0, 0, 1, 1 },
            { 0, 0, 0, 0, 0 },
            { 1, 0, 1, 1, 0 },
            { 1, 0, 0, 1, 0 }
        };

        int rows = dfsGrid.GetLength(0);
        int cols = dfsGrid.GetLength(1);
        dfsVisited = new bool[rows, cols];
        int islands = 0;

        Console.WriteLine("지도 (1=땅, 0=바다):");
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
                Console.Write($"{dfsGrid[i, j]} ");
            Console.WriteLine();
        }

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if (dfsGrid[i, j] == 1 && !dfsVisited[i, j])
                {
                    component = 0;
                    DFS(i, j);
                    islands++;
                    Console.WriteLine($"  섬 #{islands} 발견 (크기: {component})");
                }
            }
        }
        Console.WriteLine($"총 섬 개수: {islands}\n");

        // 카운팅 테스트
        Console.WriteLine("=== 카운팅: 최빈값 ===\n");
        string[] words = { "apple", "banana", "apple", "cherry", "banana", "apple" };
        Console.WriteLine($"단어들: [{string.Join(", ", words)}]");
        Console.WriteLine($"최빈값: {MostFrequent(words)}\n");

        // 이진 탐색 테스트
        Console.WriteLine("=== 이진 탐색 ===\n");
        int[] sorted = { 1, 3, 5, 7, 9, 11, 13 };
        Console.WriteLine($"배열: [{string.Join(", ", sorted)}]");
        Console.WriteLine($"BinarySearch(7): index {BinarySearch(sorted, 7)}");
        Console.WriteLine($"BinarySearch(4): index {BinarySearch(sorted, 4)}");
    }
}
