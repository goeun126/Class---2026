# 산술 연산자
# 산술 연산자는 우리가 자주 사용하는 사칙 연산자와
# 컴퓨터 프로그램에서만 사용하는 나머지, 몫, 지수 연산자를 뜻합니다.
# +, -, *, /
# %(나머지), //(몫), **(지수)

#덧셈 연산자(+)
print(10 + 20)
print(3.14 + 5)
num1 = 10; num2 = 100
print(num1 + num2)

#puiz) 전자 회사에서 1분기 매출의 총합을 구하고자 합니다. 프로그램 작성 해봅시다.
sales1 = int(input('1월 매출 입력하세요.'))
sales2 = int(input('2월 매출 입력하세요.'))
sales3 = int(input('3월 매출 입력하세요.'))
total = sales1 + sales2 + sales3
print(f'1분기 매출: {total:,}원')

#문자열 덧셈
print('a'+ 'b')             #덧셈(연결)연산자

#문자열 숫자 >Type error
print('hello' + 3)

#뺄셈 연산자(-)
print(10 - 5)
print(3.14 - 0.1)

print('hello' - 10)      #문자열 숫자 >Type error

#quiz)전자에서 1분기 수익을 계산하려고 합니다.
# 사용자가 1분기 매출액과 매입액을 입력하면
# 수익을 계산해주는 프로그램

sales = int(input('1분기 매출: '))
purchase = int(input('1분기 매입: '))
profit = sales - purchase
print(f'수익: {profit:,}원')

#곱셉 연산자(*)
print(10 * 20)
print(3.14 * 3)

#문자열 곱셈
str = "hello"
print(str * 3)

#quiz) 가로, 세로 길이를 입력하면 
# 방의 넓이를 계산해주는 프로그램을 만들어봅시다
width = int(input('가로 입력: '))
length = int(input('세로 입력: '))
area = width * length
print(f'방의 넓이: {area}')

#quiz) Goodmoening  문자열을 사용자가 입력한 숫자만큼 출력하는 프로그램 입니다.
intro = 'Good moening'
cnt = int(input('출력을 원하는 횟수를 입력하세요.'))
print(intro * cnt)

name = input('이름을 입력하세요.: ')
print(f'안녕하세요,{name}님!')

num1 = int(input('첫 번째 숫자: '))
num2 = int(input('두 번째 숫자: '))
print(f'합계: {num1 + num2}')

hamburger = int(input('햄버거 가격: '))
drink = int(input('음료 가격: '))
print(f'총 가격: {hamburger + drink} 원')

name = input('이름: ')
print(f'{name * 3}')

year = int(input('태어난 연도: '))
age = 2026 - year
print(f'당신의 나이는 {age}살 입니다.')

minute = int(input('분 입력: '))
age = 60 * minute
print(f'{age}초입니다. ')

korean = int(input('국어: '))
english = int(input('영어: '))
print(f'평균:{(korean + english)/ 2} ')

name = input('이름: ')
print(f'안녕하세요, {name}님! ')

food = input('좋아하는 음식: ')
print(f'{food}를 좋아하는군요!')

hi = input('입력: ')
print((hi + ' ') * 2)

shool = input('학교: ')
print(f'당신의 학교는 {shool}입니다. ')

name = input('이름: ')
hobby = input('취미: ')
print(f'{name}의 취미는 {hobby}입니다. ')

user = input('캐릭터 이름: ')
print(f'{user}이 생성되었습니다.! ')

order = input('주문: ')
print(f'{order} 주문 완료 ')

mood = input('기분: ')
print(f'{mood}한 하루 보내세요!')

hi = input('입력: ')
print((hi + ' ') * 3)

ver1 = input('입력: ')
print(f'{ver1}')

