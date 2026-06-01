import config
from util import gotDay, getTime

dFlag = True

while dFlag:
    selectedMenuNum = int(input('메뉴:1. 일기작성    2.일기조회    0.종료-->'))

    if selectedMenuNum == config.DIARY_WRITE:

        print(f'[{gotDay()}]할줄 일기를 작성하세요.')

        todayDiary = input()
        with open('C:\lge\python\diary.txt', 'a') as f:
            f.write(f'[{gotDay()} {getTime()}] {todayDiary}\n')

    elif selectedMenuNum == config.DIARY_READ:
        with open('C:\lge\python\diary.txt', 'r') as f:
            str = f.read
            print(str)

    elif selectedMenuNum == config.SYSTEM_SHUTDOWM:
        print('안녕히가세요.')
        dFlag = False
    
    else:
        print('번호를 잘못 입력했습니다. 다시 입력하세요.')