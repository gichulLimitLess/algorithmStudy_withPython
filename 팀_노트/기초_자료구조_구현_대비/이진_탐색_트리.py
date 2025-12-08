# ===========================================================
# Binary Search Tree (BST) 구현
# Node 구조 + insert + search + delete + traversal
# 면접용 최적 템플릿
# ===========================================================

class Node:
    """
    트리의 기본 단위인 Node
    - val : 저장 값
    - left : 왼쪽 자식 포인터
    - right : 오른쪽 자식 포인터
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    """
    Binary Search Tree (이진 탐색 트리)
    - root : 트리의 루트 노드
    - BST의 핵심 속성: left < root < right
    """
    def __init__(self):
        self.root = None

    # -------------------------------------------------------
    # 값 삽입 (insert) - O(h)
    # -------------------------------------------------------
    def insert(self, val):
        new_node = Node(val)

        # case 1: 트리가 비어 있는 경우
        if self.root is None:
            self.root = new_node
            return

        # case 2: 트리가 비어 있지 않다면 적절한 위치 찾기
        current = self.root
        while True:
            if val < current.val:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:  # val >= current.val
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    # -------------------------------------------------------
    # 값 탐색 (search) - O(h)
    # -------------------------------------------------------
    def search(self, key):
        current = self.root
        while current:
            if key == current.val:
                return True
            elif key < current.val:
                current = current.left
            else:
                current = current.right
        return False

    # -------------------------------------------------------
    # 트리 순회 (Traversal) - DFS 방식
    # In-order / Pre-order / Post-order
    # -------------------------------------------------------
    def inorder(self, node, result):
        # L → Root → R (정렬된 순서 출력)
        if node:
            self.inorder(node.left, result)
            result.append(node.val)
            self.inorder(node.right, result)

    def preorder(self, node, result):
        # Root → L → R
        if node:
            result.append(node.val)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

    def postorder(self, node, result):
        # L → R → Root
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.val)

    # -------------------------------------------------------
    # 삭제(delete) - BST 가장 어려운 기능
    # case1: leaf 삭제
    # case2: 한쪽 자식만 있는 노드 삭제
    # case3: 두 자식 모두 있는 노드 삭제 → inorder successor 사용
    # -------------------------------------------------------
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return None

        # 탐색
        if key < node.val:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.val:
            node.right = self._delete_recursive(node.right, key)
        else: # key를 발견했을 경우 --> 3가지 경우가 존재, 각 케이스에 맞게 처리
            # -------------------------
            # case 1: 자식이 없음 (leaf)
            # -------------------------
            if node.left is None and node.right is None:
                return None

            # -------------------------
            # case 2: 한쪽 자식만 존재
            # -------------------------
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # -------------------------
            # case 3: 두 자식 모두 존재
            # 오른쪽 서브트리에서 최소값(중위 후속자) 찾기 -> 그리고, 그 최솟값 찾아 node 없애기
            # -------------------------
            successor = self._get_min(node.right)
            node.val = successor.val
            node.right = self._delete_recursive(node.right, successor.val)

        return node

    def _get_min(self, node):
        """오른쪽 서브트리의 최소값(왼쪽 끝 노드)을 찾음"""
        while node.left:
            node = node.left
        return node


# ===========================================================
# 테스트 케이스 (BST 기능 검증)
# ===========================================================

if __name__ == "__main__":
    bst = BST()

    print("=== insert 테스트 ===")
    for x in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(x)
    print("삽입 완료")

    print("\n=== search 테스트 ===")
    print("search 40:", bst.search(40))  # True
    print("search 99:", bst.search(99))  # False

    print("\n=== traversal 테스트 ===")
    res = []
    bst.inorder(bst.root, res)
    print("In-order:", res)  # 정렬된 순서

    res = []
    bst.preorder(bst.root, res)
    print("Pre-order:", res)

    res = []
    bst.postorder(bst.root, res)
    print("Post-order:", res)

    print("\n=== delete 테스트 ===")
    bst.delete(30)   # 자식 2개 있는 노드
    bst.delete(20)   # leaf node
    bst.delete(70)   # 자식 2개 삭제
    res = []
    bst.inorder(bst.root, res)
    print("삭제 후 In-order:", res)
