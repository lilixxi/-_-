def add_data(friend):
    katok.append(None)  # 빈칸추가
    katok[-1] = friend  # 마지막칸에 추가
    print(katok)

# 데이터 삽입


def insert_data(position, friend):
    katok.append(None)  # 빈칸추가
    # 마지막 친구부터 삽입할 위치까지 한칸씩 뒤로 이동
    for i in range(len(katok)-1, position, -1):  # 마지막부터 거꾸로
        katok[i] = katok[i-1]  # 자리를 바꾸고
        katok[i-1] = None  # 바꾼자리를 None 으로
    katok[position] = friend  # 빈 위치에 변수 삽입
    print(katok)


def delete_data(position):
    katok[position] = None  # 그 자리를 비워주고
    for i in range(position+1, len(katok)):  # 그 다음자리부터, 리스트의 길이까지
        katok[i-1] = katok[i]  # i 위치의 값을 그 앞칸으로 옮기고
        katok[i] = None  # 전칸을 지운다
    del katok[-1]  # 그럼 맨 마지막 자리가 비워지는데 그 자리를 삭제
    print(katok)


katok = []
select = -1  # 숫자 선택용

# main code
while select != 4:
    select = int(input("1:add / 2:insert /3.delete /4.exit  -> "))

    if select == 1:
        data = input("추가할 데이터 -->")
        add_data(data)
        print(katok)
    elif select == 2:
        position = int(input("삽입할 위치 -->"))  # 변수명 수정
        data = input("추가할 데이터 -->")
        insert_data(position, data)
        print(katok)
    elif select == 3:
        position = int(input("삭제할 위치 -->"))  # 변수명 수정
        delete_data(position)
        print(katok)
    elif select == 4:
        print(' 종료합니다.. 현재갑 출력')
        print(katok)
    else:
        print('1-4 번중으로 골라주세요')
        continue