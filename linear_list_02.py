###########################
## 현실용
# 함수선언부

## 마지막 데이터 삽입
def add_data(friend):
    katok.append(None) # 빈칸추가
    katok[-1] = friend # 마지막칸에 추가 
    print(katok)

## 데이터 삽입
def  insert_data(position,friend):
    katok.append(None) # 빈칸추가
    # 마지막 친구부터 삽입할 위치까지 한칸씩 뒤로 이동
    for i in range(len(katok)-1 , position,-1): # 마지막부터 거꾸로
        katok[i] = katok[i-1] #자리를 바꾸고 
        katok[i-1] = None # 바꾼자리를 None 으로 
    katok[position] = friend #빈 위치에 변수 삽입
    print(katok)

    
    

###########################
# 전역변수
katok = []

###########################
# 메인코드
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('미나')
add_data('사나')
add_data('지효')


insert_data(3,'모모')



    
    