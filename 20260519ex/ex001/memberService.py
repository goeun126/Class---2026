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
        member = inputMemberInfo()
        members.append(member)
        print('회원가입성공!')
        print('초기 화면으로 돌아갑니다. 번호를 다시 선택해주세요!')

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
        found = False

        for member in members:
            if loginData[0] == member['id'] and loginData[1] == member['pw']:
                print(f"----{member['id']}님의 정보")
                print(f"이메일: {member['email']}")
                print(f"전화번호: {member['phone']}")
                found = True
                break
        if not found:
            print('회원정보가 없습니다. ID 와 PW 다시 확인해주세요.')

    elif selectedMenu == 4:

        if len(members) == 0:
            print('등록된 회원이 없습니다.')

        else:
            print('------- 모든 회원 정보 -------')

            for member in members:
                 print(f"ID : {member['id']}")
                 print(f"EMAIL : {member['email']}")
                 print(f"PHONE : {member['phone']}")
                 print('-------------------')
    
            break


    elif selectedMenu == 99:
        flag = False
        print('시스템이 종료 되었습니다.')
    
    else:
        print('번호를 잘못 입력하셨습니다. 다시 선택해주세요.')


# 교수님이 하신거
SIGN_UP                 = 1
SIGN_IN                 = 2
PRINT_MY_INFO           = 3
PRINT_ALL_MEMBER_INFO   = 4
SYSTEM_SHUTDOWN         = 99

DEV_MOD = True

members = {}            # Database

if DEV_MOD:

    uIds = ['gildong', 'chanho', 'saeri']
    uPws = ['1234', '5678', '9012']
    uMails = ['gildong@gmail.com', 'chanho@naver.com', 'saeri@daum.net']
    uPhones = ['010-1234-5678', '010-9999-8888', '010-7777-6666']

    for n in range(len(uIds)):      # 3회 반복 ( 0, 1, 2 )
        members[uIds[n]] = {
            'uId': uIds[n],
            'uPw': uPws[n],
            'uMail': uMails[n],
            'uPhone': uPhones[n]
        }

flag = True
while flag:
# functions START

 def getSelectedMenuNum():
    selectedMenuNum = int(input('1.회원가입    2.로그인    3.나의 정보 출력     4.모든 회원 정보 출력    99.종료'))
    return selectedMenuNum

def setNewMember(uId, uPw, uMail, uPhone):
    members[uId] = {
                'uId': uId,
                'uPw': uPw,
                'uMail': uMail,
                'uPhone': uPhone
            }
def isMember(uId):
    if uId in members:
            print(f'{uId}는(은) 이미 사용중 입니다. 다시 확인하세요.')
            return True
    else:
        return False

def printAllMemberInfo(value):
    for key1, value1 in value.items():
                print(f'{key1}: {value1}')
# functions END

    if userSelectedMunuNum == SIGN_UP:              # 1.회원가입
        uId = input('Input member ID: ')
        uPw = input('Input member PW: ')
        uMail = input('Input member EMAIL: ')
        uPhone = input('Input member PHONE: ')

        members[uId] = {
            'uId': uId,
            'uPw': uPw,
            'uMail': uMail,
            'uPhone': uPhone
        }

        print('SIGN-UP SUCCESS!!')

        if DEV_MOD: print(f'members: {members}')
