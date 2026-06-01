import lotto_ex as lm

nums = []
flag = True

print('1부터 45까지의 정수 6개를 입력')

while flag:
    userInput = int(input('1부터 45까지의 정수 6개를 입력:'))
    



lm.setUNumbers(nums)
lm.setRNumbers()

print(f'이번주 로또 번호:{lm.getRNumbers()}')
print(f'내가 선택한 로또 번호:{lm.getUNumbers()}')
print(f'일치하는번호:{lm.compareNumbers()}')