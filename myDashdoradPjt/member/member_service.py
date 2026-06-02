from util import util_time
import member.config as  member_config
import config as root_config
import os
import json
import session

class MemberSerive:
    def __init__(self):
        self.members = {}
        self.init_database()

    #회원 가입 기능
    def signUp(self):
        print('회원가입할 정보를 입력해주세요.')
        mId = input('아이디:')
        
        # id 중복체크를 할때 self.members 사용한다
        if mId in self.members:
            print('이미 사용중인 ID 입니다.')
            return

        mPw = input('비밀번호:')
        mMail = input('메일:')
        mPhone = input('연락처:')

        nowMember = {
            'mId':mId,
            'mPw':mPw,
            'mMail':mMail,
            'mPhone':mPhone,
            'mRegDate':util_time.getCurrentDateTime(),
            'mModDate':util_time.getCurrentDateTime()
        }

        self.members[mId] = nowMember

        # DB(member.json)에 새 회원 정보 저장
        self.save_members(self.members)
        
        print('성공적으로 회원가입이 성공되었습니다.')
        print(f'{mId}님 환영합니다!')

        if root_config.DEV_MOD:
            pass

    #회원 로그인 기능
    def signIn(self):
        print('아이디와 비밀번호를 입력해주세요.')
        mId = input('아이디:')
        mPw = input('비밀번호:')

        self.members = self.load_members()
        if mId in self.members and self.members[mId]['mPw'] == mPw:
            print('로그인 성공!')
            # session.signInedMemberId = mId
            session.setsignInedMemberId(mId)
            return
        
        print('로그인 실패: 아이디와 비밀번호를 다시 확인해주세요.')

    #회원 로그아웃 기능
    def signOut(self):
        session.setsignInedMemberId()
        print('로그아웃 성공!')

    #회원 수정 기능
    def modify(self):
        print('수정할 정보를 입력해주세요.')
        mPw = input('비밀번호 입력:')
        mMail = input('메일 입력:')
        mPhone = input('연락처 입력:')

        self.members = self.load_members()
        memberFoeModify = self.members[session.getsignInedMemberId()]
      
        memberFoeModify['mPw'] = mPw
        memberFoeModify['mMail'] = mMail
        memberFoeModify['mPhone'] = mPhone
        memberFoeModify['mModDate'] = util_time.getCurrentDateTime()

        self.save_members(self.members)

        print('수정이 완료되었습니다.')


    #회원 탈퇴 기능
    def delete(self):
        confirm = input('정말 탈퇴 하시겠습니까? [Y] or [N]')
        if confirm == 'Y':
            self.members = self.load_members()
            del self.members[session.getsignInedMemberId()]
            self.save_members(self.members)
            session.setsignInedMemberId()
            print('정상적으로 탈퇴처리 되었습니다.')
        else:
            print('메인메뉴로 돌아갑니다.')
            return
        
    def run(self):
        flag = True
        while flag:
            if session.getsignInedMemberId() == '':
                 menuNum = int(input('1.회원가입   2.로그인  0.종료'))
            else:
                 menuNum = int(input('3.로그아웃   4.회원정보수정   5.회원탈퇴   0.메인메뉴로'))

            if menuNum == member_config.SIGN_UP:
                self.signUp()
            elif menuNum == member_config.SIGN_IN:
                self.signIn()
            elif menuNum == member_config.SIGN_OUT:
                self.signOut()
            elif menuNum == member_config.MODIFY:
                self.modify()
            elif menuNum == member_config.DELETE:
                self.delete()
            elif menuNum == member_config.SERVICE_OUT:
                print('처음으로 돌아갑니다.')
                flag = False

    def init_database(self):
        
        # 현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH:{BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR:{ROOT_DIR}')

        self.dbFile = os.path.join(ROOT_DIR, 'db', 'members.json')

        if not os.path.exists(self.dbFile):
            self.save_members(self.members)

        else:
            self.members = self.load_members()

    # json 에 저장
    def save_members(self, members):
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(members, f, ensure_ascii=False, indent=4)


    def load_members(self):
        with open(self.dbFile, 'r' , encoding='utf-8' ) as f:
            return json.load(f)

if __name__=='__main__':
   memberSerive = MemberSerive()
   memberSerive.run()