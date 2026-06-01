print('회원정보를 입력하세요.')

userName = input('이름: ')
userMail = input('메일: ')
userId = input('아이디: ')
userPw = input('비밀번호: ')

print('------------------------------')
print('To. '+ userMail)
print('▶아이디 및 비밀번호 확인')
print(userName +' 고객님 안녕하세요.')
print(userName +' 고객님의 아이디와 비밀번호는 아래와 같습니다.')
print('아이디: ' + userId)
print('비밀번호: ' + userPw)
print('감사합니다.')
print('Naver 담당자.')
print('------------------------------')

userMail = 'gidong@gmail.com'
print('To. gidong@gmail.com')
print('To. '+ userMail)
print('To.', userMail)

print("이름", "홍길동", "나이:", 20)

print("2026", "05", "06", sep="-")

print("Hello", end=" ")
print("world")

# f-string (가장 많이 사용)
name = "철수"
age = 25

# 이름은 철수. 나이는25입니다.
print('이름은 '+ name +', 나이는 ' + str(age) + '입니다.')
print(f'이름은 {name}, 나이는 {age}입니다.') # EL 표기법

# format(두 번째로 많이 사용)
print("이름은 {}, 나이는 {}입니다.".format(name, age))
# format(index 순서 정할수있음)
print("이름은 {1}, 나이는 {0}입니다.".format(age, name))

hello = 'Good Morning'
print( hello * 3)

koreanScore = input('국어 점수')
engScore = input('영어 점수')
mathScore = input('수학 점수')

print(f'국어 점수:, {koreanScore}')
print(f'수학점수:, {mathScore}')
print(f'영어점수:, {engScore}')

firstNum = int(input('정수를 입력하시오'))
secondNum = int(input('정수를 입력하시오'))

print(f'합: {firstNum + secondNum}')
print(f'평균: {(firstNum + secondNum) / 2}')

var1 = 10
var2 = 20

print(f'var1: {var1}, var2: {var2}')

temp = var1
var1 = var2
var2 = temp

print(f'var1: {var1}, var2: {var2}')

userName = input('이름을 입력하세요: ')
print(f"안녕하세요. {userName}님!")

color = input('좋아하는 색깔: ')
print(color + "색을 좋아하시는군요!") 

zoo = input('좋아하는 동물: ')
print(f'{zoo}를 좋아하시는군요!')

ver1 = int(input('첫 번째 숫자: '))
ver2 = int(input('두 번째 숫자: '))
print(f'결과: {ver1 + ver2}')

num = 1
num += 10
print(num)

