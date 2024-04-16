# 순차검색
# 정렬이 안된 상태에서 사용 
### 함수 ###
from random import randint, choice

def seqSearch(ary,find_data): # 배열, 찾을 데이터 입력
    pos = -1   # 못찾을 경우 반환값
    for i in range(len(ary)) :
        if ary[i] == find_data :
            pos = i
            break
    return pos #인덱스 값 반환


### 변수 ###
dataAry = [randint(30,190) for i in range(8)]
findData = choice(dataAry) #하나 랜덤으로 선택
findData
### 메인 ###
print(f'정렬 전... {dataAry}')
position = seqSearch(dataAry,findData) 
if position != -1 :
    print(f'{findData} 는 {position} 위치에 있다 ')
else : print(f'{findData} 는 없습니다 ')

