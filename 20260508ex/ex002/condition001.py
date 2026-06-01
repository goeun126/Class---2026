# 조건문(if문) / 특정 조건에 의해서 프로그램 분기
# if 조건식: < 콜론은 꼭 찍어야함 안그럼 error 확인
#    실행문
# 자바
# int num = 5;
# if (num > 10){
# System.out.printlh("num은 10보다 크다.");


num = 5
if num > 10:
    print('num은 10보다 크다.')

if num < 10:
    print('num은 10보다 크다.')

# if키워드: 조건문을 선언하기 위한 키워드로 '만약 ~ 라면'의 뜻을 가지고 있다.
# 조건식: 특정 조건을 기술한다. 조건식의 결과에 따라 실행문의 실행 여부가 결정된다.
# 콜론: 코드 블록의 시작을 나타내는 것으로 콜론 이후부터가 실행될 문장이다.
# 실행문: 조건식의 결과가 참(True) 경우 실행, 조건식이 거짓(False)이면 실행문은x

# 사용자가 입력한 정수가 10보다 크면 실헹문을 출력하는 프로그램

num = int(input('please input integer number'))

if num > 10:
    print(f'{num}은 10보다 크다.')

if num == 10:
    print(f'{num}은 10보다 같다.')

if num < 10:
    print(f'{num}은 10보다 작다.')

# quiz) 속도위반 경고
# 제한 속도가 50km/h인 도로에서 속도위반을 하는 자동차에 경고 하는 프로그램

speed = int(input('자동차의 현재 속도 입력: '))

if speed > 50:
    print(f'{speed}km/h 확인 속도위반입니다.')

if speed <= 50:
    print(f'{speed}km/h 확인 정상입니다.')

speed = 40
if speed <= 50:print(f'정산 운행~') #간단한 코딩이라면 공백문자 없어도 된다고 함.

# if ~ else 구문
# else: 그렇지 않으면~
myScoer = 70
if myScoer >= 90:
    print('용돈획득')
else:
    print('빠따')

# if ~ elif 구문 -> 다중선택
# 점수가 90점 이상이면 'A'출력
# 점수가 80점 이상 ~ 90점미만 이면 'B'출력
# 점수가 70점 이상 ~ 80점미만 이면 'C'출력
# 점수가 60점 이상 ~ 70점미만 이면 'D'출력

myScore = int(input('점수 입력: '))
if myScore >= 90:
    print('A')
elif myScore >= 80:
    print('B')
elif myScore >= 70:
    print('C')
elif myScore >= 60:
    print('D')
else:
    print('F')

# quiz) 자동 주문 시스템 만들기
# 1번 누르면 한국어, 2번 영어, 3번 중국어. 그외 번호는 영어로 주문받는 프로그램

KOREA_NUMBER = 1
USA_NUMBER = 2
CHINA_NUMBER = 3

number = int(input('1. 한국어 2.English 3. 中文  / English (Other)'))
if number == KOREA_NUMBER:
    print(f'주문 하시겠습니까?')
    
elif number == USA_NUMBER:
    print(f'Would you like to order?')

elif number == CHINA_NUMBER:
    print(f'您想下单吗？')

else:
    print(f'Would you like to order?')

# 국가 재난 지원금 수령액 조회하기
# 1인가구 : 400,000원
# 2인가구 : 600,000원
# 3인가구 : 800,000원
# 4인이상 가구 : 1,000,000원

p1 = 1
p2 = 2
p3 = 3

furniture = int(input('가구인원수를 입력하세요. '))

if furniture == p1:
    print(f'400,000원')
elif furniture == p2:
    print(f'600,000원')
elif furniture == p3:
    print(f'800,000원')
else:
    print(f'1,000,000')


# bmi 지수입력후
# 90이하면 저체중
# 90~ 110 이하면 정상
# 110~ 120 과체중
# 120 ~ 140비만
# 140 고도비만

bmiIndex = int(input('BMI지수를 입력하세요. '))

normal = 90
overweight = 110
obesity = 120
severeObesity = 140

if bmiIndex >= severeObesity:
    print('고도비만')
elif bmiIndex >= obesity:
    print('비만')
elif bmiIndex >= overweight:
    print('과체중')
elif bmiIndex >= normal:
    print('정상')
else:
    print('저체중')


# 중첩 조건문
# 조건문 내에 또 다른 조건문을 쓸 수 있는데 이를 중첩 조건문 이라고 합니다.
# 사용자가 입력한 정수에서 양수(0포함)인지를 판단하고 양수라면 홀/짝인지 구분

myInteger = int(input('정수 입력:'))
if myInteger >= 0:
    print('양수')
    if myInteger % 2 == 0:
        print('짝수')
    else:
        print('홀수')
else:
    print('음수')


# quiz) 짝/홀 판별하는 프로그램
num = int(input('사용자야 양의 정수 입력 해주라'))
if num > 0:
    if num % 2 == 0:
        print('짝수')
    else:
        print('홀수')
else:
    print('입력한 정수는 0또는 음수 입니다.')

    


