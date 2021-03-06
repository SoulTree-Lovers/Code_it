def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def reverse_heapify(tree, index):
    """삽입된 노드를 힙 속성을 지키는 위치로 이동시키는 함수"""
    parent_index = index // 2  # 삽입된 노드의 부모 노드의 인덱스 계산
    
    # 코드를 쓰세요.
    if 0 < parent_index < len(tree) and tree[index] > tree[parent_index]:
        swap(tree, index, parent_index)
        reverse_heapify(tree, parent_index)
        

class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""
    def __init__(self):
        self.heap = [None]  # 파이썬 리스트로 구현한 힙


    def insert(self, data):
        """삽입 메소드"""
        # 코드를 쓰세요
        #1 힙의 마지막 인덱스에 노드를 삽입한다.
        self.heap.append(data)

        #2 (1) 삽입한 노드와 그 부모 노드를 비교해서 부모 노드가 더 작으면 둘의 위치를 바꾼다.
        #2 (2) 삽입한 노드와 그 부모 노드를 비교해서 부모 노드가 더 크면 그대로 둔다.
        reverse_heapify(self.heap, len(self.heap)-1)

        #3 2-1의 경우에는 삽입한 노드가 올바른 위치를 찾을 때까지 단계 2를 반복한다.

    def __str__(self):
        return str(self.heap)


# 실행 코드
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue)