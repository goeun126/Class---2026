# 컨테이너 자료형
# 여러개의 데이터를 묶어서 관리하는 것

fruyt1 = '사과'
fruyt2 = '포도'
fruyt3 = '복숭아'

fruits = ['사과', '포도', '복숭아']
print(f'fruyt:{fruits}')

# 파이썬에서 컨테이너 자료형으로는 
# 리스트(list), 튜플(tuple), 딕셔너리(dictronary)


# 리스트(list) 정의(선언+초기화)
fruyt = ['사과', '포도', '복숭아']

# 인덱스(index): 아이팀에 부여된 아이템 식별 번호
#   0       1        2
# ['사과', '포도', '복숭아']

# 아이템 조회
print(f'fruyt[1]:{fruits[1]}')
print(f'fruyt[2]:{fruits[2]}')
print(f'fruyt[0]:{fruits[0]}')

# 리스트의 길이(아이템 개수)
cnt = len(fruits)
print(f'cnt:{cnt}')

# 리스트의 마지막 아이템의 인덱스 '값은 리스트의 길이 -1'
print(f'last data:{fruits[len(fruits)-1]}')

# 리스트의 전체 데이터 조회
# 리사트는 반복가능한 객체(데이터)임 => 이터러블한 데이터
for f in fruits:
    print(f'fruyt:{fruits}')

for idx, fruits in enumerate(fruits):
    print(f'index:{idx}, fruyt:{fruits}')


# 아이템 삽입
# 리스트 마지막에 삽입
fruits = ['사과', '포도', '복숭아']

fruits.append('수박')
print(f'fruyt:{fruits}')

# 특정 위치 삽입
fruits.insert(2, '멜론')
print(f'fruits:{fruits}')

# 리스트 연결 extend()
list1 = [1, 2, 3]
list2 = [10, 20, 30]

list1.extend(list2)
print(f'list1:{list1}')

# 리스트 연결: +
list3 = list1 + list2
print(f'list3:{list3}')

# 아이템 삭제하기
sports = ['football', 'baseball', 'volleyball', 'basketball']
sports.pop()
print(f'sports:{sports}')

# 특정 위치 아이템 삭제
sports.pop(1)
print(f'sports:{sports}')

# pop()과 비슷하게 사용할수있는 키워드 del
del sports[1]
print(f'sports:{sports}')

# pop() vs del
nums = [1, 2, 3, 4, 5, 6]
deletednum = nums.pop(3)
print(f'deletednum:{deletednum}')

# 특정 아이템 삭제by 아이템
languages = ['c/c++', 'c#', 'java', 'python']
languages.remove('java')
print(f'languages:{languages}')

# remove()을 이용해서 아이팀을 
# 삭제하려는 개수가 2개 이상일시 처음 아이템만 삭제됨.
languages = ['c/c++', 'c#', 'java', 'python', 'java']
languages.remove('java')
print(f'languages:{languages}')

# quiz) 과일 리스트에서 야채를 찾아 삭제
# ['사과', '망고', 당근', '수박', '포토', '참외', '토마토']

fruits = ['사과', '망고', '당근', '수박', '포토', '참외', '토마토']
        
for itemm in fruits:
    if itemm == '당근' or itemm == '토마토':
        fruits.remove(itemm)
print(f'fruits:{fruits}')

# quiz) 합격 여부 판단하기
# 매 과목 100점을 만점으로 하여 매 과목 40이상
# 전과목 평균 60점 이상 득점

# 홍길동 수험생 성적표
# 부동산 개론:55점
# 민법:35점
# 공법:40점
# 제법:65점
# 중개사 법:30점

scores = []

total = 0
underSubject = 0

while True:
    myScores = int(input('점수를 입력하세요 (종료: -1): '))

    # 종료 조건
    if myScores == -1:
        break

    scores.append(myScores)

    # 총점
    total += myScores

    # 과락
    if myScores < 40:
        underSubject += 1

# 평균 계산 (0 나눔 방지)
if len(scores) > 0:
    average = total / len(scores)
else:
    average = 0

print(f'40점 미만 과목수: {underSubject}')
print(f'평균: {average:.2f}')

# 합격 여부
if underSubject > 0 or average < 60:
    print('아쉽습니다. 다음기회에...')
else:
    print('축 합격!!')