### 함수 ###
# 0. 큐가 꽉찼는지 확인 (오버플로우 방지)
def isQueFull():
    global SIZE,queue,front,rear
    if rear == SIZE-1 : # 만약 꼬리가 사이즈와 동일하다면 
        return True
    else : return False
    
# 큐의 단점 수정
def isQueFull():
    global SIZE,queue,front,rear
    if (rear != SIZE -1) : # 1. 꽉 차지 않았을경우
        return False
    elif (rear == SIZE -1 ) and (front == -1 ) : # 2. 진짜 꽉찬 경우
        return True
    elif (rear == SIZE -1 ) and (front != -1 ) : # 3. 앞에가 비었는데 꽉찼다고 나오는 경우
        # else 로 처리해도 되는데 그냥 가시성을 위해서 씀
        # 한칸씩 땡기기
        for i in range(front+1,SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1 
        rear -= 1
        return False # 꽉 차지 않았으니 False 
    
    
def enqueue(data):
    global SIZE,queue,front,rear
    if isQueFull() :
        print('Queue is full !')
        return 
    rear += 1
    queue[rear] = data 
    print(queue)


def isQueEmpty():
    global SIZE,queue,front,rear
    # front 와 rear 이 같을 경우 큐가 비었다 
    # 맨처음 초기조건 
    if front == rear :
        return True
    else : return False
    
# 2. dequeue()            
def dequeue():
    global SIZE,queue,front,rear
    if isQueEmpty() :
        print('Queue is empty !')
        return 
    front += 1 
    data = queue[front] #변수에 저장해주고
    queue[front] = None #큐는 비워주고 
    return data #변수에 저장한 값 리턴

# 3. peek()
def  peek():
    if isQueEmpty() :
        print('Queue is empty !')
        return 
    return queue[front+1] #front 다음 == 앞으로 빠질 데이터 를 보여준다 
    

### 변수 ###
SIZE = 5
queue = [ None for i in range(SIZE)] 
# stack queue 모두 배열인데, 한쪽만 뚫린것인지, 양쪽이 뚫린것인지로 취급할것인지 결정 
front = rear = -1
queue

### 메인 ###
# 1. enque()
enqueue('화사')
enqueue('솔라')
enqueue('문별')
enqueue('휘인')
enqueue('선미')
enqueue('가희')

# 2. dequeue()
dequeue()
dequeue()

# 3. peek()
# 그 다음으로 빠지는 데이터 (fron+1) 을 알려준다 
peek()
queue
enqueue('가희')
# 앞에가 비었는데 왜 꽉찼다고 하는걸까?
# rear 가 마지막에 있을때 꽉찼다고 한다
# 앞에가 비어있음에도 불구하고 rear 가 마지막이므로 꽉찼다고 여겨진다
# 이거를 해결하려면?
# 현실상황에선 한칸씩 땡기지만 컴퓨터에선 비효율적인 상황
# 누가 들어올 경우만 땡긴다 
# 누가 들어온다 -> 1. 진짜 꽉참 / 2. 앞에가 비었는데 꽉찼다고 함 
