### 함수 ###

### 변수 ###
SIZE = 5
queue = [ None for i in range(SIZE)] 
# stack queue 모두 배열인데, 한쪽만 뚫린것인지, 양쪽이 뚫린것인지로 취급할것인지 결정 
front = rear = -1
queue
### 메인 ###
# 1. enque()
rear += 1
queue[rear] = '화사'

rear += 1
queue[rear] = '솔라'

rear += 1
queue[rear] = '문별'

print(f'exit < -- {queue} <-- enter ')

# 2. deque()
front += 1 
data = queue[front]
queue[front] = None
print(data)

front += 1 
data = queue[front]
queue[front] = None
print(data)

front += 1 
data = queue[front]
queue[front] = None
print(data)

