goods = {
    '새우깡':1200,
    '비비빅':400,
    '초코파이':500,
    '맛동산':1500
}

totalpricr = 0

def shrimpCrackers():
    global totalpricr
    totalpricr += goods['새우깡'] * shrimp_count
    print(f'새우깡 구매 금액: {goods['새우깡'] * shrimp_count}원')
    
def bibibig():
    global totalpricr
    totalpricr += goods['비비빅'] * bibiBig
    print(f'비비빅 구매 금액: {goods['비비빅'] * bibiBig}원')

def chocoPie():
    global totalpricr
    totalpricr += goods['초코파이'] * chocopie
    print(f'초코파이 구매 금액: {goods['초코파이'] * chocopie}원')

def matdongsan():
    global totalpricr
    totalpricr += goods['맛동산'] * matDongsan
    print(f'맛동산 구매 금액: {goods['맛동산'] * matDongsan}원')


shrimp_count = int(input('새우깡 구매 개수: '))
bibiBig = int(input('비비빅 구매 개수: '))
chocopie = int(input('초코파이 구매 개수: '))
matDongsan = int(input('맛동산 구매 개수: '))


print(f'새우깡 구매 개수:{shrimp_count}')
print(f'비비빅 구매 개수:{bibiBig}')
print(f'초코파이 구매 개수:{chocopie}')
print(f'맛동산 구매 개수:{matDongsan}')

print('=' * 40)
shrimpCrackers()
bibibig()
chocoPie()
matdongsan()
print('=' * 40)
print(f'총 구매 금액:{totalpricr}원')
print('=' * 40)

