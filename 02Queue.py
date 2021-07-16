# 210717
# 02 큐

# [1] 큐 기본 사용법 - FIFO Queue

import queue


fifo_queue = queue.Queue() # FIFO 큐 생성

fifo_queue.put("funcoding") # 큐에 값 넣기 / put()
fifo_queue.put(1)

print(fifo_queue.qsize()) # 현재 큐 사이즈 확인 / qsize()

print(fifo_queue.get()) # 큐에서 값 하나 꺼내기 / get()



# [2] LIFO Queue 사용

lifo_queue = queue.LifoQueue() # LIFO 큐 생성

lifo_queue.put("happy") # 큐에 값 넣기 / put()
lifo_queue.put(37)

lifo_queue.qsize() # 현재 큐 사이즈 확인 / qsize()

print(lifo_queue.get()) # 큐에서 값 하나 꺼내기 / get()




# [3] Priority Queue 사용

p_queue = queue.PriorityQueue() # Priority 큐 생성

p_queue.put((10, "korea")) # 큐에 값 넣기 / put()
p_queue.put((5, 1))
p_queue.put((14, "canada"))

print(p_queue.qsize()) # 현재 큐 사이즈 확인 / qsize()

print(p_queue.get()) # 큐에서 값 하나 꺼내기 / get()





# 연습 1: 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현

queue_list = []

def enqueue(data):
    queue_list.append(data) # 리스트에 값 추가

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for i in range(10):
    enqueue(i)

print(len(queue_list))

dequeue()

print(queue_list)
