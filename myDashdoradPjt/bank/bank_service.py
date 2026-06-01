from bank.config import *
import session
import os
import json
import uuid

class BankService:
    def __init__(self):
        self.accounts = {}
        self.init_database()

    def init_database(self):
        # 현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH:{BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR:{ROOT_DIR}')

        self.dbFile = os.path.join(ROOT_DIR, 'db', 'accounts.json')

        if not os.path.exists(self.dbFile):
            self.save_accounts(self.accounts)

        else:
            self.accounts = self.load_accounts()

    # json 에 저장
    def save_accounts(self, accounts):
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(accounts, f, ensure_ascii=False, indent=4)


    def load_accounts(self):
        with open(self.dbFile, 'r' , encoding='utf-8' ) as f:
            return json.load(f)
            
        
    def isMyAccount(self):
        allAccount = self.load_accounts()
        if session.getsignInedMemberId() in allAccount:
           
            return True
        
        return False


    def run(self):

        if session.getsignInedMemberId() == '':
            print('로그인 후 이용 부탁드립니다.')
            return
            

        flag = True
        while flag:
            
            if self.isMyAccount():
                menNum = int(input('1.계좌목록   2.신규개설   3.입금   4.출금   0.메인메뉴로'))

            else:
                print('계좌가 없습니다. 신규 개설 후 이용 부탁드립니다.')
                menNum = int(input('2.신규개설   0.메인메뉴로'))

            if menNum == ACCOUNT_LIST:
                pass

            elif menNum == NEWACCOUNT:
                self.accounts = self.load_accounts()
                if session.getsignInedMemberId() not in self.accounts:
                    self.accounts[session.getsignInedMemberId()] = {}

                print('사용할 비밀번호를 입력해주세요')
                uPass = int(input('비밀번호:'))

                myAccouts = self.accounts[session.getsignInedMemberId()]
                myAccouts[str(uuid.uuid4())] = {
                    'baiance':0,
                    'passwors':uPass,
                    'histories':[]
                }

                self.save_accounts(self.accounts)
                print('새로운 계좌를 개설하신걸 축하드립니다!')

            elif menNum == DEPOSIT:
                pass

            elif menNum == WITHDRAWAL:
                pass

            elif menNum == SERVICE_OUT:
                flag = False


if __name__=="__main__":
    bankService = BankService()
    bankService.run()