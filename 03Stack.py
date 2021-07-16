# 210717
# 03 스택

# [1] 재귀함수로 스택 이해하기

def recursive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        recursive(data -1)
        print("returned", data)

recursive(4)



# [2] 리스트로 스택 사용해보기

data_stack = list() # 리스트로 스택 생성

data_stack.append(1) # 리스트에 원소 추가 / append()
data_stack.append(2)

print(data_stack)

print(data_stack.pop()) # 리스트에서 원소 추출 / pop()





# 연습 1: 리스트 변수로 스택을 다루는 pop, push 기능 구현 (pop, push 함수 사용 X)

stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[len(stack_list)-1]
    del stack_list[len(stack_list)-1]
    return data


push(1)
push(5)
push(4)
print(stack_list)

data1 = pop()
data2 = pop()

print(data1, data2)
