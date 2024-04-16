# 순차검색
# 실무코드
# 정렬이 안된 상태에서 사용 
### 함수 ###
from random import randint, choice

def binSearch(ary,find_data): # 배열, 찾을 데이터 입력
    global count
    pos = -1   # 못찾을 경우 반환값
    start = 0
    end = len(ary)-1
    while start <= end : #작거나 같을때까지 (같은경우 그 값 )
        count += 1
        middle = (start + end) // 2 
        if ary[middle] == find_data :
            pos = middle
            break
        elif ary[middle] < findData :
            start = middle+1
        elif ary[middle] > findData : # else 로 처리해도 됨 
            end = middle-1 

    return pos


### 변수 ###
count = 0 # 몇번만에 찾는지 확인
dataAry = [randint(30,190000) for i in range(1000)]
dataAry.sort()
# dataAry
findData = choice(dataAry) #하나 랜덤으로 선택
findData
# 없는 데이터 일 경우 
# findData = 199
### 메인 ###
# print(f'정렬 전... {dataAry}')
position = binSearch(dataAry,findData) 

if position != -1 :
    print(f'{position} 위치에 있다 {count} 번 만에 찾았다  ')
else : print(f'{findData} 는 없습니다 ')

