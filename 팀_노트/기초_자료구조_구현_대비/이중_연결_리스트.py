# ===========================================================
# Doubly Linked List 구현 (면접용 최적 템플릿)
# Node(prev, next) + LinkedList(head, tail)
# append, prepend, delete, search, traverse 구현
# ===========================================================

class Node:
    """
    Doubly Linked List의 노드 구조
    - val: 값
    - prev: 이전 노드를 가리키는 포인터
    - next: 다음 노드를 가리키는 포인터
    """
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    이중 연결 리스트(Doubly Linked List)
    - head: 첫 노드
    - tail: 마지막 노드
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

        # 빈 리스트
        if self.head is None:
            self.head = self.tail = new_node
            return

        # 기존 tail 뒤에 삽입
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    # -------------------------------------------------------
    # 앞에 노드 추가 (prepend) - O(1)
    # -------------------------------------------------------
    def prepend(self, data):
        new_node = Node(data)
        self._size += 1

        if self.head is None:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # -------------------------------------------------------
    # 특정 값을 가진 첫 번째 노드 삭제 - O(1)
    # -------------------------------------------------------
    def delete(self, data):
        if self.isEmpty():
            return "삭제 불가 (빈 리스트)"

        current = self.head

        # head 삭제
        if current.val == data:
            self.head = current.next
            self._size -= 1

            if self.head:
                self.head.prev = None
            else:
                self.tail = None

            return "삭제 완료"

        # 중간 삭제
        while current and current.val != data:
            current = current.next

        if current is None:
            return "삭제 불가 (값 없음)"

        # prev - current - next 구조에서 current 제거
        if current.next:  # 중간 노드
            current.prev.next = current.next
            current.next.prev = current.prev
        else:  # tail 삭제
            current.prev.next = None
            self.tail = current.prev

        self._size -= 1
        return "삭제 완료"

    # -------------------------------------------------------
    # 특정 값 검색(search) - O(n)
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
    # 리스트 전방 순회 (정방향) - O(n)
    # -------------------------------------------------------
    def traverse_forward(self):
        if self.isEmpty():
            return "빈 리스트"

        vals = []
        current = self.head

        while current:
            vals.append(str(current.val))
            current = current.next

        return " → ".join(vals)

    # -------------------------------------------------------
    # 리스트 역방향 순회 (후방) - O(n)
    # -------------------------------------------------------
    def traverse_backward(self):
        if self.isEmpty():
            return "빈 리스트"

        vals = []
        current = self.tail

        while current:
            vals.append(str(current.val))
            current = current.prev

        return " ← ".join(vals)

    # -------------------------------------------------------
    # 리스트 길이 반환
    # -------------------------------------------------------
    def get_size(self):
        return self._size

    # -------------------------------------------------------
    # 비어있는지 확인
    # -------------------------------------------------------
    def isEmpty(self):
        return self._size == 0


# ===========================================================
# 테스트 케이스
# ===========================================================

if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("=== append 테스트 ===")
    dll.append(10)
    dll.append(20)
    dll.append(30)
    print("정방향:", dll.traverse_forward())   # 10 → 20 → 30
    print("역방향:", dll.traverse_backward())  # 30 ← 20 ← 10
    print("size =", dll.get_size())

    print("\n=== prepend 테스트 ===")
    dll.prepend(5)
    dll.prepend(1)
    print("정방향:", dll.traverse_forward())   # 1 → 5 → 10 → 20 → 30
    print("역방향:", dll.traverse_backward())
    print("size =", dll.get_size())

    print("\n=== search 테스트 ===")
    print(dll.search(20))  # 4번째에서 20 발견
    print(dll.search(999))

    print("\n=== delete 테스트 ===")
    print(dll.delete(1))   # head 삭제
    print(dll.delete(20))  # 중간 삭제
    print(dll.delete(30))  # tail 삭제
    print("정방향:", dll.traverse_forward())
    print("역방향:", dll.traverse_backward())
    print("size =", dll.get_size())

    print("\n=== 없는 값 삭제 ===")
    print(dll.delete(999))
    print("정방향:", dll.traverse_forward())
