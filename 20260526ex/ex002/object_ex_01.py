# 클래스(객체를 만들기 위한 틀: 설계도) 문법

'''
user_taste = input('원하는 붕어빵 속을 입력하시오: ')
user_dough = input('원하는 붕어빵 반죽을 입력하시오: ')


class FisgBread:     # 클래스 선언
    def __init__(self, f, b):   # 속성(attribute)

        self.flour = f
        self.bean = b

    def makeFishBread(self):
        print('붕어빵 제조')      # 기능(function, method)

# 붕어빵 클래스로부터 객체를 만들어 봅시다.(객체 생성)
myFisgBread = FisgBread(user_taste, user_dough)
print(f'붕어빵 속 재료:{myFisgBread.flour},반죽재료: {myFisgBread.bean}')

# 계산기 클래스
class Calculator:
    # 속성
    def __init__(self, n1, n2):
        self.num1 = n1
        self.num2 = n2

    # 기능
    def add(self):
        print(f'add: {self.num1 + self.num2 }')

    def sub(self):
        print(f'add: {self.num1 - self.num2 }')

    def mul(self):
        print(f'add: {self.num1 * self.num2 }')

    def div(self):
        print(f'add: {self.num1 / self.num2 }')

# 인간 클래스
class Human:
    # 속성
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight


    # 기능
    def walk(self):
        print('걷자!')

    def run(self):
        print('뛰자!')

    def printMyInfo(self):
        print(f'나의 신장:{self.height}')
        print(f'나의 체중:{self.weight}')

import random

# quiz) 가위바위보

print('가위 바위 보를 입력하세요.')

class RockPaperScissors:
    # 속성
    def __init__(self):
        self.playerChoice = input('가위 바위 보')
        self.computerChoice = random.choice(['가위','바위','보'])

game = RockPaperScissors()

print(f'플레이어:{game.playerChoice}')
print(f'상대:{game.computerChoice}')

if game.playerChoice == game.computerChoice:
    print('비겻습니다.')

elif game.playerChoice =='가위' and game.computerChoice == '보':
    print('플레이어 승')

elif game.playerChoice =='보' and game.computerChoice == '바위':
    print('플레이어 승')

elif game.playerChoice =='바위' and game.computerChoice == '바위':
    print('플레이어 승')

else:
    print('플레이어 패')


class Words:
    def __init__(self):
        self.wordBook = {
            'Football':'축구',
            'Pencil':'연필',
            'Eraser':'지우개',
            'car':'차',
            'Doll':'인형',
            'Clock':'시계'
        }
        choices = self.wordBook.keys()
        quizWord = random.choice(list(choices))
        print(f'문제:{quizWord}')

        playerInput = input('정답: ')
        if playerInput == self.wordBook[quizWord]:
            print('정답입니다.')

        else:
            print('틀렸습니다.')
            print(f'정답:{self.wordBook[quizWord]}')

game = Words()
'''
from mp3 import *
import random

music = True

my_player = Mp3list()

while music:
    menu = int(input('1.곡추가   2.재생   3. 곡 제거   4.리스트출력   0.종료'))
    if menu == ADDSONG:
        user = input('추가할 곡제목만 입력해주세요:')
        my_player.playList.append(user)
        print(f'{user}.mp3 추가되었습니다.')
        print(f'현재 리스트{my_player.playList}')

    elif menu == PLAYMUSIC:
        print('재생모드를 선택해주세요.')
        playMode = int(input('5.일반재생 모드  6. 셔플재생 모드'))

        if playMode == PLAY_NORMAL:
            print('-----------일반재생 모드 ---------')
            print(f'{my_player.playList[0]}을 재생합니다.')
            pass

        elif playMode == PLAY_SEQUENTIAL:
            print('-----------셔플재생 모드 ----------')
            play = random.sample( my_player.playList, 1)
            print(f'{play[0]}을 재생합니다.')
            pass

    elif menu == REMOVESONG:

        while True:
            print('-----------목록-----------')
            print(*enumerate(my_player.playList), sep='\n')

            userSong= int(input('제거할 곡의 번호를 입력해주세요: '))

            if 0 <= userSong < len(my_player.playList):
                my_player.playList.pop(userSong)
                print('제거가 완료 되었습니다.')

            else:
                print('없는 번호입니다. 다시 입력 해주세요.')
                continue

            userChoice= int(input('1. 노래 추가 제거 2.다시 처음으로'))

            if userChoice == 1:
                pass

            elif userChoice == 2:
                print('메인 메뉴로 돌아갑니다.')
                break
            else:
                print('없는 번호입니다. 다시 입력 해주세요.')

    elif menu == SHOWLIST:
        print('-----------목록-----------')
        print(*enumerate(my_player.playList), sep='\n')

    elif menu == PLAY_END:
        print('종료합니다.')
        music = False