### 함수 ###
from random import randint

def findMinIndex(ary): # 배열 넘겨 받기
    minIdx = 0 # 0번째를 가장 작은 값으로 (인덱스로 받음)
    for i in range(1,len(ary)): # 그 다음값부터 끝까지?
        if (ary[minIdx] > ary[i]) : # 만약 최솟값이 아니라면
            minIdx = i
    return minIdx


### 변수 ###
before = [randint(30,190) for i in range(8)]
before # 정렬전
after = []  # 정렬후 
### 메인 ###
print(f'정렬 전... {before}')
for i in range(len(before)):
    minpos = findMinIndex(before)
    # pop 은 맨 마지막 값을 삭제하고 
    # remove 는 값을 삭제하는거라 (위치가 다를수 있다)
    # 그냥 append 하고 del 해주자 
    after.append(before[minpos])
    del (before[minpos])

print(f'정렬 후... {after}')

# 하지만 굳이 메모리 방을 2개씩이나 쓸 필요가 있을까?
# -> 방 하나에서 처리해보자 