flag = True
while flag:
    
    userSelectedMunuNum = getSelectedMenuNum()

    # elif selectedMenuNum == SIGN_IN:            # 2.로그인 
    if userSelectedMunuNum == SIGN_UP:              # 1.회원가입
        uId = input('Input member ID: ')
        uPw = input('Input member PW: ')

        if uId in members:
            uInfo = members[uId]
            if uInfo['uPw'] == uPw:
                print('SIGN-IN SUCCESS!!')
        if not isMember(uId):        # False: 회원이 없는경우(회원가입 진행O)   True: 회원이 있는경우(회원가입 진행X)
            uPw = input('Input member PW: ')
            uMail = input('Input member EMAIL: ')
            while True:
                if '@' not in uMail:
                    print('입련한 이메일 주소가 형식에 맞지 않습니다. ')
                    uMail = input('Input member EMAIL: ')
                else:
                    break

            uPhone = input('Input member PHONE: ')

            setNewMember(uId, uPw, uMail, uPhone)

            print('SIGN-UP SUCCESS!!')

            if DEV_MOD: print(f'members: {members}')

    elif userSelectedMunuNum == SIGN_IN:            # 2.로그인 
        signInCount = 1
        while True:
            uId = input('Input member ID: ')
            uPw = input('Input member PW: ')

            if uId in members:
                uInfo = members[uId]
                if uInfo['uPw'] == uPw:
                    print('SIGN-IN SUCCESS!!')
                else:
                    print('SIGN-IN FAIL!!')
                    signInCount += 1
                    if signInCount > 3:
                        print('3회 이상 틀렸어요!!')
                        break
            else:
                print('SIGN-IN FAIL!!')
        else:
            print('존재 하지 않은 ID입니다. 다시 확인하세요.')
            print('존재 하지 않은 ID입니다. 다시 확인하세요.')


    # elif selectedMenuNum == PRINT_MY_INFO:      # 3.나의 정보 출력  
    elif userSelectedMunuNum == PRINT_MY_INFO:      # 3.나의 정보 출력  
        uId = input('Input member ID: ')
        uPw = input('Input member PW: ')

        if uId in members:
            uInfo = members[uId]
            if uInfo['uPw'] == uPw:
                print('SIGN-IN SUCCESS!!')

                print('-' * 30)
                for key, value in uInfo.items():
                    print(f'{key}: {value}')
                print('-' * 30)

            else:
                print('SIGN-IN FAIL!!')
        else:
            print('존재 하지 않은 ID입니다. 다시 확인하세요.')

    # elif selectedMenuNum == PRINT_ALL_MEMBER_INFO:      # 4.모든 회원 정보 출력
    elif userSelectedMunuNum == PRINT_ALL_MEMBER_INFO:      # 4.모든 회원 정보 출력
        for key, value in members.items():
            print(f'{key}님의 정보 ----------------')
            for key1, value1 in value.items():
                print(f'{key1}: {value1}')
            printAllMemberInfo(value)
            print('-' * 30)

    # elif selectedMenuNum == SYSTEM_SHUTDOWN:    # 99.종료
    elif userSelectedMunuNum == SYSTEM_SHUTDOWN:    # 99.종료
        flag = False
        print('Good bye~')

# 성진님 코드

totalUserInfoDict = {}

def menuSelection():
    userInputNum = int(input(
    '원하는 항목을 선택하세요. 1. 회원가입  2. 로그인  3. 특정 회원 정보 출력  4. 모든 회원 정보 출력  5. 회원정보 수정  99. 종료 : '
    ))

    return userInputNum




def userinfoData():
    userInputId = input('ID를 입력하세요.')
    userInputPw = input('PW를 입력하세요.')
    userInputEmail = input('Email을 입력하세요.')
    userInputPhoneNum = input('핸드폰 번호를 입력하세요.')

    userInfodict = {
        'ID': userInputId,
        'PW': userInputPw,
        'Email': userInputEmail,
        'PhoneNum': userInputPhoneNum
    }

    userInfodict = {userInputId: userInfodict}
    return userInfodict


def checkUserLogin():
    userInputId = input('ID를 입력하세요.')
    userInputPw = input('PW를 입력하세요.')

    if userInputId in totalUserInfoDict and totalUserInfoDict[userInputId]['PW'] == userInputPw:
        print('로그인 성공!')
    else:
        print('로그인 실패 다시 입력해주세요!')


def checkUserData():
    userInputId = input('ID를 입력하세요.')
    userInputPw = input('PW를 입력하세요.')

    if userInputId in totalUserInfoDict and totalUserInfoDict[userInputId]['PW'] == userInputPw:
        print(f'ID : {userInputId} 님의 정보는 {totalUserInfoDict[userInputId]}입니다.')


def changeUserInfo():
    userInputId = input('ID를 입력하세요.')
    userInputPw = input('PW를 입력하세요.')

    if userInputId in totalUserInfoDict and totalUserInfoDict[userInputId]['PW'] == userInputPw:
        print('로그인 성공!')

        userInputNum = int(input('변경하고 싶은 회원정보 1. 비밀번호, 2. 이메일, 3. 핸드폰 번호: '))

        if userInputNum == 1:
            totalUserInfoDict[userInputId]['PW'] = input('변경하고 싶은 비밀번호 : ')

        elif userInputNum == 2:
            totalUserInfoDict[userInputId]['Email'] = input('변경하고 싶은 이메일주소 : ')

        elif userInputNum == 3:
            totalUserInfoDict[userInputId]['PhoneNum'] = input('변경하고 싶은 핸드폰번호 : ')

        else:
            print('번호를 다시 입력해주세요.')

    else:
        print('로그인 실패 다시 입력해주세요!')


flag = True

while flag:
    menu = menuSelection()


    if menu == 99:
        flag = False
        print('프로그램을 종료합니다.')

    elif menu == 1:
        userInfodict = userinfoData()

        for userId in userInfodict:
            totalUserInfoDict[userId] = userInfodict[userId]

    elif menu == 2:
        checkUserLogin()

    elif menu == 3:
        checkUserData()

    elif menu == 4:
        print(f'모든 회원 정보: {totalUserInfoDict}')

    elif menu == 5:
        changeUserInfo()

    else:
        print('번호를 다시 입력해주세요.')