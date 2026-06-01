# 지역변수 VS 전역변수
# 지역변수는 함수 내부에서 선언된 변수로 함수 내부에서만 사용 가능함.
# 전역변수는 함수 외부에서 선언된 변수로 함수 내/외부에서만 사용 가능함.
num = 10

def fun():
    # num = 20
    global num  # global 키워드는 함수 내에서 전역변수의 값을 '수정'하고자 할때 명시 필요
    num += 1
    print(f'num:{num}')

print(f'num:{num}')

fun()

# quiz) 웹사이트의 누적 방문 횟수 프로그램
# 웹사이트 방문 여부를 입력받아 누적 방문 횟수 출력

flag = True
totalVisitor = 0

def countVisitor():
    global totalVisitor
    totalVisitor += 1

while flag:
    selectedMeniNum = int(input('1. 웹사이트 방문     2. 종료'))

    if selectedMeniNum == 1:
        countVisitor()
        print(f'누적 방문횟수:{totalVisitor}')

    else:
        flag = False
        print('Good bye')

# 매개 변수
# 매개: 둘 사이에서 양편의 '관계를 맺어' 줌

# 함수를 사용하기 위해 먼저 함수를 정의하고 필요할 때 호출하는데,
# 이때, 함수를 정의하는 쪽을 함수 정의부(선언부), 함수를 호출하는 쪽을 호출부 라고 함

# 함수를 호출할 때 데이터를 넘겨줄 수 있는데 이 데이터를 '인수' 라고 함
# 함수 정의부는 인수를 받으면 '매개변수'라는 변수에 저장 함, 
# 매개변수는 지역 변수의 일종임



def greet (name, age):
    print(f'{name}님 안녕하세요! 나이:{age}세')

name = input('이름 입력: ')
age = int(input('나이 입력: '))

greet(name, age)

def forecastWeather(tenp, humi, rain):
    print('날씨 예보입니다.')
    print(f'최고 온도: {tenp}도')
    print(f'평균 습도: {humi}%')
    print(f'비올 확율: {rain}%')

tenp = int(input('온도 입력:'))
humi = int(input('습도 입력:'))
rain = int(input('강수량 입력:'))

forecastWeather(tenp, humi, rain)

# 인수의 개수를 모르는 경우
# 우리 학급학생 들의 시험점수를 총합과 평균을 구하는 함수
# 학급 학생수 총 3명

def printScoersForStudent(*scores):
    
    totalScore = 0
    for score in scores:
        totalScore += score
        
    print(f'총합:{totalScore}')
    acerageScoer = totalScore / len(scores)
    print(f'총합: {acerageScoer:.2f}')

printScoersForStudent(90, 80, 70, 20, 50, 30, 60)

# 선생님이 몇명일지 모르는 학생의 점수를 입력함.
# 이때 학생 점수의 총합과 평균을 구하는 함수를 만들고 이를 이용하는 프로그램.

flag = True
studentScores = []

def printScoersForStudent(scores):
    if len(scores) == 0:
        print('학생수가 0명이라 평균과 총점을 구할 수 었습니다.')
    else:
        totalScore = 0
    for score in scores:
        totalScore += score

    acerageScoer = totalScore / len(scores)
    print(f'총점:{totalScore}')
    print(f'평균:{acerageScoer:.2f}')

while flag:
    seletedMenuNum = int(input('1. 학생 점수 입력    2. 종료'))
    if seletedMenuNum == 1:
        scoer = int(input('학생 점수 입력:'))
        studentScores.append(scoer)
    else:
        flag = False

printScoersForStudent(studentScores)

# quiz) SMS와 MMS 구별하
# 문자를 보낼 때 100자 이하인 경우에는 단문 메시지(SMS)로 50원을 부과함 
# 그런데 100자를 넘어가면 장문 메시지(MMS)로 변경되면서 100원이 부과됨 
# 단문과 장문을 구별해서 돈을 부과하는 프로그램. 

inputData = input('문자 입력:')

def sendUserMessage(str):
    strLength = len(str)
    print(f'사용자가 입력한 문자 길이:{strLength}')

    if strLength <= 100:
        print(f'SMS 발송 완료')
        print('50원 부과')
    else:
        print(f'MMS 발송 완료')
        print('100원 부과')

sendUserMessage(inputData)

# 인수와 매개변수의 순서가 일치하지 않을 경우
def printMemberInfo(name, email, major, grade):
    print(f'name\t:{name}')
    print(f'email\t:{email}')
    print(f'major\t:{major}') 
    print(f'grade\t:{grade}') 
    print('-----------------------------------')

