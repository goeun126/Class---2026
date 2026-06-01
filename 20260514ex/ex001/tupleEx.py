# 튜플 선언하는 방법은 리스트와 같으나 [] 대신 () 를 씀

fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')
print(f'fruits:{fruits}')
print(f'fruits type:{type(fruits)}')


# 튜플 조회
# 튜플은 아이템의 수정이 불가능하기 때문에 삽입, 삭제, 정렬등의 기능 x
# 조회하는 기능만 있음

fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')
print(f'fruits[3]:{fruits[3]}')

# quiz) 튜플에서 인덱스가 홀수인 아이템 조회하기
sports = ('태권도', '야구', '농구', '축구', '배구', '권투', '양궁')

for idx, item in enumerate(sports):
    if idx % 2 == 0:
        print(f'idx:{idx},item:{item} ')


# 특정아이템의 인덱스 조회
# 인덱스 사용 index()

fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')
print(f'idx:{fruits.index('바나나')} ')

# quiz) 아이템 값으로 인덱스 출력
# names 튜플에서 사용자가 원하는 이름을 입력하면 이름에 해당하는 인덱스 출력

names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')

inputData = input('선수 이름 입력: ')
print(f'이름:{inputData}, 인덱스:{names.index(inputData)}')

# 튜플 안의 아이템 유/무 확인
# in과 not in 키워드를 사용하면 튜플안에 특정 아이템의 존재 유/무를 확인할 수 있음.
colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
print(f'{'Green+' in colors}')

if 'Green' in colors:
    print('colors에는 Green이 있습니다.')

else:
    print('colors에는 Green이 없습니다.')


if 'Green' not in colors:
    print('colors에는 Green이 없습니다.')

else:
    print('colors에는 Green이 있습니다.')

# quiz) 학점 경고 프로그램 만들기
# scores는 1학기 성적을 튜플로 나타낸 것 F 학점이 있으면 ‘경고’를 출력하는 프로그램
scores = ('A', 'A+', 'B', 'B-', 'F')

if 'F' in scores:
    print('경고')
else:
    print('경고 없음')

scores = ('A', 'A+', 'F', 'B', 'B-', 'F')
fCnt = scores.count('F')
print(f'F학점 개수:{fCnt}')

# 튜플 결합
# at list
nums1 = [1, 2, 3]
nums2 = [10, 20, 30]

# #1
nums1.extend(nums2)
print(f'nums1:{nums1}')

# #2
result = nums1 + nums2
print(f'nums1:{nums1}')
print(f'nums2:{nums2}')
print(f'result:{result}')

# at tuple 
nums1 = (1, 2, 3)
nums2 = (10, 20, 30)
result = nums1 + nums2
print(f'nums1:{nums1}')
print(f'nums2:{nums2}')
print(f'result:{result}')

num1 = 10
num2 = num1

print(f'num1:{num1}')
print(f'num2:{num2}')

num1 = 100
print(f'num1:{num1}')
print(f'num2:{num2}')


nums1 = [1, 2, 3]
nums2 = nums1
print(f'nums1:{nums1}')
print(f'nums2:{nums2}')

nums1[0] = 100
print(f'nums1:{nums1}')
print(f'nums2:{nums2}')

nums1 = [1, 2, 3]
nums2 = [0, 0, 0]

for idx, num in enumerate(nums1):
    nums2[idx] = num

print(f'nums1:{nums1}')
print(f'nums2:{nums2}')


nums1[0] = 100

print(f'nums1:{nums1}')
print(f'nums2:{nums2}')

print('deep copy------------------------------')

import copy

a = [1, 2, 3, 4, 5]
b = copy.deepcopy(a) # b = a.copy()

b[0] = 100

print(f'a:{a}')
print(f'b:{b}')

# 슬라이싱
animals = ('호랑이', '사자', '곰', '여우', '늑대')
print(f'animals:{animals}')

print(f'animals[:3]:{animals[:3]}')
print(f'animals[:3]:{animals[1:4]}')
print(f'animals[:3]:{animals[:-2]}')
print(f'animals[:3]:{animals[-1:-2]}')
print(f'animals[:3]:{animals[-3:-1]}')

# 슬라이싱 연습하기

# fruits 튜플에서 주어진 요구사항에 맞게 슬라이싱해봅시다.
#  - 인덱스 2부터 4까지의 아이템을 출력하시오.
#  - 인덱스 0부터 3까지의 아이템을 출력하시오.
#  - 인덱스 3부터 끝까지의 아이템을 출력하시오.

fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')

#  - 인덱스 2부터 4까지의 아이템을 출력하시오.
print(f'fruits[2:5]:{fruits[2:5]}')

#  - 인덱스 0부터 3까지의 아이템을 출력하시오.
print(f'fruits[:3]:{fruits[:4]}')

#  - 인덱스 3부터 끝까지의 아이템을 출력하시오.
print(f'fruits[3:]:{fruits[3:]}')

# 리스트와 튜플간 변환(형변화, casting)
# 불가피하게 튜플의 아이템을 수정하려면 리스트로 변환해야함
# 리스트로 선언된 데이 터를 수정이 안 되게 하려면 튜플로 변환해야 됨
# 데이터 변환을 통해 리스트와 튜플을 변환을 해야함
colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

colors = list(colors)    # 형변환
print(f'colors type:{type(colors)}')

colors[1] = '오렌지'      # 리스트 형변환 되어서 변환가능
print(f'colors:{colors}')

colors = tuple(colors) 
print(f'colors:{colors}')
print(f'colors type:{type(colors)}')

# quiz) 튜플 정렬하기
colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

colors = list(colors)
colors.sort()
print(f'colors:{colors}')

colors = tuple(colors) 
print(f'colors:{colors}')

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

cs = tuple(sorted(colors))
print(f'cs:{cs}')
