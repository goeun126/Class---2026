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
'''
