# CRUD
# C:Create (생성, 추가) 
# R: Read (조회) 
# U:Upate (수정)
# D:delete (삭제)
'''
#딕셔너리(Dictionary): {key: value}
# C:Create
student = {
    '학번': 123456789,
    '이름': '홍길동',
    '나이': '20',
    '성별': 'M',
    '연락처': '010-1234-5678'
}
print(f'student: {student}')
print(f'student type: {type(student)}')

# R: Read (조회) 
sNo =  student['학번']
print(f'sNo:{sNo}')
print(f'sNo type: {type(sNo)}')

# U:Upate (수정)
sName = student['이름']
print(f'sName:{sName}')

student['이름'] = '홍길자'
sName = student['이름']
print(f'sName:{sName}')

# D:delete (삭제)
del student['연락처']
print(f'student: {student}')

# keys(), values(), itme()
# keys(): 딕셔너리 자료형에서 키값들만 전체 확인, 뽑은 키들은 리스트와 비슷한 데이터 타입.
kets = student.keys()
print(f'kets:{kets}')
print(f'kets type: {type(kets)}')

for key in kets:
    print(f'key:value = {key}:{student[key]}')

# values(): 딕셔너리에서 벨류값들만 전체 확인, 뽑은 벨류들은 리스트와 비슷한 데이터 타입.
values = student.values()
print(f'values:{values}')
print(f'values type: {type(values)}')

for value in values:
    print(f'value:{value}')

items = student.items()
print(f'itme:{items}')

for item in items:
    print(f'item:{item}')
    print(f'item[0], item[1]:{item[0]}, {item[1]}')

for key, value in items:     # 구조분해할당 문법
    print(f'key:value = {key} : {value}')

# 구조분해할당 문법
a, b = (10, 20)
print(f'a:{a}, b:{b}')

a = 10
b = 20

# seapping ==> a:20, b:10

temp = a
a = b
b = temp

a, b = b, a

# a = 10 b = 20 c = [30, 40, 50, 60]
scores = [10, 20, 30, 40, 50, 60]

a, b, *c = scores
print(f'a:{a}')
print(f'b:{b}')
print(f'c:{c}')
'''
# quiz) 스포츠 센터 회원정보 표이다 표를 보고 컨테이너 자료형 만들기

members = {
    '2019-05201':{
        '이름':'박찬호',
        '나이': 25,
        '성별': 'M',
        '연락처': '010-1234-5678',
        '이용서비스': '헬스,수영',
        '할인율': '0'
    }
}

# info = members['2019-05201']
# print(f'info:{info}')
# infos = info.split('+')
# print(f'infos:{infos}')

print(members['2019-05201']['이름'])
print(members['2019-05201']['나이'])
print(members['2019-05201']['성별'])
print(members['2019-05201']['연락처'])
print(members['2019-05201']['이용서비스'])
print(members['2019-05201']['할인율'])