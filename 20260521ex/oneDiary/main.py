from config_dir import config
from member import session
from db import member_db
from db import diary_db
from member import member_dumy
import copy
from datetime import datetime

if config.DEV_MOD:
    member_dumy.dumyInit()
    print(f'회원 데이터베이스(memberDB):{member_db.memberDB}')
    print(f'일기 데이터베이스(diary_DB):{diary_db.diaryDB}')

flag = True

while flag:

    menuNum = ''

    if session.signInedMemberId == '':
        menuNum = int(input(f'1.회원가입  2.로그인   6.일기쓰기   7.일기읽기   0.종료'))

    else:
        menuNum = int(input(f'3.정보수정  4.회원정보삭제   5.로그아웃  6.일기쓰기   7.일기읽기  8.일기삭제  0.종료'))


    if menuNum == config.SIGN_UP :
        print('--- 1. 회원가입 ---')
        uId = input('새로 사용할 아이디를 입력하세요::')
        uPw = input('새로 사용할 비밀번호를 입력하세요:')
        uMail = input('이메일 주소를 입력하세요:')
        uPhone = input('전화번호를 입력하세요(- 포함):')
        uRegDate = datetime.now().strftime("%Y-%m-%d %H:%M")

        member_db.memberDB[uId] = {
            'uId':uId,            # 아이디
            'uPw':uPw,            # 비밀번호
            'uMail':uMail,        # 이메일
            'uPhone':uPhone,      # 전화번호
        }

        print('회원가입에 성공하였습니다!')
        print(f'가입날짜:{uRegDate}')

        if config.DEV_MOD:
            print(f'회원 데이터베이스(memberDB):{member_db.memberDB}')

        diary_db.diaryDB[uId] = []
        if config.DEV_MOD:
            print(f'일기 데이터베이스(diaryDB):{diary_db.diaryDB}')




    elif menuNum == config.SIGN_IN:
        print('--- 2. 로그인 ---')
        uId = input('아이디를 입력하세요:')
        uPw = input('비밀번호를 입력하세요:')

        if uId in member_db.memberDB:
            if member_db.memberDB[uId]['uPw'] == uPw:
                print('로그인 성공!')
                print('원하는 메뉴를 고르세요.')
                session.signInedMemberId = uId

            else:
                print('로그인 실패: 비밀번호를 다시 확인해주세요.')
        else:
            print('로그인 실패: 존재하지 않는 아이디입니다.')


    elif menuNum == config.MEMBER_MODIFY:
        print('--- 3. 회원정보 수정 ---')

        uPw = input('변경할 비밀번호를 입력하세요:')
        uMail = input('변경할 이메일을 입력하세요:')
        uPhone = input('변경할 전화번호를 입력하세요:')
        uModDate = datetime.now().strftime("%Y-%m-%d %H:%M")

        currentSignInedMemberID = session.signInedMemberId
        memberInfo = member_db.memberDB[currentSignInedMemberID]
        if config.DEV_MOD: print(f'현재 회원 정보:{memberInfo}')

        memberInfo['uPw'] = uPw
        memberInfo['uModDate'] = uModDate
        memberInfo['uMail'] = uMail
        memberInfo['uPhone'] = uPhone

        print(f'회원정보 수정한 날짜:{uModDate}')
        print('회원정보가 성공적으로 수정되었습니다!')
        if config.DEV_MOD: print(f'변경 완료된 정보:{memberInfo}')

    elif menuNum == config.MEMBER_DELETE :
        print('--- 4. 회원탈퇴 ---')
        currentSignInedMemberID = session.signInedMemberId
        del member_db.memberDB[currentSignInedMemberID]
        del diary_db.diaryDB[currentSignInedMemberID]

        print('회원정보가 완전히 삭제되었습니다. 그동안 이용해 주셔서 감사합니다.')
        session.signInedMemberId = ''
        if config.DEV_MOD: print(f'회원 데이터베이스(memberDB):{member_db.memberDB}')

    elif menuNum == config.SIGN_OUT:
        print('--- 5. 로그아웃 ---')
        print('안전하게 로그아웃이 되었습니다.')
        session.signInedMemberId = ''

    elif menuNum == config.SYSTEM_OUT:
        print('프로그램을 종료합니다. 좋은 하루 되세요!')
        flag = False

    elif menuNum == config.DIARY_WRITE:
        print('--- 6. 일기 쓰기 ---')

        if session.signInedMemberId == '':
            print('죄송합니다. 로그인 후 이용 부탁드립니다.')
            

        else:
           while True:
            
               uModDate = datetime.now().strftime("%Y-%m-%d %H:%M")
               diaryTxt = input('10글자 이하의 짧은 일기를 작성하세요.')
               fullDiary = f"[{uModDate}] {diaryTxt}"
               if len(diaryTxt) == 0:
                  print('아무것도 입력되지않았습니다. 다시 확인 해주세요.')
            
               elif len(diaryTxt) > 10:
                     print(f'10글자 초과 했습니다.(현재{len(diaryTxt)}글자)')
               else:
                    currentSignInedMemberID = session.signInedMemberId
                    diary_db.diaryDB[currentSignInedMemberID].append(fullDiary)
                    print('일기가 성공적으로 등록되었습니다.')
                    if config.DEV_MOD:print(f'일기 데이터베이스(diaryDB):{diary_db.diaryDB}')
                    break
           
    elif menuNum == config.DIARY_READ:
        print('--- 7. 일기 읽기 (최신순) ---')
        
        if session.signInedMemberId == '':
            print('죄송합니다. 로그 후 이용 부탁드립니다.')
        
        else:
            currentSignInedMemberID = session.signInedMemberId
            myDiaries = diary_db.diaryDB[currentSignInedMemberID]

            if not myDiaries:
                print('아직 작성된 일기가 없습니다. 일기를 먼저 작성해주세요.')

            else:
                deepCoptedDiaries = copy.deepcopy(myDiaries)
                deepCoptedDiaries.reverse()

            for idx, diaryTxt in enumerate(deepCoptedDiaries):
                print(f'({idx+1}번 일기):{diaryTxt}')
   
    elif menuNum == config.DIARY_DEL:
        currentSignInedMemberID = session.signInedMemberId
        myDiaries = diary_db.diaryDB[currentSignInedMemberID]
        print('--- 8. 일기 삭제 ---')
        print(f'------현재 저장된 일기 목록--------')
        print(f'{myDiaries}')

        delDate = input('삭제할 날짜를 적어주세요 (-포함)')
        for idx in reversed(range(len(myDiaries))):
            if delDate in myDiaries[idx]:
               myDiaries.pop(idx)
               print('정상적으로 삭제 되었습니다.')

        userChoice = input('1. 추가삭제   2. 돌아가기')
        if userChoice == config.Choice1:
            pass

        elif userChoice == config.Choice2:
            pass