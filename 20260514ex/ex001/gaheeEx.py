# 1.숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기
scores = [3, 7, 1, 9, 5]

max_num = scores[0]

for num in scores:
    if num > max_num:
        max_num = num

print(max_num)

# 2. 사용자에게 숫자 입력받아서
# 1부터 입력한 숫자까지 합계 출력하기 ( 5 )

myNum = int(input('숫자를 입력하시오.'))
num1 = myNum + 1
total = 0

for num in range(1, num1):
    total += num

print(f'{total}')

# 3. 리스트에 있는 숫자 중 짝수만 출력하기
list =  [1,2,3,4,5,6]

for num in list:
    if num % 2 == 0:
        print(f'짝수:{num}')
    else:
        print(f'홀수:{num}')

# 4. 리스트 숫자를 오름차순 정렬하기
list = [5,1,7,3]
list.sort()
print(f'list:{list}')

# 5. 리스트 숫자를 내림차순 정렬하기
list.sort(reverse=True)
print(f'list:{list}')

# 6. 리스트 안 숫자의 평균 구하기

list = [10,20,30]

list2 = sum(list)
list3 = len(list)
print(f'list:{list2 / list3}')

# 7. 리스트에서 가장 작은 숫자 찾기

scores = [3, 7, 1, 9, 5]

min_num = scores[0]

for num in scores:
    if num < min_num:
        min_num = num

print(min_num)

# 8. 1부터 100까지 숫자 중 3의 배수와 5의 배수 출력하기

for num in range(1,100):

    if num % 3 == 0:
        print(f'3의 배수: {num}')
        
    elif num % 5 == 0:
        print(f'5의 배수: {num}')

# 9. 사용자가 입력한 숫자를 리스트에 저장하다가 0 입력하면 종료 후 리스트 출력하기

num = []

while True:
    user = int(input('숫자를 입력하세요. 0입력시 종료'))

    if user == 0:
        print('종료')
        break

    num.append(user)
    print(f'현재까지 입력한 숫자:{num}')


print(f'입력한 숫자:{num}')
print(f'입력한 모든 숫자의 합계: {sum(num)}')