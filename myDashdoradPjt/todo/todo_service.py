import session
import os
import json
from util import util_time
from todo.config import *

class TodoService:
    def __init__(self):
        self.todos = {}
        self.init_database()

    def init_database(self):
        # 현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH:{BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR:{ROOT_DIR}')

        self.dbFile = os.path.join(ROOT_DIR, 'db', 'todos.json')

        if not os.path.exists(self.dbFile):
            self.save_todos(self.todos)

        else:
            self.todos = self.load_todos()

    # json 에 저장
    def save_todos(self, todos):
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(todos, f, ensure_ascii=False, indent=4)


    def load_todos(self):
        with open(self.dbFile, 'r' , encoding='utf-8' ) as f:
            return json.load(f)
            
        
    def isMytodos(self):
        alltodos = self.load_todos()
        if session.getsignInedMemberId() in alltodos:
           
            return True
        
        return False

    def run(self):

        if session.getsignInedMemberId() == '':
            print('로그인 후 이용 부탁드립니다.')
            return
        
        flag = True
        while flag:

            if not self.isMytodos():
                self.todos[session.getsignInedMemberId()] = []
                self.save_todos(self.todos)

            menuNum = int(input('1.신규작성    2.조회    3.수정    4.삭제    5.완료체크    0.메인메뉴로'))
            
            if menuNum == WRITE:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getsignInedMemberId()]
                
                tText = input('일정을 작성 해주세요.')
                tExpDate = input('일정 만료기간 설정(ex.2026-08-05 06:09:09):')

                todo = {
                    'tText':tText,
                    'tExpDate':tExpDate,
                    'tRehData':util_time.getCurrentDateTime(),
                    'tModDate':util_time.getCurrentDateTime(),
                    'tComplete':False

                }
                myTodos.insert(0, todo)
                self.save_todos(self.todos)
                print(f'[{tText}] 정상적으로 일정이 등록 완료 되었습니다.')

            elif menuNum == READ:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getsignInedMemberId()]
                for idx, myTodo in enumerate(myTodos):
                    print('-' * 50)
                    print(f'[{idx + 1}]')
                    print(f'일정: {myTodo['tText']}')
                    print(f'내가 등록한 만료일자: {myTodo['tExpDate']}')
                    print(f'일정 처음으로등록한 일자: {myTodo['tRehData']}')
                    print(f'일정 마지막으로수정한 일자: {myTodo['tModDate']}')
                    print(f'일정 완료여부: {myTodo['tComplete']}')
                    print('-' * 50)


            elif menuNum == UPDATE:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getsignInedMemberId()]
                for idx, myTodo in enumerate(myTodos):
                    print('-' * 100)
                    print(f'[{idx + 1}] {myTodo['tText']} {myTodo['tExpDate']}')
                    print('-' * 100)
                    
                todoNumber = int(input('수정할 일정의 번호를 입력하세요.'))

                tText = input('수정할 일정을 작성 해주세요.')
                tExpDate = input('수정할 일정 만료기간 설정(ex.2026-08-05 06:09:09):')
                
                todo = {
                    'tText':tText,
                    'tExpDate':tExpDate,
                    'tRehData':myTodos[todoNumber-1]['tRehData'],
                    'tModDate':util_time.getCurrentDateTime(),
                    'tComplete':myTodos[todoNumber-1]['tComplete']

                }

                myTodos[todoNumber-1] = todo
                self.save_todos(self.todos)
                print('일정이 정상적으로 업데이트 되었습니다.')

            elif menuNum == DELETE:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getsignInedMemberId()]
                for idx, myTodo in enumerate(myTodos):
                    print('-' * 100)
                    print(f'[{idx + 1}] {myTodo['tText']} {myTodo['tExpDate']}')
                    print('-' * 100)
                    
                todoNumber = int(input('삭제할 일정의 번호를 입력하세요.'))
                # myTodos.pop(todoNumber-1)
                del myTodos[todoNumber-1]
                self.save_todos(self.todos)
                print('정상적으로 삭제 완료되었습니다.')

            elif menuNum == COMPLETE_CHANGE:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getsignInedMemberId()]
                for idx, myTodo in enumerate(myTodos):
                    print('-' * 100)
                    print(f'[{idx + 1}] {myTodo['tText']} {myTodo['tExpDate']}')
                    print('-' * 100) 

                todoNumber = int(input('완료할 일정을 선택하세요.'))
                myTodos[todoNumber-1]['tComplete'] = not myTodos[todoNumber-1]['tComplete']
                self.save_todos(self.todos)
                print('완료처리 되었습니다.')


            elif menuNum == SERVICE_OUT:
                flag = False
                print('처음으로 돌아갑니다.')



if __name__=="__main__":
    bankService = TodoService()
    bankService.run()