# 실무버전

### 함수 ###
# 0. 함수가 꽉 찼는지 확인 (오버헤드 방지)
# 꽉찼다 == top 이 맨 꼭대기(== 사이즈만큼 인지)
def isStackFull():
    global SIZE,stack,top
    if top == SIZE-1 :
        return True #꽉찼다
    else : return False #꽉차지 않았다 
    
# 1. push
def push(data):
    global SIZE,stack,top
    if isStackFull(): # 자체가 True False 니 두번 묻지 않기
        print('stack is full ! ')
        return
    top += 1
    stack[top] = data
    # else 를 굳이 넣을 필요가 없음
    
    print(f'>>>{stack}>>>')
# 0. 비었는지 확인
def isStackEmpty():
    global SIZE,stack,top
    if top == -1 : 
        return True
    else : return False
# 2. pop()    
def pop():
    global SIZE,stack,top
    # 비었는지 확인
    if isStackEmpty() :  # 자체가 True False 니 두번 묻지 않기
        print('Stack is empty !')
        return 
    data = stack[top] # 탑에 있는것을 
    stack[top] = None #그리고 없앰 
    top -= 1
    return data #반환 

# 3. peek() 
# top 위치를 확인하고 스택에 그대로 두는 것
# 비어있는지 확인 
def peek():
    global SIZE,stack,top
    if isStackEmpty() : 
        print('Stack is empty !')
        return 
    return stack[top]

### 변수 ###
SIZE = 5
stack = [ None for i in range(SIZE)]
stack
top = -1  #stack 초기화

### 메인 ###
# 1. push()
push('커피')
push('녹차')
push('꿀물')
push('콜라')
push('환타')
push('제로콕')

# 2. pop()
pop()
pop()
stack

# 3. peek()
peek()