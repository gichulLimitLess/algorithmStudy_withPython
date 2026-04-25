# C# 코딩테스트 연습 파일

## 실행 방법

각 파일을 개별적으로 실행할 수 있습니다:

```bash
# dotnet-script 사용 (설치: dotnet tool install -g dotnet-script)
dotnet-script 01_Variables.cs

# 또는 csc 컴파일러 사용
csc 01_Variables.cs && mono 01_Variables.exe    # macOS
csc 01_Variables.cs && ./01_Variables.exe        # Windows
```

## 파일 목록

| 파일 | 치트시트 섹션 | 내용 |
|------|-------------|------|
| `01_Variables.cs` | 2~3장 | 변수, 타입, 변환, 연산자, 조건문 |
| `02_Arrays.cs` | 4~5장 | 1차원/2차원/가변 배열, 정렬, 반복문 |
| `03_DataStructures.cs` | 6장 | List, Dictionary, HashSet, Stack, Queue, PriorityQueue |
| `04_Strings.cs` | 7장 | 문자열 조작, char 판별, StringBuilder |
| `05_LINQ.cs` | 8장 | 집계, 필터, 변환, 정렬, GroupBy 등 |
| `06_LambdaAndUtils.cs` | 9~12장 | 람다, Math, 튜플, 디버깅 출력 |
| `07_Templates.cs` | 14장 | BFS, DFS, 카운팅, 이진탐색 실전 템플릿 |
