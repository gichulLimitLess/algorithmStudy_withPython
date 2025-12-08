# ===========================================================
# Singly Linked List 구현 (면접용 최적 템플릿)
# Node + LinkedList(head, tail) + append + prepend + delete + search + traverse
# ===========================================================

class Node:
    """
    단일 노드 구조
    - val : 저장할 값
    - next : 다음 노드를 가리키는 포인터
    """
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    """
    단일 연결 리스트(Singly Linked List)
    - head : 리스트의 첫 번째 노드
    - tail : 리스트의 마지막 노드 (append 시간복잡도를 O(1)로 만들기 위함)
    - _size: 리스트 길이
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # -------------------------------------------------------
    # 끝에 노드 추가 (append) - O(1)
    # -------------------------------------------------------
    def append(self, data):
        new_node = Node(data)
        self._size += 1

        # 리스트가 비었다면 head, tail 모두 새 노드를 가리킴
        if self.head is None:
            self.head = self.tail = new_node
            return

        # tail이 있으므로 O(1)로 추가 가능
        self.tail.next = new_node
        self.tail = new_node

    # -------------------------------------------------------
    # 앞에 노드 추가 (prepend) - O(1)
    # -------------------------------------------------------
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

        # 리스트가 비어 있었던 경우 tail도 설정
        if self.tail is None:
            self.tail = new_node

    # -------------------------------------------------------
    # 특정 값을 가진 첫 번째 노드 삭제 (delete) - O(n)
    # -------------------------------------------------------
    def delete(self, data):
        if self.isEmpty():
            return '삭제 불가 (빈 리스트)'

        current = self.head

        # case 1) head 삭제
        if current.val == data:
            self.head = current.next
            self._size -= 1

            # head 삭제 후 리스트가 비어버렸다면 tail도 제거
            if self.head is None:
                self.tail = None

            return '삭제 완료'

        # case 2) 중간 삭제
        prev = None
        while current and current.val != data:
            prev = current
            current = current.next

        if current is None:
            return '삭제 불가 (값 없음)'

        prev.next = current.next
        self._size -= 1

        # tail 삭제한 경우
        if current == self.tail:
            self.tail = prev

        return '삭제 완료'

    # -------------------------------------------------------
    # 특정 값 검색 (search) - O(n)
    # -------------------------------------------------------
    def search(self, key):
        current = self.head
        idx = 1

        while current:
            if current.val == key:
                return f"{idx}번째에서 {key} 발견"
            current = current.next
            idx += 1

        return f"{key}는 리스트에 존재하지 않음"

    # -------------------------------------------------------
    # 리스트 전체 순회 (traverse) - O(n)
    # -------------------------------------------------------
    def traverse(self):
        if self.isEmpty():
            return "빈 리스트"

        values = []
        current = self.head

        while current:
            values.append(str(current.val))
            current = current.next

        return " → ".join(values)

    # -------------------------------------------------------
    # 리스트 길이 반환
    # -------------------------------------------------------
    def get_size(self):
        return self._size

    # -------------------------------------------------------
    # 리스트가 비었는지 체크
    # -------------------------------------------------------
    def isEmpty(self):
        return self._size == 0


# ===========================================================
# 테스트 케이스 (LinkedList 기능 검증)
# ===========================================================

if __name__ == "__main__":
    ll = LinkedList()

    print("=== 테스트 1: append ===")
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("현재 리스트:", ll.traverse())   # 10 → 20 → 30
    print("size =", ll.get_size())         # 3

    print("\n=== 테스트 2: prepend ===")
    ll.prepend(5)
    ll.prepend(1)
    print("현재 리스트:", ll.traverse())   # 1 → 5 → 10 → 20 → 30
    print("size =", ll.get_size())         # 5

    print("\n=== 테스트 3: search ===")
    print(ll.search(20))  # 4번째에서 20 발견
    print(ll.search(99))  # 존재하지 않음

    print("\n=== 테스트 4: delete ===")
    print(ll.delete(1))   # head 삭제
    print(ll.delete(20))  # 중간 삭제
    print(ll.delete(30))  # tail 삭제
    print("현재 리스트:", ll.traverse())   # 5 → 10
    print("size =", ll.get_size())         # 2

    print("\n=== 테스트 5: delete (없는 값)")
    print(ll.delete(999))                  # 존재하지 않음
    print("현재 리스트:", ll.traverse())
