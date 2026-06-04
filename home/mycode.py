'''
forest = '숲'
cave = '동굴'

print('앞에 두갈래길이 있습니다. 어떤길로 가시겠습니까?')
choice = input("선택: ")


if choice == '1':
    print(f'{forest}으로 들어갔습니다!')
    print(f'{forest}들어오니 앞에 슬라임이 있다!')
if choice == '2':
    print(f'{cave}로 들어갓습니다!')
    print(f'{cave}들어오니 앞에 고블린이 있다!')


print('칼은1번 마법은 2번 어떤 걸로 공격하시겠습니까?')
choice1 = input("공격 선택: ")

if choice1 == '1':
    print('칼 공격!')
    print('몬스터에게 -10hp !')

if choice1 == '2':
    print('마법 공격!')
    print('몬스터에게 -20hp !')


print('몬스터가 공격할 준비를 하고있다!')
print('회피,방패 중 어떤걸 선택하시겠습니까?')
choice2 = input("선택: ")

if choice2 == '회피':
    print('민첩한 발놀림으로 공격을 회피 했습니다!')
    print('데미지를 받지 않았습니다.')

if choice2 == '방패':
   print('방패를 들어 방어했습니다!')
   print('데미지를 거의 받지않았습니다.')


print('다시 당신이 공격할 차례입니다.')
print('칼은1번 마법은 2번 어떤 걸로 공격하시겠습니까?')
choice1 = input("공격 선택: ")

if choice1 == '1':
    print('칼 공격!')
    print('몬스터에게 -10hp !')

if choice1 == '2':
    print('마법 공격!')
    print('몬스터에게 -20hp !')

print('성공적으로 몬스터를 해치웠다!')

money = int(input('돈: '))
xp = int(input('경험치: '))

print(f'{(money):,}골 과 {(xp):,}xp 를 획득했다!')


number = int(input('숫자를 입력하세요. '))
if number > 0:
    print(f'양수')
if number == 0:
    print(f'0입니다.')
if number < 0:
    print(f'음수')


age = int(input('나이를 입력하세요.'))
if age >= 20:
    print(f'성인')
elif age >= 14:
    print(f'청소년')
else:
    print(f'어린이')


ID = (input('ID: '))
PW = int(input('PW: '))
id = 'admin'
pw = 1234

if ID == id:
    if PW == pw:
     print('로그인 성공')
elif PW != pw:
     print('비밀번호 오류')
else:
   print('아이디 없음')



age = int(input('나이를 입력 하세요: '))
height = int(input('키를 입력하세요: '))
onehundred = 100
oneHunDredForty = 140

if age >=65 or age < 3:
    print('무료입장 가능합니다.')
else:
    if height >= oneHunDredForty:
        print('12,000원')
    elif height >= onehundred:
        print('8,000원')
    else:
        print('5,000원')


for num in range(1, 31):
    if num  % 2 == 1:
        print(f'num:{num}')

for num in range(1, 51):
    if num % 3 == 0:
        print(f'num:{num}')

num2 = 0

num2 = 0

for num in range(1, 21):
    if num % 2 == 0:
     num2 += 1
    print(f'{num2}')

for num in range(1, 14, 3):
    print(f'num:{num}')

num2 = 0
for num in range (50, 1, -1):
   num2 = num2 + num
print(f'{num2}')

name = input('이름을 입력: ')
print(f'안녕하세요. {name}님!')

animal = ['강아지', '토끼', '고양이']
name = input('이름을 입력: ')
if name in animal:
    print('있습니다.')
else:
    print('없습니다.')

num = 10
myNum = int(input('숫자: '))
if myNum > num:
    print('큰 수')
else:
    print('작은 수')

pw = 1234
password = int(input('비밀번호를 입력하세요: '))
result = '합격' if pw == password else '불합격'
print(f'resilt:{result}')

name1 = ['김철수', '이영희', '박똥개', '홍길동', '개차반']
name2 = input('이름을 입력하세요: ')

if name2 in name1:
    print('친구입니다')
else:
    print('친구가 아닙니다')

animal = ['강아지', '토끼', '고양이']
name = input('이름을 입력: ')
if name in animal:
    print('있습니다.')
else:
    print('없습니다.')

num = 10
myNum = int(input('숫자: '))
if myNum > num:
    print('큰 수')
else:
    print('작은 수')

color = ['red', 'blue', 'green']
mynumber = int(input('1.red 2.blue 3.green'))
target = color[mynumber - 1]
number = color.index(target)
print(f'{number}')

fruit = []
myFruit = input('추가할 과일을 입력하세요.')
fruit.append(myFruit)
print(f'{fruit}')

english = ['a', 'b', 'c']
english.append('item')
print(f'english:{english}')

snackFood = ['김밥', '라면', '떡볶이']
for item in enumerate(snackFood):
    print(f'{item}')

name1 = ['김철수', '이영희', '박똥개', '홍길동', '개차반']
name2 = input('이름을 입력하세요: ')

if name2 in name1:
    print('친구입니다')
else:
    print('친구가 아닙니다')

color = ['red', 'blue', 'green']
myColor = int(input('1.red 2.blue 3.green'))
colorIdx = 0

if myColor == 1:
    colorIdx = color.index('red')
elif myColor == 2:
    colorIdx = color.index('blue')
elif myColor == 3:
    colorIdx = color.index('green')

print(f'colorIdx: {colorIdx}')

shoppingCart = []

while True:
    mynumber = input('물건 입력:')
    shoppingCart.append(mynumber)
    print(f'현재 구매한 목록{shoppingCart}')
    shopping  = int(input('1.계속 구매 2. 종료'))
    num = 2
    if shopping == num:
        break

import random
randNum = random.randint(1, 50)
count = 0

while True:

    myRandNum = int(input('난수를 입력하세요.'))
    count += 1


    if count >= 7:
        print(f'실패! 정답은{randNum}입니다.')
        break

    elif myRandNum == randNum:
        print('정답입니다!')
        print(f'{count}번 만에 맞췄습니다.')
        break

    elif myRandNum < randNum:
        print('더 큰 수입니다.')

    elif myRandNum > randNum:
        print('더 작은 수입니다.')

    print(f'{count}번째 시도')


# 프로그램 요구사항
# 1.현재 자리 상태를 전부 출력하기
# 2. 사용자에게 원하는 자리 번호 입력받기
# 3.예약할 자리 번호 :
#   빈자리라면 "예약 완료" 출력 해당 자리 상태를 "사용중" 으로 변경 이미 사용중이라면 이미 사용중인 자리입니다 출력
# 5.예약 후 전체 자리 상태 다시 출력하기

seats = {
    1: "빈자리",
    2: "사용중",
    3: "빈자리",
    4: "사용중",
    5: "빈자리"
}

for key, value in seats.items():
    print(f'자리 번호:{key}, 상태:{value}')

userSeat = int(input('원하는 자리를 입력하세요.'))

if seats[userSeat] == "빈자리":
   seats[userSeat] = '사용중'
   print('예약이 완료되었습니다.')
else:
    print('사용중인 자리입니다.')

print(f'현재 자리상태:{seats}')


# 프로그램 요구사항

# 1. 학생 점수를 5개 입력받기
# 2. 모든 점수 출력하기
# 3. 가장 높은 점수 출력하기
# 4. 평균 점수 출력하기
# 5. 80점 이상인 학생 수 출력하기
# 6. 프로그램 종료 전 총합 출력하기

scores = []

for index in range(5):
    userScore = int(input('학생 점수를 입력하세요.'))
    scores.append(userScore)
    print(f'전체 점수:{scores}')
    
    max_scores= max(scores)
    print(f'최고점수:{max_scores}')

    totalScores = sum(scores)
    highCount = 0
    if userScore >= 80:
        highCount += 1

print(f'총합 : {totalScores}')
print(f'평균 점수: {totalScores / len(scores)}')
print(f'80점 이상 학생수:{highCount}')

# 1. 과일 가격을 딕셔너리에 저장하기
#   - 사과: 1500원
#   - 바나나: 1000원
#   - 딸기: 3000원
# 2. 사용자에게 각 과일 구매 개수 입력받기
# 3. 각 과일별 구매 금액 출력하기
#   (가격 × 개수)
# 4. 총 구매 금액 출력하기
# 5. 가장 비싼 과일 이름 출력하기 (가격 기준)

fruitPrice = {
    '사과':1500,
    '바나나':1000,
    '딸기':3000
}

totalFruit = 0

def apple():
    global totalFruit
    totalFruit += fruitPrice['사과'] * apple_count
    print(f'사과 구매 금액: {apple_count * fruitPrice['사과']}')

def banana():
    global totalFruit
    totalFruit += fruitPrice['바나나'] * banana_count
    print(f'바나나 구매 금액: {banana_count * fruitPrice['바나나']}')

def strawberry():
    global totalFruit
    totalFruit += fruitPrice['딸기'] * strawberry_count
    print(f'딸기 구매 금액: {strawberry_count * fruitPrice['딸기']}')


apple_count = int(input('사과 구매 개수:'))
banana_count = int(input('바나나 구매 개수:'))
strawberry_count = int(input('딸기 구매 개수:'))

apple()
banana()
strawberry()

print(f'사과 구매 개수:{apple_count}개')
print(f'바나나 구매 개수:{banana_count}개')
print(f'딸기 구매 개수:{strawberry_count}개')

print(f'총 금액: {totalFruit}원')
maxPriceFruit = max(fruitPrice, key=fruitPrice.get)
print(f'가장 비싼 과일: {maxPriceFruit}')

# 1. 음식 가격을 딕셔너리에 저장
#    - 햄버거: 5000원
#    - 감자튀김: 3000원
#    - 콜라: 1500원

menuPrice = {
    '햄버거':5000,
    '감자튀김':3000,
    '콜라':1500
}
# 2. 각각 함수 만들기 (def 사용)
# 3. 각 함수는 다음을 해야 함:
#    - 개수 입력받기
#    - 총 금액 계산 (가격 x 개수)
#    - 출력하기
def hamburger():
    return menuPrice['햄버거'] * burger_count

def fries():
    return menuPrice['감자튀김'] * fries_count

def coke():
    return menuPrice['콜라'] * coke_count

burger_count = int(input('햄버거 구매 개수: '))
fries_count = int(input('감자튀김 구매 개수:'))
coke_count = int(input('콜라 구매 개수'))

print(f'햄버거 총 금액:{burger_count * menuPrice['햄버거']}원')
print(f'감자튀김 총 금액:{fries_count * menuPrice['감자튀김']}원')
print(f'콜라 구매 개수 총 금액:{coke_count * menuPrice['콜라']}원')

burger_total = hamburger()
fries_total = fries()
coke_total = coke()

total = burger_total + fries_total + coke_total

# 4. 전체 총 금액 출력하기

print(f'총 금액{total}원')

# 수학시험 프로그램
# 다음은 수학시험 문제 및 정답입니다.
# 튜플에 문제를 저장하고 사용자가 답을 입력하면 채점하는 프로그램을 만들어봅시다. 

# -------------------------------------------
# 문제               정답            점수
# -------------------------------------------
# 3+2                 5              3점
# 5/2의 몫            2              5점
# 10-2                8              3점
# 100 x 2            200             5점
# 1=(10/4의 나머지)   -1             5점
# 2의 4제곱           16             3점
# 4/2                 2              3점
# ------------------------------------------


quiz = (
    ['3+2', 5, 3],
    ['5/2의 몫', 2, 5],
    ['10-2', 8, 3],
    ['100 x 2', 200, 5],
    ['1=(10/4의 나머지)', -1, 5],
    ['2의 4제곱', 16, 3],
    ['4/2', 2, 3],  
)
answerCount = 0
totalScore = 0
wrongCount = 0

for item in quiz:               # 첫 번째 반복시행
    print(f'문제: {item[0]}')
    answer = int(input('정답 입력:'))
    if answer == item[1]:
        answerCount += 1
        totalScore += item[2]
    else :
        wrongCount += 1

print('-'*25)       
print(f'맞힌 개수: {answerCount}')
print(f'틀린 개수: {wrongCount}')
print(f'총점: {totalScore}')
print('-'*25) 



# for key in classes.keys():
# if days in allowance:
# for key in allowance: (전수 조사)
# if days in allowance: (확인 및 직행)

# 1. 회원가입 2.프로그램 종료

flag = True
members = {}

while flag:

    userInputNum = int(input('1. 회원가입   2.프로그램 종료'))
    if userInputNum == 1:
        id = input('아이디:')
        pw = input('비밀번호')
        members[id] = pw               # 아이디는 중복되면 안 되니까 key값으로 쓴다
    elif userInputNum == 2:
        flag = False

        for key in members.keys():
            print(f'ID: {key}, PW: {members[key]}')
print()

# 3학점인 과목을 모두 5학점으로 변경하는 프로그램

classes =  {'python':'5학점', 'C/C++':'5학점', 'HTML5':'3학점', 'Java':'5학점', 'Javascript':'3학점'}

for key in classes.keys():           # for key in classes
    if classes[key] == '3학점':            # 이건 true or false
       classes[key] = '5학점'             #  변수 
print(classes)

members = {
    '2019-052001':['박찬호', '25', 'M', '010-1234-5678', '헬스' '수영', 0],
    '2019-052004':['박용택', '65', 'M', '010-9012-3456', '수영', 50],
    '2019-052003':['박세리', '70', 'W', '010-7890-1234', '아쿠아로빅', 50],             
}


# 전체 회원 정보 출력
for key in members:
    print(f'회원번호: {key}, 회원정보: {members[key]}')

print('-'*30)

# 전체 회원 정보를 출력을 하는데, 이 때 회원의 '이름'과 '성별'만 출력을 하자

for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value[0]},{value[1]}')

members = {
    '2019-052001': {
        '이름': '박찬호',
        '나이': 25,
        '성별': 'M',
        '연락처': '010-1234-5678',
        '이용서비스': ['헬스', '수영'],                 # 따옴표 따로 따로 해줘야함
        '할인율': 0
    },                    #컴마 있어야함
    '2019-052004': {
        '이름': '박용택', 
        '나이': '65', 
        '성별': 'M', 
        '연락처': '010-9012-3456',
        '이용서비스': ['수영'],
        '할인율': 50,
    },
    '2019-052003':{
        '이름': '박세리', 
        '나이': 70,
        '성별': 'W', 
        '연락처': '010-7890-1234',
        '이용서비스': ['아쿠아로빅'],
        '할인율': 50,   
    }              
}

# 회원정보를 출력하는데 이름 성별 이용서비스 그리고 이용서비스개수 만 출력을 하자!

for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별: {value['이름']}, {value['성별']}, {value['이용서비스']}, {len(value['이용서비스'])}')


vagetables = {
    '당근': {
        '입고량' : 11,
        '소비량' : 1,
        '재고량' : 0,
    },
    '건대추': {
        '입고량' : 100,
        '소비량' : 10,
        '재고량' : 0,
    },
    '대파': {
        '입고량' : 20,
        '소비량' : 1,
        '재고량' : 0,
    },
    '애호박': {
        '입고량' : 3,
        '소비량' : 1,
        '재고량' : 0,
    },
    '부추': {
        '입고량' : 10,
        '소비량' : 1,
        '재고량' : 0,
    },
}   

current = 0 

for key, value in vagetables.items():
    current = value['입고량'] - value['소비량']
    value['재고량'] = current
    print(f"채소명: {key},\t : 입고: {value['입고량']},\t 소비: {value['소비량']},\t 재고량 : {current}")


# 용돈 기입장 

allowance = {
    '월': {
        '수입' : 0,
        '지출' : 0,
        '잔액' : 0,
    },
    '화': {
        '수입' : 0,
        '지출' : 0,
        '잔액' : 0,
    },
    '수': {
        '수입' : 0,
        '지출' : 0,
        '잔액' : 0,
    },
    '목': {
        '수입' : 0,
        '지출' : 0,
        '잔액' : 0,
    },
    '금': {
        '수입' : 0,
        '지출' : 0,
        '잔액' : 0,
    },
    '토': {
        '수입' : 0,
        '지출' : 0,
        '잔액' : 0,
    },
    '일': {
        '수입' : 0,
        '지출' : 0,
        '잔액' : 0,
    },
}   

totalIncome = 0
totalOutcome = 0
totalBudget = 0

while True:
    selectedNum = int(input('1. 기입   2. 종료'))
    if selectedNum == 2 :
     
        print('종료합니다.')
        print(allowance)
        break
    
    days = str(input('요일 입력:'))     
    income = int(input('받은 용돈:'))
    outcome = int(input('지출 금액:'))
    budget = income - outcome 
    

    if days in allowance:
            
            allowance[days]['수입'] = income
            allowance[days]['지출'] = outcome
            allowance[days]['잔액'] = budget

            totalIncome += income
            totalOutcome += outcome 
            totalBudget += income - outcome   
    else:
        print('다시 입력해 주세요')
    
    print(f" {days} :  수입: {totalIncome}, 지출 :{totalOutcome}, 남은 돈: {totalBudget}")

   
# 결론부터 말씀드리면, break는 "지금 당장 즉시 탈출!", 
# flag = False는 "이번 바퀴까지만 돌고 다음에는 들어오지 마!"라는 뜻입니다.


# : 용돈 기입장 :::::
from datetime import datetime

MENU_INCOME     = 1
MENU_EXPENSE    = 2
MENU_VIEW       = 3
EXIT            = 99

flag = True
DEV_MOD = True

bankAccount = []
currentMoney = 0

if DEV_MOD:
    txt =  '[2026-05-15 15:14:08] \t 100 \t\t aaaaa \t\t 100'
    bankAccount.append(txt)
    txt = '[2026-05-15 15:15:08] \t 200 \t\t bbbbb \t\t 300'
    bankAccount.append(txt)
    txt = '[2026-05-15 15:16:08] \t\t -50 \t ccccc \t\t 250'
    bankAccount.append(txt)

while flag:

    selectedMenuNum = int(input('1.수입    2.지출    3.조회    99.시스템종료 -----> '))
    if selectedMenuNum == MENU_INCOME:
        incomeMoney = int(input('수입 금액: '))
        incomeDesc = input('수입 내용: ')
        currentMoney += incomeMoney

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        txt = f'[{now}] \t {incomeMoney} \t {incomeDesc} \t\t\t {currentMoney}'
        bankAccount.append(txt)

    elif selectedMenuNum == MENU_EXPENSE:
        expenseMoney = int(input('지출 금액: '))
        expenseDesc = input('지출 내용: ')
        currentMoney -= expenseMoney

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        txt = f'[{now}] \t\t\t -{expenseMoney} \t {expenseDesc} \t {currentMoney}'
        bankAccount.append(txt)

    elif selectedMenuNum == MENU_VIEW:
        print('-' * 63)
        print('날짜&시간 \t\t 입금 \t 출금 \t 내역 \t\t 잔액')
        print('-' * 63)
        for item in bankAccount:
            print(item)
        print('-' * 63)

    elif selectedMenuNum == EXIT:
        flag = False 
'''

import random

food =  ['카', '소', '파']

food = random.choice(food)
print(f'{food}')