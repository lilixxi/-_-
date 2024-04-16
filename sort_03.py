### 함수 ###
from random import randint

def selectSort(ary):
    n = len(ary) # 전체 데이터의 개수 
    for i in range(len(ary)-1) : #데이터의 개수보다 1개 더 적게 돔 / cycle 1 
        minIdx = i  # 맨처음에 지정하는 최솟값을 i 로  / ary[i] 보다 작은 값을 찾는것임 
        for k in range(i+1,len(ary)): #그 다음번호부터 끝까지 / cycle 2 / i 다음값부터 끝까지 
            if ary[minIdx] > ary[k] :
                minIdx = k #업데이트 해주고 작은값을 
        ary[i],ary[minIdx] = ary[minIdx],ary[i] # 업데이트 한 값과 i 의 위치를 바꿔준다 / 최솟값을 맨 처음으로 / i 와 최솟값의 위치를 바꿔줌 
        

def selectSort(ary) :

    for i in range(len(ary)-1):
        min_idx = i
        for k in range(i+1,len(ary)):
            if ary[min_idx] > ary[k]  :
                min_idx = k
        ary[i] , ary[min_idx] = ary[min_idx],ary[i]                   
        
    

### 변수 ###

dataAry = [randint(30,190) for i in range(4)]
dataAry

### 메인 ###
print(f'정렬 전... {dataAry}')
dataAry = selectSort(dataAry)
print(f'정렬 후... {dataAry}')