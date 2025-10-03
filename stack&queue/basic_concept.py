'''
    queue: FIFO(선입선출) 형식으로 데이터를 저장하는 자료구조
    queue는 rear에서 데이터를 추가하는 eunqueue와 front에서 데이터를 삭제하는 dequeue를 포함한다.
    1. Array List based Queue
    2. Linked List based Queue
    ** queue는 코딩테스트에 단독으로 출제되지 않음 **
'''

# 1. python의 list로 queue 만들기 -> 사실상 queue는 array list로 구현하지 않음.
# queue 선언
q=[] 
# queue의 enqueue는 append로 구현하면 된다.
# O(1)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
# queue의 dequeue는 list의 pop으로 구현하면 된다. 
# O(n): 첫번째 데이터를 빼고 한칸씩 옮겨줘야함
q.pop(0)
q.pop(0)
q.pop(0)

# 2. Linked list based queue  - deque(doubly ended queue) 활용
# 파이썬의 deque 자료구조를 활용, 파이썬의 deque은 front와 rear를 포함한 inked List로 구현되어 있다.
# deque은 front에서도 enqueue와 dequeue를 할 수 있고, rear에서도 enqueue와 dequeue를 할 수 있다. 
from collections import deque
queue = deque() 
# enqueue() O(1)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
# dequeue() O(1)
queue.popleft()
queue.popleft()
queue.popleft()



'''
    stack: LIFO(후입선출) 형식으로 데이터를 저장하는 자료구조
    stack의 top에 데이터를 추가하는 것을 push라고 하며 stack의 top에서 데이터를 추출하는 것을 pop이라고 한다.
    1. Array List based Stack
    2. Linked List based Stack
    ** stack은 코딩테스트에서도 단독으로 자주 출제되기 때문에 굉장히 중요한 자료구조다. **
'''

# 1. List based Stack -> stack은 list로 구현함!
stack=[]
# push O(1)
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
# pop O(1)
stack.pop()
stack.pop()
stack.pop()
