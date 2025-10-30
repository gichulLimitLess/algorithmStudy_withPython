/*
  우선순위대로 원소를 뽑아내야 하는 우선순위 큐
  --> 다익스트라, 어려운 그리디 문제 등 여러 문제에서 사용된다!
  --> Python에서는 heapq로 최소 힙 바로 사용 가능하나.. JS는 없다! 직접 구현해야 함
*/

class PriorityQueue {
  constructor() {
    // 2차원 트리를 선형적인 배열로 구현 가능
    this.heap = [];
  }

  size() {
    return this.heap.length;
  }

  isEmpty() {
    return this.heap.length === 0;
  }

  /* 데이터 삽입 */
  enqueue(value) {
    this.heap.push(value);
    this.heapifyUp(); // 최소 힙 원칙에 따라 정렬하는 heapifyUp 메소드 수행
  }

  // -> 맨 끝에 새로 삽입된 노드를 정렬해 주는 코드
  heapifyUp() {
    // "최소 힙" 원칙에 따라 정렬
    let i = this.size() - 1;
    const lastNode = this.heap[i];

    while (i > 0) {
      const parentIndex = Math.floor((i - 1) / 2); // 자기 자신의 index에서 -1하고 나누기 2 하면 부모 index임
      if (this.heap[parentIndex] > lastNode) {
        // 부모가 lastNode보다 크다면 --> 바꿔야 한다
        this.heap[i] = this.heap[parentIndex]; // parentIndex에 있는 친구를 heap[i](--> 자식)으로 내린다
        i = parentIndex;
      } else {
        // 이미 부모가 자식보다 작거나 같은 경우 --> 최소 힙 이미 만족 중임
        break;
      }
      this.heap[i] = lastNode; // lastNode를 부모에 넣는다
    }
  }

  /* 
    데이터 삭제
    --> 힙의 삭제는 항상 루트노드에서만 일어난다
  */
  dequeue() {
    if (this.isEmpty()) return null; // 비어 있으면 그냥 종료
    const rootNode = this.heap[0];
    const lastNode = this.heap.pop();

    // heap이 완전히 비어 있다면, heapifyDown() 수행 불필요
    // --> root 한 개만 남아있는 경우, 그거 빼고 더 이상 수행하면 안된다
    if (this.size() > 0) {
      this.heap[0] = lastNode; // 마지막 노드를 맨 위로 올린다 --> rootNode는 없어짐
      this.heapifyDown();
    }

    return rootNode; // 저장해 놨던 사라지기 전의 루트 노드 값을 돌려준다
  }

  // 상위 루트노드를 좌우의 자식노드와 비교해서 트리의 하위로 점점 내리면서 정렬시키는 메소드
  heapifyDown() {
    let i = 0;
    const heapSize = this.size();

    while (true) {
      let swapIndex = null;
      let leftChildIndex = i * 2 + 1;
      let rightChildIndex = i * 2 + 2;
      if (leftChildIndex < heapSize) {
        // heapSize보다 leftChildIndex보다 작으면 --> 유효한 범위!
        if (this.heap[leftChildIndex] < this.heap[i]) {
          // 대상이 왼쪽 자식보다 크다면, 왼쪽 자식 인덱스를 바꿔야할 인덱스로 지정해야 한다
          swapIndex = leftChildIndex;
        }
      }

      if (rightChildIndex < heapSize) {
        // heapSize보다 rightChildIndex보다 작으면 --> 유효한 범위!
        if (
          (swapIndex === null && this.heap[rightChildIndex] < this.heap[i]) ||
          (swapIndex !== null && this.heap[rightChildIndex] < this.heap[leftChildIndex])
        ) {
          // 바꿔야할 인덱스가 지정된 값이 없고, 대상이 오른쪽 자식보다 크거나,
          // 바꿔야할 인덱스가 왼쪽으로 지정되어 있지만, 왼쪽 자식이 오른쪽 자식보다 크다면
          swapIndex = rightChildIndex; // 바꿔야할 인덱스로 오른쪽 자식 인덱스를 지정한다
        }
      }

      // 바꿔야할 인덱스가 없다면 반복문 종료
      if (swapIndex === null) break;

      // 바꿔야할 인덱스와 대상의 위치를 바꿔준다
      // i를 swapIndex로 계속 갱신해 주면서 그 밑을 더 탐색한다
      [this.heap[i], this.heap[swapIndex]] = [this.heap[swapIndex], this.heap[i]];
      i = swapIndex;
    }
  }
}

const q = new PriorityQueue();
q.enqueue(5);
q.enqueue(10);
q.enqueue(4);
q.enqueue(1);
console.log(q.dequeue()); // 결과: 1
console.log(q.dequeue()); // 결과: 4
console.log(q.dequeue()); // 결과: 5
console.log(q.dequeue()); // 결과: 10
