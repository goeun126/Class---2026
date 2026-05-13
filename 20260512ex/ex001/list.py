# 컨테이너 자료형(contaner data type) 묶어서 관리시 사용
# list(리스트) / tuple(튜플) / dictionary(딕셔너리)

# list(리스트)
# >>> fruits = ['사과', '포도', '참외', '배', '자두'] 식으로 이용

Frults = ['과일', '포도', '수박', '참외', '배', '복숭아']
tama = input('과일을 입력하세요. ')

if tama in Frults:
        print('가지고있는 과일입니다.')
else:
    print('가지고있는 과일이 아닙니다.')

# 리스트와 데이터
# 리스트에 포함되는 데이터는 어떤 자료형이든 상관없음
# 정수,실수,문자 하나의 리스트로 묶을 수 있음

complexList = [10, 3.14, 'a', 'hello']
# 이렇게 하나의 리스트에 다양한 데이터 타입의 데이터를 넣을수있는 언어는
# python 과 javascrip뿐, java 불가
print(f'complexList:{complexList}')
print(f'type of complexList: {type(complexList)}')

membr = []
print(f'complexList:{membr}')
print(f'type of complexList: {type(membr)}')

# quiz) 참석자 명단 리스트로 선언

arrendList = ['이순철', '김병헌', '김민우', '박찬호', '김민태']
list = input('이름을 입력하세요.')
if list in arrendList:
    print(f'참석')
else:
    print(f'불참')

# how to 리스트의 아이템 조회
# 특정 아이템 조회
          # -7    -6      -5    -4     -3      -2      -1
          # 0      1       2     3      4       5       6
fruits = ['사과', '포도', '참외', '배', '자두', '복숭아', '바나나']
print(fruits[1]) # 리스트에 존재하지않은 IndexError인덱스를 참조하면 에러남

# 리스트 길이(아이템 개수) 조회
# 리스트 길이란 리스트의 아이템 개수를 뜻하는 것 len() 함수를 사용하면 확인 가능
numbers = [1, 2, 3, 4, 5]
print(f'numbers:{numbers}')
print(f'numbers length:{len(numbers)}')

numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# 첫 번째 데이터 조회
print(f'첫 번째 데이터 조회: {numbers[0]}')
# 마지막 데이터 조회
print(f'마지막 데이터 조회: {numbers[len (numbers)-1]}')

# len() 함수는 문자열의 길이를 조회하는데에도 사용됨.
str = 'hellllllllllllllllo'
print(len(str))

# quiz) 입력한 글자 수 확인하기
# 사용자로부터 메세지 입력받고, 입력 받은 문자열 길이를 확인하는 프로그램
message = input('메세지를 입력: ')
msglen = len(message)
print(f'메세지 길이:{msglen}')

# 리스트 전체 데이터 조회
balls = ['야구공','축구공','탁구공','골프공','농구공',]
# print(f'{balls[0]}')
# print(f'{balls[1]}')
# print(f'{balls[2]}')
# print(f'{balls[3]}')
# print(f'{balls[4]}')
for item in enumerate(balls):
    print(f'item:{item}')

balls = ['야구공','축구공','탁구공','골프공','농구공',]
i = 0
while i < len(balls):
    print(f'item: {balls[i]}, index:{i}')
    i += 1

# quiz) 다음 리스트에서 마지막 인덱스 값을 출력하는 프로그램
sports = ['baseball', 'basketbll', 'trnnis', 'goif', 'socer']
lenVar = len(sports) - 1
print(sports[lenVar])

# quiz) 다음 리스트에서 'python' 문자열의 인덱스 값을 출력
languages = ['c/c++', 'c#', 'python', 'java']
for idx, str in enumerate(languages):
    if str == 'python':
        print(f'python idx:{idx}')

targerIdx = languages.index('python')
print(f'targerIdx: {targerIdx}')

# 아이템 기존 리스트에 삽입
# 리스트 마지막에 삽입
sports = ['baseball', 'football', 'volleyball']
print(f'sports:{sports}')

sports.append('baseball')
print(f'sports:{sports}')
print(f'sports lenght: {len(sports)}')

# quiz) 취미 추가하기
# 취미들을 저장할 리스트를 정의하고 사용자가 입력한 취미가 추가되는 프로그램
# 그리고 취미의 개수를 출력
hobboes = []

while True:
    hobby = input('취미 입력:')
    hobboes.append(hobby)
    print(f'현재 입력한 취미: {hobboes}') 
    print(f'총 개수:{len(hobboes)}')
    selectedMenuNumber = int(input('1. 총 현재 개수 2. 취미 추가 3. 종료'))
    num2 = 3
    if selectedMenuNumber == num2:
        break

# 특정 위치에 아이템 삽입
# 리스트의 원하는 위치에 아이템을 삽입할때는 insert() 함수 이용
contries = ['korea', 'china', 'japan']
contries.insert(1,'usa')
print(f'contries:{contries}')

# quiz) 누락된 숫자 추가하기
numbers = [1, 2, 3, 4, 5, 7, 8, 9]
numbers.insert(5, 6)
print(f'numbers:{numbers}')
numbers.insert(9, 10)
print(f'numbers:{numbers}')

# 리스트 연결하기
# 리스트에 또 다른 리스트를 연결할 때는 extend() 함수를 사용합니다.
list1 = [1, 2, 3]
print(f'list1:{list1}')

list2 = [10, 20, 30]
print(f'list2:{list2}')

list1.extend(list2)
print(f'list1:{list1}')

# --------------------------------------
list1 = list1 + list2
print(f'list3:{list1}')

# 리스트 아이템 삭제하기
# 리스트 마지막 아이템 삭제하기
sports = ['baseball', 'football', 'volleyball', 'basketbll']
print(f'sports:{sports}')
sports.pop()
print(f'sports:{sports}')
sports.pop(2)
print(f'sports:{sports}')
removedItem = sports.pop()
print(f'removedItem:{removedItem}')

# pop()대신 del 키워드를 이용해서 아이템 삭제 가능
sports = ['football', 'baseball', 'volleyball', 'basketbll']
del sports[2]
print(f'sports:{sports}')

# quiz) sports 리스트에서 'volleyball'을 삭제하는 프로그램을 만들어보자
sports = ['football', 'baseball', 'volleyball', 'basketbll']

volleyballIdx = sports.index('volleyball')
print(f'sports:{sports}')
sports.pop(volleyballIdx)
print(f'sports:{sports}')
