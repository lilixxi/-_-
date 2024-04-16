# 정렬 
### 함수 ###

# 1. 최솟값 찾기
def findMinIndex(ary): # 배열 넘겨 받기
    minIdx = 0 # 0번째를 가장 작은 값으로 (인덱스로 받음)
    for i in range(1,len(ary)): # 그 다음값부터 끝까지?
        if (ary[minIdx] > ary[i]) : # 만약 최솟값이 아니라면
            minIdx = i
    return minIdx
            

### 변수 ###
testArry = [55,88,33,77]
testArry

### 메인 ###
minPos = findMinIndex(testArry)
testArry[minPos]