printMemberInfo('Hong Gildong', 'gildong@gmail.com', 'art', '1')
printMemberInfo(email = 'gildong@gmail.com', 
                name= 'Hong Gildong', 
                major = 'art', 
                grade= '1')

def printMemberInfo(info):
    print(f'name:{info['name']}')
    print(f'email:{info['email']}')
    print(f'major:{info['major']}')
    print(f'grade:{info['grade']}')

printMemberInfo(
    {
        'name':'Hong Gildong',
        'email':'gildong@gmail.com',
        'major':'art',
        'grade':1

    }
)

# 매개변수의 기본값 설정
# 직원 급여 지급 프로그램
def setSalary(name,pay = 200):
    print(f'{name}의 급여는 {pay:,}원')

name = input('이름 입력:')
pay = int(input('급여 입력:'))

setSalary(name, pay)

# 데이터 반환(return)
# 데이터 반환이라느 함수는 실행이 끝난 후에 결과물(값)을 호출부로 반환 할수 있음
# 이때 사용하는 키워드 return
# 덧셈 연산 함수를 만들어 결과를 출력하는 프로그램

def printResult(vlue):
    print(f'reyurn:{vlue}')


def addFuntion(n1, n2):
    sum = n1 + n2
    # print(f'결과 값:{sum}')
    printResult(sum)
    return sum

addFuntion(10, 20)

DEV_MOD = True

def fun1():
    print('222222222')   
    if DEV_MOD == True:
        print('111111111')
        return                # 개발 단계에서 디버깅용도로만 사용함.
    print('333333333')

fun1()

# 별탑 만들기

def increaseStart(limotStarCount):
    # print('*')
    # print('**')
    # print('***')
    # print('****')
    # print('*****')
    # print('******')
    # print('*******')
    for n in range(1, 8):
        print('*' * n)
        if n == limotStarCount:
            break

increaseStart(5)

# 처음 프로그램이 실행되면 다음과 같은 메뉴를 출력
# 메뉴: 1. 회원가입   2.로그인    3.특정회원 정보 출력  4. 모든회원 정보 출력    99.종료
# 사용자가 '1.회원가입'을 선택하면 회원ID, 회원PW, 회원Eail, 회원Phone 입력 받아 회원가입 진행
# 2.로그인을 선택하면 회원ID, 회원PW를 입력받아 로그인 성공 또는 실패를 출력
# 3.특정회원 정보 출력 을 선택시 회원ID, 회원PW 입력받아 일치하는 회원 정보를 모두 출력
# 4. 모든회원 정보 출력를 선택하면 가입되어있는 모든 회원 목록을 출력
# 99. 종료를 선택하면 프로그램 종료
# 심심하면 특정회원의 회원ID, 회원PW 입력받아 인증되면 회원 정보를 수정하는 기능

members = []


def menuSelection():
    print('\n--- 원하는 메뉴를 선택하세요! ---')
    print('1. 회원가입')
    print('2. 로그인')
    print('3. 특정 회원 정보출력')
    print('4. 모든 회원 정보출력')
    print('99. 종료')
    print('--------------------------------')



def inputMemberInfo():
    
    memberId = input('ID 입력:')
    memberPw = input('PW 입력:')
    memberEmail = input('Email 입력:')
    memberPhone = input('Phone 입력:')
    
    newMember = {
            'id':memberId,
            'pw':memberPw,
            'email':memberEmail,
            'phone':memberPhone
        }
    return newMember

def loginInput():
    memberId = input('ID 입력:')
    memberPw = input('PW 입력:')
    return memberId, memberPw

flag = True

while flag:
    menuSelection()
    selectedMenu = int(input('원하는 번호를 입력하세요.'))

    if selectedMenu == 1:
        members.append(inputMemberInfo())
        print('회원가입성공!')
        print('초기 화면으로 돌아갑니다. 번호 다시 선택해주세요!')

    elif selectedMenu == 2:
        loginData = loginInput()
        
        login_success = False
        for member in members:
            if loginData[0] == member['id'] and loginData[1] == member['pw']:
                print('로그인 성공!')
                login_success = True
                break

            if not login_success:
                print('로그인 실패: ID 또는 PW를 확인하세요.')
                

    elif selectedMenu == 3:
        loginData = loginInput()
        if loginData[0] == member['id'] and loginData[1] == member['pw']:
            print(f'인증성공 {members['id']}님의 정보입니다.')

    elif selectedMenu == 4:
        pass

    elif selectedMenu == 99:
        flag = False
        print('시스템이 종료 되었습니다.')
    
    else:
        print('번호를 잘못 입력하셨습니다. 다시 선택해주세요.')
    