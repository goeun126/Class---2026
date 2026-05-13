# quiz) 369 게임 만들기
# 1부터 99까지 1씩 증가하면서 숫자에 3,6,9가 들어가있을 때마가 짝을 출력

for num in range(1, 100):

    if num <= 9:                # 1의 단위
        if num % 3 == 0:
            # print(f'{num}, 짝!')
            print(num, ', 짝!', end='')
        else:
            print(num, end='')
    else:                       # 10의 단위 
        # print(f'{num}')       # 12 > 1, 2 : 16 > 1, 6 : 99 > 9, 9
        # printStr = str(num)
        print(num, end='')

        firstNum = num // 10    # 15 > 15 // 10 -> 1
        secondNum = num % 10    # 15 > 15 % 10  -> 5, 30 > 0

        if firstNum % 3 == 0:
            # print(f'짝!')
            # printStr += ', 짝!'
            print(', 짝!', end='')

        if secondNum % 3 == 0 and secondNum != 0:
            # print(f'짝!')
            # printStr += ', 짝!'
            print(', 짝!', end='')
        
    print()


# quiz) 열차 교차 시간 알아내기
# 대전역에는 3개의 노선의 열차가 9시~6시까지 교차 운행 함
# 3대의 열차가 교차하는 시간을 구해 충돌사고 안나게 해야함
# 단 매일 오전 9시에 대전역에서 모든 열차가 출발함.

# A열차: 첫치 오전 9시 | 마지막 오후 6시 | 운행간격 10분
# B열차: 첫치 오전 9시 | 마지막 오후 6시 | 운행간격 25분
# C열차: 첫치 오전 9시 | 마지막 오후 6시 | 운행간격 30분

trainA = 10
trainB = 25
trainC = 30

for n in range(1, 541):
    if n % trainA == 0 and n % trainB == 0 and n % trainC == 0:
        print('trainA <-> trainB <-> trainC')
        # print(9 + n // 60, end='')        #시
        # print('시', end='')
        # print(n % 60, end='')
        # print('분')
        print(f'{9 + n // 60}시 {'00'if n % 60 == 0 else str (n % 60)}분')
    elif n % trainB == 0 and n % trainC == 0:
        print('trainA <-> trainB')
        # print(9 + n // 60, end='')        #시
        # print('시', end='')
        # print(n % 60, end='')
        # print('분')
        print(f'{9 + n // 60}시 {'00'if n % 60 == 0 else str (n % 60)}분')
    elif n % trainC == 0 and n % trainA == 0:
        print('trainA <-> trainB')
        # print(9 + n // 60, end='')        #시
        # print('시', end='')
        # print(n % 60, end='')
        # print('분')
        print(f'{9 + n // 60}시 {'00'if n % 60 == 0 else str (n % 60)}분')
    elif n % trainA == 0 and n % trainB == 0:
        print('trainA <-> trainB')
        # print(9 + n // 60, end='')        #시
        # print('시', end='')
        # print(n % 60, end='')
        # print('분')
        print(f'{9 + n // 60}시 {'00'if n % 60 == 0 else str (n % 60)}분')

# quiz) 로그인 기능 만들기
# 암호를 입력하면 틀릴경우 '암호를 다시 확인하세요.' 를 출력하고 5회이상 실패할시 
# 로그인 실패 횟수 초과 라는 메세지 출력후 종료 (암호: dwac1234)
ADMIN_PW = 'dwac1234'
count = 1

while True:
 
    if count > 5:
        print(' 로그인 실패')
        break

    inputPw =  input('관리자 암호를 입력하세요. ')

    if inputPw != ADMIN_PW:
        print('암호를 다시 확인하세요.')
        count += 1

    elif inputPw == ADMIN_PW:
        print('로그인 성공')
        break


# quiz) 사용자가 입력한 양수를 이용해 팩토리얼 값을 구하는 프래그램
# 팩토리얼 (factoral, !) n!은 1부터 양의 정수n까지의 모든 정수를 곱한값
# ex) 4!은 1x2x3x4 = 24이다.

userInputIntegerData = int(input('양수 입력:'))
result = 1

for num in range(1, userInputIntegerData + 1):
    result *= num
print(f'{userInputIntegerData}의 팩토리얼은 {result}이다.')

# quiz) 숫자 맞추기 게임
# 0부터 100사이의 난수를 발생시키고 사용자가 난수맞힐때까지 계속 물어보는 게임
# 1부터 100까지 난수 발생
# 난수와 일치하면 정답 출력후 게임 종료
# 난수와 일치 하지않으면 틀렷습니다. 다시 입력하세요 출력
# 기회는 10횔 제한 게임에 졋습니다.게임을 종료
# 사용자가 틀릴때다 난수를 비교해서 크고 작음을 알려줌
# 게임이 종료하기 전 난수 출력

import random
randNum = random.randint(1, 100)
count = 0

while True:

    myRandNum = int(input('난수를 입력하세요.'))
    count += 1
    
    if myRandNum == randNum:
     print('정답입니다.')
     break

    elif count >= 10:
     print('틀렸습니다.')
     break

    elif myRandNum > randNum:
        print('난수보다 수가 큼니다.')
    
    else:
        print('난수보다 수가 작습니다.')

print(f'정답:{randNum}')
        

import random


randomNum = random.randint(1, 100)


for chance in range(1, 11):

    userInputIntData = int(input('숫자를 입력하세요: '))

    print(f'{chance}번째 시도')
    
    if chance > 10: 
        print('게임에 졌습니다.')
        print(f'정답: randomNum')
        break

    elif userInputIntData == randomNum:
        print('정답입니다.')
        break

    elif userInputIntData > randomNum:
        print(f'{userInputIntData}: 보다 작습니다.')

    elif userInputIntData < randomNum:
        print(f'{userInputIntData}: 보다 큽니다.')


print(f'정답: {randomNum}')


import random
randomNum = random.randint(1, 100)

userNum = int(input('1~100의 숫자를 입력하세요. '))
count = 1
while True:
    if randomNum == userNum:
        print('정답입니다.')
        break

    elif randomNum < userNum:
        print('틀렸습니다. 다시 입력하세요.DOWN ')
    elif randomNum > userNum:
        print('틀렸습니다. 다시 입력하세요.UP')
    
    userNum = int(input('1~100의 숫자를 입력하세요. '))
    count += 1
    
    if count > 10:
        print('게임에 졌습니다.')
        break

print(f'randomNum')

# quiz) 다음 요구조건을 참고하여 
# 가로 세로 변화에 따른 사각형의 넓이를 구하는 프로그램
# 가로길이 1부터 2의 배수로 증가
# 세로길이는 1부터 3의 배수로 증가
# 사각형의 넓이가 150보다 크면 프로그램 종료
# 가장 작은 사각형과 큰 사각형의 넓이를 출력.

width = 1
height = 1

minArea = width * height
mxnArea = width * height

while True:

    area =  width * height
    if area > 150:
       break

    print(f'가로:{width}, 세로:{height}, 넓이:{area}')

    if area < minArea:
        minArea = area
    
    if area > mxnArea:
        mxnArea = area

    if width == 1:
        width = 2
    else:
        width += 2
    
    if height == 1:
        height = 3
    else:
        height += 3

print(f"가장 작은 넓이:{minArea}")
print(f"가장 큰 넓이:{mxnArea}")
