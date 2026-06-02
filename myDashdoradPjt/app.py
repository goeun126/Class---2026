from config import *
from member.member_service import MemberSerive
from bank.bank_service import BankService
from memo.memo_service import MemoService
from todo.todo_service import TodoService



def main():
    flag = True
    while flag:
        menuNum = int(input('1.회원관리   2.계좌   3.메모   4.일정   0.종료'))
        if menuNum == MEMBER_SERVICE:
            MemberSerive().run()
            
        elif menuNum == BANK_SERVICE:
            BankService().run()
            
        elif menuNum == MEMO_SERVICE:
            MemoService().run()

        elif menuNum == TODO_SERVICE:
            TodoService().run()

        elif menuNum == SYSTEM_OUT:
            flag = False
            print('시스템을 종료합니다.')

if __name__=="__main__":
    main()