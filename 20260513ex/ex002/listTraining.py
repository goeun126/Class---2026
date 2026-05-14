# 1.숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기
'''
scores = [3, 7, 1, 9, 5]

max_num = scores[0]

for num in scores:
    if num > max_num:
        max_num = num

print(max_num)

# 2. 사용자에게 숫자 입력받아서
# 1부터 입력한 숫자까지 합계 출력하기 ( 5 )

myNum = int(input('숫자를 입력하시오.'))
num1 = myNum + 1
total = 0

for num in range(1, num1):
    total += num

print(f'{total}')

# 3. 리스트에 있는 숫자 중 짝수만 출력하기
list =  [1,2,3,4,5,6]

for num in list:
    if num % 2 == 0:
        print(f'짝수:{num}')
    else:
        print(f'홀수:{num}')

# 4. 리스트 숫자를 오름차순 정렬하기
list = [5,1,7,3]
list.sort()
print(f'list:{list}')

# 5. 리스트 숫자를 내림차순 정렬하기
list.sort(reverse=True)
print(f'list:{list}')

# 6. 리스트 안 숫자의 평균 구하기

list = [10,20,30]

list2 = sum(list)
list3 = len(list)
print(f'list:{list2 / list3}')

# 7. 리스트에서 가장 작은 숫자 찾기

scores = [3, 7, 1, 9, 5]

max_num = scores[0]

for num in scores:
    if num < max_num:
        max_num = num

print(max_num)

# 8. 1부터 100까지 숫자 중 3의 배수와 5의 배수 출력하기

num = range(1,100)

for num in range(1,100):

    if num % 3 == 0:
        print(f'3의 배수: {num}')
    elif num % 5 == 0:
        print(f'5의 배수: {num}')

# 9. 사용자가 입력한 숫자를 리스트에 저장하다가 0 입력하면 종료 후 리스트 출력하기

num = []

while True:
    user = int(input('숫자를 입력하세요. 0입력시 종료'))

    if user == 0:
        print('종료')
        break

    num.append(user)
    print(f'현재까지 입력한 숫자:{num}')


print(f'입력한 숫자:{num}')
print(f'입력한 모든 숫자의 합계: {sum(num)}')
'''
# 출석부 관리 시스템
# 이번에 만들 출석부 관리 시스템은 리스트를 이용해서 학급의 학생 명단을 관리하는 프로그램, 
# 시나리오에 따라 프로그래밍을 전개, 예제가 쉬운 만큼 시나리오만 보고 직접 코딩해 보는 것을 추천
# [[ 시나리오 ]]
#1 :  학급 학생수가 10명(정우람, 박으뜸, 배힘찬, 천영웅, 신석기, 배민규, 전민수, 박건우, 박찬호, 이승엽)인 리스트를 만든뒤
#2 :  ‘가나다’ 순으로 정렬한다.
#3 :  ‘박찬호’ 학생이 전학을 가게 되었다. 출석부에서 삭제한 후 전체 학생과 학생 수를 출력
#4 :  선생님을 돕기 위한 학생으로 앞에서 3명을 뽑는다.
#5 :  새로운 친구가 전학 왔다. 이름은 ‘이병규’이다.
#6 :  자리를 바꾸기 위해서 학생 순서를 역순으로 뒤집는다.
#7 :  ‘정우람’ 학생이 이름을 ‘정잘남’으로 개명했다.

# #1
students = ['정우람', '박으뜸', '배힘찬', '천영웅', '신석기', 
            '배민규', '전민수', '박건우', '박찬호', '이승엽']
print(f'students:{students}')

# #2
students.sort()
print(f'students:{students}')

# #3
students.remove('박찬호')
print(f'students:{students}')
print(f'students count:{len(students)}')

# #4
studentsFoeHelp = students[:3]
print(f'studentsFoeHelp:{studentsFoeHelp}')

# #5
students.append('이병규')
students.sort()
print(f'students:{students}')
print(f'students count:{len(students)}')

# #6
students.sort(reverse=True)
print(f'students:{students}')

# #7
idx = students.index('정우람')
students[idx] = '정잘남'
print(f'students:{students}')

# 혈액 보관 시스템
# 헌혈 프로그램 통해서 10명의 기부자에게 혈액을 받아 리스트에 보관,
# 보관하고있는 혈액형 종류별로 몇팩씩 보유하고 있는지 한분에 보여주는 프로그램

LOOP_COUNT = 10
bloods = []

for i in range(LOOP_COUNT):
    print('헌혈해주셔서 감사합니다. 혈액형을 선택 하세요. (A, B, AB, O)')
    bloods.append(input())


print(f'bloods:{bloods}')
print('-' * 30)
print(f'형액형\t|개수')
print('-' * 30)
print(f'A형\t:{bloods.count('A')}')
print(f'B형\t:{bloods.count('B')}')
print(f'AB형\t:{bloods.count('AB')}')
print(f'O형\t:{bloods.count('O')}')
print('-' * 30)

