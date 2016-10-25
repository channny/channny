import random

"""
# 문서 설명
####### 컴퓨터와 가위바위보 대결하기 #######
생성 날짜 : 2016.10.12
작성자 : 권 채은
사용 언어 : Python
"""

def RSP() :

	user_count = 0
	com_count = 0

	for i in range(10):
		print(i+1,"번째 경기 입니다.")
		user = int (input("1 = 가위, 2 = 바위, 3 = 보 "))
		com = random.randrange(1,4)
		if user == com :
			pass
		else if user + 1 ==  com or user == com + 2 :
			com_count += 1
		else :
			user_count += 1
		print(i+1,"번째 경기가 종료되었습니다.)
	print(user_count : com_count)					
	if(user_count>com_count) :
		print("최종적으로 사용자가 승리하였습니다 !")
	else :
		print("최종적으로 컴퓨터가 승리하였습니다 !")

	print("종료되었습니다 !)
RSP()

"""
변수
	user_count : 사용자가 이긴 횟수를 저장
	com_count : 컴퓨터가 이긴 횟수를 저장
	user : 사용자가 선택한 패를 저장
	com : 컴퓨터에서 랜덤으로 선택된 패를 저장
시나리오
	user_count와 com_count 를 0으로 초기화 한다
		사용자의 패는 input으로 입력받고 컴푸터의 패는 랜덤으로 선택한다.
	
		1. com 과 user 가 같은 경우에는 아무 일도 일어나지 않는다.
		2.com이 user보다 1 또는 2 크면 컴퓨터가 이겼으므로 "컴퓨터 승"을 출력하고 com_count 를 1만큼 늘린다.
		3. 1,2의 경우가 아니라면 사용자가 이겼으므로 "사용자 승"을 출력하고 user_count 를 1만큼 늘린다.
	for 문을 사용해서 10번 반복한다.
	for문이 끝나면 user_count 와 com_count를 비교해 최종적인 승자를 출력한다.

	+-------------------+--------------------+--------------------+
	|      비김          |       사용자 승      |     컴퓨터 승         |
	+===================+====================+====================+
	| 아무일도 일어나지 않음  |    user_count ++   |     com_count ++.  |
	+                   +--------------------+--------------------+
	|                   |   print(사용자 승)   |     print(컴퓨터 승)  |
	+-------------------+--------------------+--------------------+



"""
