# split(쪼갠다)

names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')
print(f'names:{names}')
print(f'names type:{type(names)}')

str = "박찬호+이승엽+박세리+박지성+이순철+선동열+손흥민+김연아"
splitedStr = str.split("+")                 # list -> tuple
print(f'splitedStr:{splitedStr}')
print(f'namsplitedStres type:{type(splitedStr)}')


splitedStr = tuple(splitedStr)
print(f'splitedStr:{splitedStr}')
print(f'namsplitedStres type:{type(splitedStr)}')