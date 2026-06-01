# 나눗셈 연산자(/)

print(10 / 2)
print(3.14 / .5)

#quiz) 신체질량 지수(BMI)구하기
# 몸무게와 신장을 입력하면 신체질량 지수(BMI) 를 계산해주는
# 프로그램을 만들어 보자(BMI = 몸무게(kg) / 신장의 제곱(m2))

weight = float(input('뭄무게(kg): '))  #소수점이기때문에 float 들어감
height = float(input('신장(m): '))
bmi = weight / (height * height)
print(f'BMI: {bmi:.2f}')     #소수점 자리 확인


# 숫자 0을 어떤 수로 나누어도 결과는 항상 0이다.
print(0 / 123)

# 어떤 숫자를 0으로 나눌 수 없다. -> 에러
print(10 / 0)      #ZeroDivisionError


#나머지(%)
print(10 % 2)
print(10 % 3)

#quiz) 홀짝 게임하기
# 주면 쥔손을 상태방에게 내밀며 손 안에 동전 개수가 홀수인지 짝수인지 맞추는 게임입니다.
# 손 안에 동전 개수를 입력하면 Wkrtnsms0, 홀수는 1을 출력하는 프로그램을 만들어봅시다.
inpuData = int(input('손 안에 동전수를 입력하세요.'))
result = inpuData % 2
print(result)


#몫(//)
print(10 // 3)
print(6 // 2)

#quiz) 빵을 나누어 줄 수 잇는 학생 수 구하기
# 97개의 빵을 3개씩 나누어 주려고 함
# 최대 몇명 까지 줄 수 있는지 구하고, 남는 빵의 개수를 구하시오
bread = 97
breadCnt = 3
maxFriendCnt = bread // breadCnt
print(f'빵을 나누어 줄 수 있는 학생 수:{maxFriendCnt}')

restBreadCnt = bread % breadCnt
print(f'남는 빵 개수: {restBreadCnt}')

#거듭제곱(**)
print(2**2)
print(2**3)
print(2**10)

#quiz) 점염병 예상 감염자 수 구하기
# 하루에 한 사람이 한명씩 감염되고있음
# 확진자 한 사람이 나올 경우 30일 이후에 몇 명의 감염자가 나오는지 계간하기
man = 2
date = 30
total = man ** date
print(f'{date}일 이후 예상 감염자 수:{total}')