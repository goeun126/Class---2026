from memo.config import *
import session
import os
import json

class MemoService:
    def __init__(self):
        self.memos = {}
        self.init_database()

    def init_database(self):
        # 현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH:{BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR:{ROOT_DIR}')

        self.dbFile = os.path.join(ROOT_DIR, 'db', 'memos.json')

        if not os.path.exists(self.dbFile):
            self.save_memos(self.memos)

        else:
            self.memos= self.load_memos() 

    def save_memos(self, memos):
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(memos, f, ensure_ascii=False, indent=4)

    def load_memos(self):
        with open(self.dbFile, 'r' , encoding='utf-8' ) as f:
            return json.load(f)
        
    def isMymemos(self):
        allMemo = self.load_memos()
        if session.getsignInedMemberId() in allMemo:
            return True
        
        return False


    def run(self):

        if session.getsignInedMemberId() == '':
            print('로그인 후 이용 부탁드립니다.')
            return
        
        flag = True

        while flag:
            if not self.isMymemos():
                self.memos[session.getsignInedMemberId()] = []
                self.save_memos(self.memos)
                
            menuNum = int(input('1.메모쓰기   2.메모읽기    3.메모수정    4.메모삭제    0.메인메뉴로'))

            if menuNum == WRITE:
                newMemo = input('새로운 메모를 작성해주세요.')

                self.memos = self.load_memos()
                myMemos = self.memos[session.getsignInedMemberId()]
                myMemos.insert(0, newMemo)

                self.save_memos(self.memos)
                print(f'[{newMemo}]정상적으로 등록되었습니다.')


            elif menuNum == READ:
                    self.memos = self.load_memos()
                    myMemos = self.memos[session.getsignInedMemberId()]
                    for idx, memo in enumerate(myMemos):
                        print(f'[{idx + 1}] {memo}')

            elif menuNum == UPATE:
                self.memos = self.load_memos()
                myMemos = self.memos[session.getsignInedMemberId()]
                for idx, memo in enumerate(myMemos):
                    print(f'[{idx + 1}] {memo}')

                selectedNumber = int(input('수정할 메모를 선택하세요:'))
                memo = input('수정할 메모 입력:')
                myMemos[selectedNumber-1] = memo

                self.save_memos(self.memos)
                print(f'[{memo}]으로 정상수정되었습니다.')

            elif menuNum == DWLETE:
                self.memos = self.load_memos()
                myMemos = self.memos[session.getsignInedMemberId()]
                for idx, memo in enumerate(myMemos):
                    print(f'[{idx + 1}] {memo}')

                selectedNumber = int(input('삭제할 메모를 선택하세요:'))
                myMemos.pop(selectedNumber-1)
                self.save_memos(self.memos)

            elif menuNum == SERVICE_OUT:
                flag = False
                print('처음으로 돌아갑니다.')

if __name__=="__main__":
    bankService = MemoService()
    bankService.run()