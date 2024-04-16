## 함수
def isqueueFull() :
    global SIZE, queue, front, rear
    if ( (rear+1)%SIZE == front) :
        return True
    else :
        return False

def enqueue(data) :
    global SIZE, queue, front, rear
    if (isqueueFull()) :
        print('큐 꽉!')
        return
    rear = (rear+1)%SIZE
    queue[rear] = data

def isqueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def dequeue() :
    global SIZE, queue, front, rear
    if (isqueueEmpty()) :
        print('큐 텅~')
        return
    front = (front+1)%SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isqueueEmpty()) :
        print('큐 텅~')
        return
    return queue[(front+1)%SIZE]

## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0 # -1 이 없다


enqueue('화사')
enqueue('솔라')
enqueue('문별')
enqueue('휘인')
enqueue('선미')
queue
dequeue()
dequeue()
queue
enqueue('가희') 
#원형큐, 맨 앞으로 값이 간다 
# none 의 위치는 계속 바뀜 (그것이 원형큐니까)