'''
    Python으로 트리 구조를 표현하기 위해서, Node 클래스를 정의해서..
    각 노드의 값과 자식 노드들을 저장하고, 이를 연결해서 트리 구조를 만든다.

    [트리 구조 구현]
    1. 노드 클래스 정의
        - 트리의 기본 요소인 노드를 나타내는 클래스를 만든다
        - 각 노드는 data(또는 value)와 자식 노드들을 저장할 children
            (또는, left, right 등 / 이진트리에서..) 속성을 가진다
    2. 트리 구조 구현
        - 일반 트리: Node 객체를 생성하고, 자식 노드를 children 리스트에 추가하는 방식으로 트리 구축
        - 이진 트리: Node 객체를 생성하고, left와 right 속성을 사용해서 왼쪽/오른쪽 자식 노드를 연결
'''

class Node:
    def __init__(self, data):
        self.data = data
        # self.children = [] # 자식 노드들을 저장할 리스트 (일반적인 트리)
        self.left = None # 이진 트리라면 왼쪽 자식 노드
        self.right = None # 이진 트리라면 오른쪽 자식 노드

# 루트 노드 생성
root = Node(10)

# 왼쪽 자식 노드 추가 (값 5)
root.left = Node(5)

# 오른쪽 자식 노드 추가 (값 15)
root.right = Node(15)

# 오른쪽 자식 노드의 왼쪽 자식 추가 (값 12)
root.right.left = Node(12)

# 순회 예시 (전위 순회: root -> left -> right)
def pre_order_traversal(node):
    if node:
        print(node.data, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

pre_order_traversal(root)
# 출력: 10 5 15 12

'''
    위처럼 구현하면, 자료구조에 대한 본질적 이해가 깊어지고..
    트리 변형, 병합, 다중 루트, 가중치 처리 등 복잡한 문제로 확장 가능하다.
    그러나, Python에서는 재귀 깊이 + 클래스 오버 헤드로 속도도 느리고.. 
    코딩 테스트에서 직접적으로 사용하기엔 에바일 가능성도 있다.
    즉, 위 문제는 "기술 면접"에서 트리 구현 어케 함? 같은 때에 사용하면 좋은 코드일 것이다.
    ---> 그리고, 결정적으로, 실전 코딩테스트에서는 대부분 트리 문제도 "인접 리스트"로 풀어도 충분하다.
'''

