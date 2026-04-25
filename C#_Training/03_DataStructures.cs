using System;
using System.Collections.Generic;
using System.Linq;

class DataStructures
{
    static void Main()
    {
        // ===== List<T> =====
        Console.WriteLine("=== List<T> (Python의 list, C++의 vector) ===\n");

        List<int> list = new List<int> { 10, 20, 30 };
        list.Add(40);           // 끝에 추가
        list.Insert(0, 5);      // 맨 앞에 5 삽입
        Console.WriteLine($"Add/Insert 후: [{string.Join(", ", list)}]");

        list.Remove(20);        // 값 20 제거
        list.RemoveAt(0);       // 인덱스 0 제거
        Console.WriteLine($"Remove 후: [{string.Join(", ", list)}]");
        Console.WriteLine($"Count: {list.Count}, Contains(30): {list.Contains(30)}");
        Console.WriteLine($"IndexOf(30): {list.IndexOf(30)}, IndexOf(99): {list.IndexOf(99)}");

        list.Sort();
        Console.WriteLine($"Sort: [{string.Join(", ", list)}]");
        list.Sort((a, b) => b - a);
        Console.WriteLine($"내림차순: [{string.Join(", ", list)}]");

        int[] asArray = list.ToArray();
        Console.WriteLine($"ToArray: [{string.Join(", ", asArray)}]");

        // ===== Dictionary<K,V> =====
        Console.WriteLine("\n=== Dictionary<K,V> (Python의 dict) ===\n");

        var map = new Dictionary<string, int>();
        map["apple"] = 3;
        map["banana"] = 5;
        map["cherry"] = 2;

        Console.WriteLine($"map[\"apple\"] = {map["apple"]}");
        Console.WriteLine($"ContainsKey(\"banana\"): {map.ContainsKey("banana")}");
        Console.WriteLine($"Count: {map.Count}");

        // TryGetValue - 안전한 조회
        if (map.TryGetValue("cherry", out int val))
            Console.WriteLine($"TryGetValue(\"cherry\"): {val}");

        if (!map.TryGetValue("grape", out int val2))
            Console.WriteLine($"TryGetValue(\"grape\"): 없음 (val2={val2})");

        // 순회
        Console.WriteLine("\n순회:");
        foreach (var kv in map)
            Console.WriteLine($"  {kv.Key} -> {kv.Value}");

        // 카운팅 패턴 (코딩테스트 단골!)
        Console.WriteLine("\n=== 카운팅 패턴 ===");
        string[] words = { "hello", "world", "hello", "foo", "world", "hello" };
        var count = new Dictionary<string, int>();
        foreach (var w in words)
        {
            if (!count.ContainsKey(w)) count[w] = 0;
            count[w]++;
        }
        foreach (var kv in count)
            Console.WriteLine($"  \"{kv.Key}\": {kv.Value}번");

        // ===== HashSet<T> =====
        Console.WriteLine("\n=== HashSet<T> (Python의 set) ===\n");

        var set = new HashSet<int>();
        set.Add(1);
        set.Add(2);
        set.Add(2);  // 중복 무시
        set.Add(3);
        Console.WriteLine($"Set: {{{string.Join(", ", set)}}}");
        Console.WriteLine($"Contains(2): {set.Contains(2)}, Count: {set.Count}");

        // 배열 중복 제거
        int[] dupes = { 1, 3, 2, 3, 1, 4, 2 };
        var unique = new HashSet<int>(dupes);
        Console.WriteLine($"중복 제거: {{{string.Join(", ", unique)}}}");

        // ===== Stack<T> =====
        Console.WriteLine("\n=== Stack<T> ===\n");

        var stack = new Stack<int>();
        stack.Push(10);
        stack.Push(20);
        stack.Push(30);
        Console.WriteLine($"Stack: [{string.Join(", ", stack)}]  (top이 왼쪽)");
        Console.WriteLine($"Peek: {stack.Peek()}");
        Console.WriteLine($"Pop: {stack.Pop()}");
        Console.WriteLine($"Pop 후: [{string.Join(", ", stack)}]");

        // ===== Queue<T> =====
        Console.WriteLine("\n=== Queue<T> ===\n");

        var queue = new Queue<int>();
        queue.Enqueue(10);
        queue.Enqueue(20);
        queue.Enqueue(30);
        Console.WriteLine($"Queue: [{string.Join(", ", queue)}]  (front가 왼쪽)");
        Console.WriteLine($"Peek: {queue.Peek()}");
        Console.WriteLine($"Dequeue: {queue.Dequeue()}");
        Console.WriteLine($"Dequeue 후: [{string.Join(", ", queue)}]");

        // ===== PriorityQueue =====
        Console.WriteLine("\n=== PriorityQueue<T, TPriority> (.NET 6+) ===\n");

        var pq = new PriorityQueue<string, int>();
        pq.Enqueue("낮은 우선순위", 3);
        pq.Enqueue("높은 우선순위", 1);
        pq.Enqueue("중간 우선순위", 2);

        Console.WriteLine("우선순위 순서대로 Dequeue:");
        while (pq.Count > 0)
            Console.WriteLine($"  {pq.Dequeue()}");

        // 최대 힙 트릭
        Console.WriteLine("\n최대 힙 (우선순위에 - 붙이기):");
        var maxPq = new PriorityQueue<int, int>();
        int[] vals = { 5, 1, 8, 3 };
        foreach (int v in vals)
            maxPq.Enqueue(v, -v);

        while (maxPq.Count > 0)
            Console.Write($"{maxPq.Dequeue()} ");
        Console.WriteLine();
    }
}
