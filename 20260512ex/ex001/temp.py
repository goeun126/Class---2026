
# 데이터 중에서 실수는 현존하는 어떤 언어도 완벽하게 다룰 수 없다.
print(.1 + .2)    # 0.3 > 0.30000000000000004

fit = .1
while True:
    print(f'fit:{fit}')
    fit += .1

    if fit >= 1:
        break

total = .1 + .2
print(f"total: {total}")
if total > 0.3:
    print('total은 3보다 크다.')