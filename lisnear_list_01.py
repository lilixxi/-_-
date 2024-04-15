# 선형리스트

###########################
# 함수선언부


###########################
# 전역변수
katok = ['다현','정연','쯔위','사나','지효']

###########################
# 메인코드

## 1. 빈칸 추가 
katok.append(None) #insert the empty place
katok[-1] ='모모' #insert friend in the empty place
katok

## 2. 데이터 삽입 (미나를 3등으로)
katok.append(None)
katok
# 한칸씩 뒤로 이동(마지막부터 3등까지 이동)
katok[6] = katok[5]
katok[5] = katok[4]
katok[4] = katok[3]
katok[3] = None
katok
# 3등자리에 미나 넣기
katok[3] = '미나'
katok

## 3. 데이터 삭제

# 1. 데이터 삭제 (사나카톡 삭제)
katok[4] = None

# 2. 한칸씩 이동
katok[4] = katok[5]
katok[5] = katok[6]
katok[6] = None

# 3. 마지막 칸 제거 
del katok[-1]