# quiz) 출생년도 끝자리 와 나이를 입력하면 다음 요구사항에 맞춰 마스크 구매 가능한 요일을 출력하는 프로그램
# - 출생년도 끝자리를 이용한 5부제 
# 1,6 => 월
# 2,7 => 화
# 3,8 => 수
# 4,9 => 목
# 5,0 => 금
# 만 65세 이상 어르신은 언제든지 구매 가능

endBirthYear = int(input('출생연도 끝자리 입력: '))
age = int(input('나이 입력: '))

if age < 65:
    if endBirthYear == 1 or endBirthYear == 6:
        print('월요일 구매 가능합니다.')
    if endBirthYear == 2 or endBirthYear == 7:
        print('화요일 구매 가능합니다.')
    if endBirthYear == 3 or endBirthYear == 8:
        print('수요일 구매 가능합니다.')
    if endBirthYear == 4 or endBirthYear == 9:
        print('목요일 구매 가능합니다.')
    if endBirthYear == 5 or endBirthYear == 0:
        print('금요일 구매 가능합니다.')
else:
    print('언제나 구매 가능합니다.')

# 날짜 관련 모듈: datetime
from datetime import datetime

# 현재 일 구하기
print(datetime.today().weekday())
print(datetime.today().day())

# quiz) 차량 2부제 시스템
from datetime import datetime
carNumber = int(input('차량 번호를 4자리 입력하세요.'))
day = int(datetime.today().day)

print(f'오늘 날짜 :{day}일')

if day % 2 == 0:
    print('오늘 입차: 번호가 짝수인 차량')
else:
    print('오늘 입차: 번호가 홀수인 차량')

if day % 2 == carNumber % 2:
    print('귀하의 차량은 입차 가능합니다.')
else:
    print('귀하의 차량은 입차 불가합니다.')

# 심장정지 환자에게 충격기 사용했을때 생존율 나타낸다

basic = int(input('최초 장비를 사용하기까지 걸린 시간(초)을 입력하세요. '))

limit_60 = 60
limit_120 = 120
limit_180 = 180
limit_240 = 240
limit_300 = 300

print(f'최초 장비를 사용하기까지 걸린 시간(초)을 입력하세요.{basic}초')
if basic <= limit_60:
    print('생존율:85%')
elif basic <= limit_120:
     print('생존율:76%')
elif basic <= limit_180:
     print('생존율:66%')
elif basic <= limit_240:
     print('생존율:57%')
elif basic <= limit_300:
     print('생존율:47%')
else:
     print('생존율:25% 미만')

# 누진세가 적용된 단가표 참고 하여 사용량을 입력하면 전기료가 출력되는 프로그램
unitPrice1 = 99.3
unitPrice2 = 187.9
unitPrice3 = 280.6

baseFee1= 910
baseFee2= 1600
baseFee3= 7300

kwh= int(input('전기 사용량을 입력하세요. '))

if kwh <= 200:
    print(f'사용량:{kwh:.1f}kwh')
    print(f'{baseFee1}원')
    print(f'{unitPrice1:.1f}원')
    print(f'{baseFee1 + unitPrice1 * kwh:.1f}원')

elif kwh >= 200:
    print(f'사용량:{kwh:.1f}kwh')
    print(f'{baseFee2}원')
    print(f'{unitPrice2:.1f}원')
    print(f'{baseFee2 + unitPrice2 * kwh:.1f}원')

elif kwh >= 400:
    print(f'사용량:{kwh:.1f}kwh')
    print(f'{baseFee3}원')
    print(f'{unitPrice3:.1f}원')
    print(f'{baseFee3 + baseFee2 * kwh:.1f}원')


# 어린이 신장 입력하면 탑승 여부가 출력되는 프로그램
# 120cm~ 최대 160

height = int(input('신장을 입력하세요.'))
if height >= 120 and height <= 160:
    print('탑승 가능')
else:
    print('탑승 불가능')

# 시험점수 입력
testScore = int(input('시험 점수 입력:'))
if testScore >= 85:
    print('success')
else:
    print('fall')

# 가위 바위 보 컴터랑 게임
import random       #난수발생 모듈

ranNum = random.randint(1, 3)   # 1 ~ 3까지의 정수중에서 하나는 발생한다.

myNum = int(input('1.가위 2.바위 3.보 를 선택하세요.'))

if ranNum == myNum:
    print('무승부')
elif (ranNum == 1 and myNum == 2) or \
    (ranNum == 2 and myNum == 3) or \
        (ranNum == 3 and myNum == 1):
     print('사용자 승')
elif (ranNum == 1 and myNum == 3) or \
    (ranNum == 2 and myNum == 1) or \
        (ranNum == 3 and myNum == 2):
    print('컴퓨터 승')

# 입력한 문자 메세지 길이에 따라서 sms, mms 발송을 결정하는 프로그램
# 50이하면 sms / 이상이면 mms 발송

str = 'hello'
print(f'str: {str}')
print(f'str length: {len(str)}')

useMessage = input('메세지를 입력하세요.')
msgLen = len(useMessage)

if msgLen <= 50:
    print('sms 발송')
else:
    print('mms 발송')