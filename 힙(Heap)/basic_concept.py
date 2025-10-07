'''
    우선 순위 큐 : 우선순위가 높은 데이터부터 추출하는 자료구조
    1. 배열 기반 우선순위 큐 - enqueue: O(1), dequeue: O(n)
    2. 배열 기반 우선순위 큐(enqueue시 정렬) - enqueue:O(nlogn), dequeue: O(1) 
    3. 힙 기반 우선순위 큐 - enqueue: O(logn), dequeue: O(logn)
'''

'''
    Heap: 완전 이진 트리 형태의 자료구조 
    특징: 
        List로 구현할 수 있다. list의 index만으로 부모노드,자식노드를 찾을 수 있다는 장점이 있다.
        i번째 노드의 왼쪽 자식 노드는 2i+1, 오른쪽 자식 노드는 2i+2
    Heap의 종류 
        1. min heap: 부모 노드의 값이 자식 노드의 값보다 작은 트리 형태의 자료구조. 형제 노드 간에는 대소 관계가 정해지지 않는다.
        2. max heap: 부모 노드의 값이 자식 노드의 값보다 큰 트리 형태의 자료구조. 형제 노드 간에는 대소 관계가 정해지지 않는다.
'''



# min-heap 구현
import heapq
min_heap=[5,3,9,4,1,2,6]
# 힙 구현 - heapify: O(n)
heapq.heapify(min_heap)
print(min_heap) # [1, 3, 2, 4, 5, 9, 6]
# 힙 dequeue - dequeue시 sift down 최대 logn번 실행
print(heapq.heappop(min_heap)) # 1 heappop은 루트노드를 return
print(min_heap) # [2, 3, 6, 4, 5, 9]
# 힙 enqueue - enqueue시 sift up 최대 logn번 실행
print(heapq.heappush(min_heap,1)) # heappush의 return은 None
print(min_heap)

# max-heap 구현1
max_heap=[5,3,9,4,1,2,6]
# 힙 구현
heapq._heapify_max(max_heap) # [9, 4, 6, 3, 1, 2, 5]
print(max_heap)
# 힙 dequeue
# heapq._heappop_max(max_heap) 
# 힙 enqueue -> heappush가 없음 

# max-heap 구현2
max_heap=[5,3,9,4,1,2,6]
max_heap=[i*-1 for i in max_heap]
heapq.heapify(max_heap)
print(max_heap)
weight = heapq.heappop()
value = -1*weight
