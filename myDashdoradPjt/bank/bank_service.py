from bank.config import *
import session
import os
import json
import uuid
from util import util_time

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
                menNum = int(input('1.입출금내역   2.신규개설   3.입금   4.출금   0.메인메뉴로'))

            else:
                print('계좌가 없습니다. 신규 개설 후 이용 부탁드립니다.')
                menNum = int(input('2.신규개설   0.메인메뉴로'))

            if menNum == ACCOUNT_LIST:
                self.accounts = self.load_accounts()
                myAccounts = self.accounts[session.getsignInedMemberId()]

                for idx, myAccount in enumerate(myAccounts.keys()):
                    print('=' * 80)
                    print(f'{myAccounts[myAccount]['uAccountName']}')
                    print(f"[{idx + 1}]: {myAccounts[myAccount]['uAccountName']}계좌: {myAccount}:  {myAccounts[myAccount]['balance']}")
                    print('-' * 80)
                    print('날짜/시간 \t\t 내역 \t\t\t 입금 \t\t 출금')
                    for history in myAccounts[myAccount]['histories']:
                        if 'dAmount' in history:
                            print(f'{history["dRegData"]}\t {history["dHistory"]} \t\t {history["dAmount"]}')
                        else:
                             print(f'{history["wRegDate"]}\t {history["wHistory"]} \t\t\t\t {history["wAmount"]}')
                    print()
            elif menNum == NEWACCOUNT:
                self.accounts = self.load_accounts()
                if session.getsignInedMemberId() not in self.accounts:
                    self.accounts[session.getsignInedMemberId()] = {}

                print('사용할 비밀번호를 입력해주세요')
                uPass = int(input('비밀번호:'))
                uAccountName = input('계좌 이름 설정:')

                myAccounts = self.accounts[session.getsignInedMemberId()]
                myAccounts[str(uuid.uuid4())] = {
                    'uAccountName':uAccountName,
                    'balance':0,
                    'password':uPass,
                    'histories':[]
                }

                self.save_accounts(self.accounts)
                print(f'{uAccountName}계좌개설이 완료되었습니다.')

            elif menNum == DEPOSIT:
                self.accounts = self.load_accounts()
                myAccounts = self.accounts[session.getsignInedMemberId()]

                print('\n---------------현재 계좌 현황-----------------')
                for idx, account in enumerate(myAccounts.keys()):
                    print(f'[{idx + 1}]:{account}')
                print('\n--------------------------------------------')

                depositAccountNumber = ''

                while True:

                    print('원하는 계좌번호를 입력 해주세요.')
                    depositAccountNumber = input('계좌 번호:')

                    if depositAccountNumber not in myAccounts:
                        print('현재 입력한 계좌번호는 없는 번호입니다.')
                        print('\n---------------현재 계좌 현황-----------------')
                        for idx, account in enumerate(myAccounts.keys()):
                            print(f'[{idx}]:{myAccounts[myAccount]['uAccountName']}{account}')
                        print('\n--------------------------------------------')

                    else:
                        break
                

                depositAmount = int(input('입금할 금액:'))
                depositHistory = input('입금 기록을 입력하세요:')
                deposit = {
                    'dAmount':depositAmount,
                    'dHistory':depositHistory,
                    'dRegData':util_time.getCurrentDateTime(),
                    'dMpdData':util_time.getCurrentDateTime()
                }

                myAccounts[depositAccountNumber]['balance'] += depositAmount
                myAccounts[depositAccountNumber]['histories'].insert(0, deposit)

                self.save_accounts(self.accounts)
                print(f'{depositAmount:,}입금이 완료되었습니다.')


            elif menNum == WITHDRAWAL:
                
                self.accounts = self.load_accounts()
                myAccounts = self.accounts[session.getsignInedMemberId()]

                print('\nMy Accounts-----------------------------------')
                for idx, account in enumerate(myAccounts.keys()):
                    print(f'[{idx+1}]: {account}')
                print('----------------------------------------------\n')

                withdrawalAccountNumber = ''
                
                while True:
                    withdrawalAccountNumber = input('출금할 계좌 번호를 입력하세요.')
                    if withdrawalAccountNumber not in myAccounts:
                        print('The account was not found!!')
                        print('\nMy Accounts-----------------------------------')
                        for idx, account in enumerate(myAccounts.keys()):
                            print(f'[{idx+1}]:{myAccounts[myAccount]['uAccountName']} {account}')
                        print('----------------------------------------------\n')
                    else:
                        break

                withdrawalAmount = int(input('출금할 금액을 입력하세요: '))
                withdrawalHistory = input('출금기록 입력: ')
                withdrawal = {
                    'wAmount': withdrawalAmount,
                    'wHistory': withdrawalHistory,
                    'wRegDate': util_time.getCurrentDateTime(),
                    'wModDate': util_time.getCurrentDateTime()
                }

                if withdrawalAmount > myAccounts[withdrawalAccountNumber]['balance']:
                    print('잔액이 부족합니다.')

                else:
                    myAccounts[withdrawalAccountNumber]['balance'] -= withdrawalAmount
                    myAccounts[withdrawalAccountNumber]['histories'].insert(0, withdrawal)

                    self.save_accounts(self.accounts)
                    print('출금이 완료 되었습니다.')

            elif menNum == SERVICE_OUT:
                flag = False
                print('처음으로 돌아갑니다.')


if __name__=="__main__":
    bankService = BankService()
    bankService.run()