# 210717
# 04 링크드 리스트

# [1] 간단한 Linked List 구현
# 1. Node 구현

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



# 2. Node와 Node 연결(포인터 활용)

node1 = Node(1) # Node 생성
node2 = Node(2)

node1.next = node2 # Node 연결

head = node1 # head Node 설정



# 3. Linked List로 데이터 추가하기

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)


node1 = Node(1) # Node 생성
head = node1 # head node 설정

for i in range(2, 10): # linked list에 데이터 추가(2 ~ 9)
    add(i)



# 4. Linked List 데이터 출력하기(검색하기)
print("----Linked List 데이터 출력하기----")

node = head

while node.next:
    print(node.data)
    node = node.next
print(node.data)



# [2] Liked List의 복잡한 기능
# 1. Linked List의 데이터 사이에 새로운 데이터 추가
print("----데이터 사이에 새로운 데이터 추가하기----")

node3 = Node(1.5)
node = head
search = True

while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

node_next = node.next
node.next = node3
node3.next = node_next

node = head
while node:
    print(node.data)
    node = node.next



# [3] 객체지향 프로그래밍으로 Linked List 구현

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            print("해당 노드가 없습니다.")
            return

        if self.head.data == data: # 특정 노드가 head인 경우
            temp = self.head
            self.head = self.head.next
            del temp
            
        else: # 특정 노드가 head가 아닌 경우
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next
                    


# [3]코드 Test & 연습 1: 위 코드에서 노드 데이터가 2인 노드 삭제
print("----특정 노드 삭제하기----")


linkedlist1 = NodeMgmt(0) # 테스트를 위해 1개의 노드 생성
linkedlist1.desc() # 전체 노드 출력

linkedlist1.delete(0) # 특정 노드 삭제

linkedlist1.desc() # 전체 노드 출력, 삭제됐기 때문에 아무 것도 뜨지 않음

print()

linkedlist1 = NodeMgmt(0) # 노드 생성
for data in range(1, 10):
    linkedlist1.add(data) # 노드 추가
    
print("삭제 전")
linkedlist1.desc() # 전체 노드 출력

print("\n삭제 후")

linkedlist1.delete(2) # 특정 노드 삭제
linkedlist1.desc() # 전체 노드 출력



# 연습 2: [3]코드에서 노드 데이터가 특정 숫자인 노드를 찾는 함수를 만들고 테스트 해보기
# 테스트 : 임의로 1~9까지 데이터를 linked list에 넣고 데이터 값이 4인 노드의 데이터 값 출력

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data): # 맨 끝에 새로운 데이터 추가
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            print("해당 노드가 없습니다.")
            return

        if self.head.data == data: # 특정 노드가 head인 경우
            temp = self.head
            self.head = self.head.next
            del temp
            
        else: # 특정 노드가 head가 아닌 경우
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next

    def search_node(self, data):
        if self.head == '':
            print("해당 노드가 없습니다.")
            return

        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

# 테스트
print("----특정 노드 검색하기----")

node_mgmt = NodeMgmt(0)
for data in range(1, 10):
    node_mgmt.add(data)

node = node_mgmt.search_node(4)
print(node.data)
