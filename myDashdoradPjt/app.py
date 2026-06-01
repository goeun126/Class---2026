from config import *
from member.member_service import MemberSerive
from bank.bank_service import BankService

def main():
    flag = True
    while flag:
        menuNum = int(input('1.회원관리   2.계좌   3.메모   4.일정   0.종료'))
        if menuNum == MEMBER_SERVICE:
            memberSerive = MemberSerive()
            memberSerive.run()
            
        elif menuNum == BANK_SERVICE:
            bank_service = BankService()
            bank_service.run()

        elif menuNum == MEMO_SERVICE:
            pass

        elif menuNum == TODO_SERVICE:
            pass

        elif menuNum == SYSTEM_OUT:
            flag = False

if __name__=="__main__":
    main()