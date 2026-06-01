# 할당(대입) 연산자
# 할당 연산자는 변수에 값을 대입하는 데 사용하는 연산자로 대입 연산자라고도 합니다.

# 할당 연산자(=)
num = 5

# 복합대입 연산자(+=, -=, *=, /=, %=, //, **=)

# num = num + 5
num += 5

# num = num - 5
num -= 5

# num = num * 5
num *= 5

# num = num / 5
num /= 5

# num = num % 5
num %= 5

# num = num // 5
num //= 5

# num = num ** 5
num **= 5


#quiz> 복리계산기
# 500만원씩 5년 만기인 정기 예금 상품에 가입했을때 5년후 받을 총 수령액 계산(이자율: 연5%)

myMoney = 5000000
rate = 0.05

myMoney = myMoney + (myMoney * rate)      # 1년후 총 금액

myMoney = myMoney + (myMoney * rate)      # 2년후 총 금액

myMoney = myMoney + (myMoney * rate)      # 3년후 총 금액

myMoney = myMoney + (myMoney * rate)      # 4년후 총 금액

myMoney = myMoney + (myMoney * rate)      # 5년후 총 금액

print(f'5년 후 총 수령액: {int(myMoney):,}원')
