# 딕셔너리(dictionary)
# 리스트가 인덱스를 이용하여 아이템을 참조 한다면
# 딕셔너리는 키를 이용해서 아이템을 참조함

# 딕셔너리 정의
# 딕셔너리 {} 

# 키(key)값 중복x :value값 중복가능
ages = {'박찬호':48, '박지성':40, '박세리':50, '이승엽':43}
print(f'ages:{ages}')
print(f'ages type:{type(ages)}')

# quiz) 성적을 집합을 딕셔너리 이용해서 선언
scores = {'C/C++':'A', 'java':'B+', '네트워킹':'C', '보안':'A+', '해킹':'F', '시스템':'C+'}
print(f'scores:{scores}')
print(f'scores type:{type(scores)}')

# 마지막 내용
# 리스트, 튜플, 딕셔너리

listVar = [3, 3.14, 'hello']
print(f'listVar:{listVar}')

tupleVar = [3, 3.14, 'hello']
print(f'tupleVar:{tupleVar}')

dictVar = {'홍길동':10, '박찬호':'열살', '박세리':3.14}
print(f'dictVar:{dictVar}')

listVar1 = [1, 2, 3]
listVar2 = [1, 2, 3, listVar1]

print(f'listVar1:{listVar1}')
print(f'listVar2:{listVar2}')

print(listVar2[3][1])
print(type(listVar2[3]))

dicts = {
    'name':'박찬호',
    'age': 20,
    'addr':'대전 중구',
    'hoddy':['축구', '농구','배구']
}

print(f'dicts:{dicts}')
print(dicts['hoddy'][1])
