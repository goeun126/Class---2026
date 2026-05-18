# 함수(function)
# python 함수 제일 중요함 
# 함수를 만든 사람만 수정가능 다른사람은 x

# 함수 정의하기
# 사용자 함수를 만든다는 것은 '함수를 정의 함,라고 함
# 함수를 정의 할때 def 키워드 이용,함수명 콜론(:), 실행부를 이용함

# def 함수명():
#     실행문(함수 가능)
def gye():
    print('안녕하세요')
    print('반갑습니다.')
    print('저는 홍실동입니다.')

# 함수명 규칙
# 1. 내장 함수명과 동일하게x
# 2. 첫 글자는 주로 소문자로 시작함.
# 3. 첫 글자는 숫자로 시작 x
# 4. 특수 문자는 사용이 불가능하나_는 사용가능
# 5. 두개이상의 단어가 조합되는 경우, 스네이크 또느 카멜 표기법을 사용.

# quiz) 온도센서 작동 시스템 만들기
# 온도센서를 작동을 시작하고 멈추는 함수 정의
# 함수명으느 함수의 기능을 이해하기 쉽게 짓는게 좋음

def startTemperatureSensor():
    print('온도센서 작동을 시작합니다.')
def stoptTemperatureSensor():
    print('온도센서 작동을 중지합니다.')

# 함수 호출
startTemperatureSensor()
stoptTemperatureSensor()

# quiz) 노트북 인치 확인하기
# 노트북으로 하나 장만햇음
# 노트북 사이즈에 꼭 맞는 파우치를 하나 구매하려하고 함, 
# cm 인치로 바꿔주는 함수로 만들기
# 1icf = 0.39301cv

def convertUnit():
    lengthcm = float(input('길이(cm) 입력:'))
    print(f'{lengthcm * 0.393701}inch')

convertUnit()

# quiz) 이동거리를 계산하는 함수
# 5시간 동안 3km의 속도로 등산
# 등산한 시간과 속도를 입력하면 이동한 거리를 계산해주는 프로그램

def calculateDistance():
    print(f'이동거리:{hourData * speedData} km')

hourData = float(input('이동 시간:'))
speedData = float(input('이동 속도:'))

calculateDistance()

# pass 키워드
def calculaeNumber():
    pass

# 함수내에서 또다른 함수 호출
def fun1():
    print('fun1() CALLDED')

def fun2():
    print('fun2() CALLDED')

def fun3():
    fun1()
    fun2()
    print('fun3() CALLDED')

fun3()

def fun4():
    print('fun4() CALLDED')
    fun4()   # 본인이 본인을 호출한다 (재기 함수)

fun4()

# quiz) 다국어 인사말 프로그램
# 출신 국가를 선택하면 해당 하는 국가의 인사말이 출력되는 프로그램
# 1. 한국    2. USA    3. Japan

def introKor():
    print('안녕하세요.')

def introEng():
    print('Hello')

def introHap():
    print('こんにちは')

selectedMenuNum = int(input('Where are you from? 1. 한국    2. USA    3. Japan'))

if selectedMenuNum == 1:
    introKor()

elif selectedMenuNum == 2:
    introEng()

elif selectedMenuNum == 3:
    introHap()

# quiz) 계산기 프로그램
# 사용자가 숫자 2개 입력하고 연산자를 선택하여 연산결과가 출력되는 프로그램

def add():
    print(f'뎃셈 결과:{inputNumber1 + inputNumber2}')

def sub():
    print(f'뺄셈 결과:{inputNumber1 - inputNumber2}')

def mul():
    print(f'곱셈 결과:{inputNumber1 * inputNumber2}')

def div():
    print(f'나눗셈 결과:{inputNumber1 / inputNumber2}')


def calculator():
    if selectedOperator == 1:
        add()

    elif selectedOperator == 2:
        sub()

    elif selectedOperator == 3:
        mul()

    elif selectedOperator == 4:
        div()


inputNumber1 = float(input('숫자를 입력하세요.'))
selectedOperator = int(input('연산자를 선택하세요. 1. 덧셈   2.뺄셈   3.곱셈    4.나눗셈'))
inputNumber2 = float(input('숫자를 입력하세요.'))

calculator()