# 반복문(for문 & while문)

# for 문: ~ 하는 동안 ==> 횟수에 의한 반복
            # iterable(반복 가능한 객체)
# for 변수 in 범위(시작, 끝값(+1), 범위):
    # 실행구문

# 1~10까지의 정수를 출력
for num in range(1, 101, 1):
    print(f'{num} : hello')
    print(f'hello')

for num in range(2, 11, 2):
    print(f'{num}')

for num in range(0, 11, 1):
    print(f'{num}')

# range() 간략화 -> 단계가 1일경우 생략가능
for num in range(0, 11):
    print(f'{num}')

# range() 간략화 -> 단계가 생략되고 시작이 0이면 시작도 생략이 가능
for num in range(11):
    print(f'{num}')

# quiz) 2~8사이의 짝수 출력하기
for num in range(2, 9, 2):
    print(f'num: {num}')

for num in range(2, 16):
    if (num <= 8) and (num % 2 == 0):
        print(f'{num}')

# quiz) 사용자가 입력한 횟수만큼'메일발송!'
mail = int(input('횟수: '))

for mail in range(mail):
    print(f'메일 발송')

# 1~10 사이의 정수로 출력하되, 정수가 3의 배수이면 '3의 배수!' 출력하기
for num in range(1, 11):
    if num % 3 == 0:
        print('3의 배수!')
    else:
        print(num)

for i in range(1, 11):
    print('3의 배수!' if (i % 3 == 0) else i)

# quiz) 사용자가 원하는 구구단을 입력 하면 구구단
timesTables= int(input('구구단을 입력하세요. '))
for num in range(1,10):
    print(f'{timesTables} X {num} = {timesTables * num} ')


# quiz) 1~10까지 정수의 합
num2 = 0
for num in range (1, 50):
   num2 = num2 + num
print(f'{num2}')

# quiz) for문을 이용해서 1~100까지 정수중에서 3과 7공배수와 최소 공배수

first = True
for i in range(1, 101):
    if i % 3 == 0 and i % 7 == 0 and first == True:
        print(f'{i}는 3과 7의 최소공배수입니다.')
        first = False
    elif i % 3 == 0 and i % 7 == 0 :
        print(f'{i}는 3과 7의 공배수입니다.')


# 문자열을 이용한 for 문
# 이터러블 range() 함수에 이용한 예를 확인했음.
# 하지만 다음과 같이 문자열도 이용가능

for ch in 'hello':
    print(f'ch:{ch}')

# 50보다 작은 7의 배수를 출력하는 프로그램
for num in range(1,51):
    if num % 7 == 0:
        print(f'num:{num}')

# while 문: ~ 하는 동안 ==> 조건에 의한 반복

# quiz) 1 ~ 30까지의 정수중 홀수와 짝수를 구분하여 출력하기

num = 1               #시작
while num < 31:       #조건(끝)
    
    if num % 2 == 0:
        print(f'{num}은 짝수')
    else:
        print(f'{num}은 홀수')

    num += 1          #단계

# quiz) 구구단 3단 출력하기 by while문 이용하요 구구단

timesTables = int(input('구구단 숫자를 입력하세요.'))
num = 1
while num < 10:
    print(f'{timesTables} x {num} = {timesTables * num}')
    num += 1

# quiz) 구구단 전체 (2단 3단 4단 ....9단)

num1 = 1

while num1 <= 10:
  timesTables = 2
  str = ''
  while timesTables <= 10:
    str += f'{num1} x {timesTables} = {num1 * timesTables}\t'
    timesTables += 2
  print(str)
  num1 += 1


# quiz) while문과 if 문을 이용해서 0~ 100까지 정수중 3과 8의 공배수와 최소공배수

minimum = 0
num = 1
while num <= 100:
    if (num % 3 == 0) and (num % 8 == 0):
        print(f'3과 8의 공배수:{num}')
        if minimum == 0:
            minimum = num
    num += 1
print(f'최소공배수: {minimum}')


# 반복문 내 실행 제어(continue, break)
# continue: 반복문의 continue 키워드 사용하면 이후 '실행을 생략하고 반복문의 처음으로' 돌아감

# continue 이용해서 1부터 10까지 정수중 홀수만 출력하는 프로그램
for num in range(1,11):
    if num % 2 == 1:
        continue
    print(f'num:{num}')

# break:
# 반복문에서 break 키워드를 만나면 '실행을 중단 반복문 빠져' 나옴

# 1부터 10까지 정수를 더하되 결과가 30이상 될 때 정수를 찾는 프로그램
num = 1
sum = 0

while num < 11:
    sum += num
    if sum >= 30:
        print(f'num:{num}')
        break
    num += 1

count = 1
for num in range(10):
    print(f'num:{num}')
    count += 1
    if count >= 5:
        break

# for ~ else 키워드
# for문에 else 키워드를 사용하는 경우 , else이하의 구문은 for문의 반복 업무를 모두 완료 하고 난뒤 실행

# 1부터 5까지 정수를 출력하고 반복문의 끝나면 메세지 전달
for num in range(1, 6):
    print(f'num:{num}')
else:
    print('완료')

# pass 키워드
for num in range(1, 10):
    pass

# quiz) 삼각형의 넚이 구하기 가로 길이 1부터 2의 배수로 증가하고 
# 삼각형의 넚이가 150보다 크면 프로그램 종료

count = 1
maxArea = 150

while True:
    result = ((count * 2) * (count * 3)) / 2
    if result > 150:break
    print(f'삼각형의 넚이는: {result}')
    count += 1

