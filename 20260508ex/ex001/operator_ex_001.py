data = int(input('수심을 입력 하세요. '))
temperature = 20 - (data // 10 * .7)
print(f'temperature: {temperature}')

# 속도와 시간을 입력하면 자동차의 주행거리를 구하는 프로그램을 만드시오
speed = input('주행 속도: ')
time = input('주행 시간: ')
distance = int(speed) * int(time)
print(f'주행 거리: {distance}')

# quiz) 3대의 컴퓨터로 8시간 일하면 하루 업무를 처리 가능, 
# 단축근무로 시간이 줄게 되면 몇대에 컴퓨터가 필요한지 프로그램을 만드시오
time = int(input('근무시간을 입력하세요.:'))
computer = 3 * 8 // time
addComputer = 1 if (3 * 8 % time) > 0 else 0
totalComputer = computer + addComputer
print(f'필요한 컴퓨터 개수: {totalComputer}')

# 한개에 340원 마스크x개를 구매하고 y원을 지불햇을때 거스름돈 프로그램
maskPrice = 340
maskCnt = int(input('마스크 구매 개수: '))
totalPrice = maskPrice * maskCnt

cash = int(input('지불 금액: '))
change = cash - totalPrice

print(f'거스름돈: {(change):,}원')

# 13시 30분 25초를 초로 나타내는 프로그램
print(f'{25 + (60 * 30) + (60 * 60 * 13)}초')

# 국어, 영어, 수학 점수 평균
kor = int(input('국어 점수: '))
eng = int(input('영어 점수: '))
mat = int(input('수학 점수: '))
totalScore = kor + eng + mat
averageScore = totalScore / 3
print(f'총 점수: {totalScore}점')
print(f'평균: {averageScore}점')

#밤 최저 기온과 낮 최고 기온을 입력하면 일교차를 출력하는 프로그램
daytime = int(input('낮 최고 기온을 입력하세요.'))
night = int(input('밤 최저 기온을 입력하세요.'))
temperature = night - daytime
print(f'오늘의 최고기온 {daytime}도')
print(f'오늘의 최저기온 {night}도')
print(f'오늘의 일교차 {temperature}도')

# 사용자 길어(cm) 입력하면 inch로 환산하는 프로그램(1cm는 0.39inch)
length = int(input('길이를 입력 하세요.'))
totalInch = length * .39
print(f'inch: {totalInch}')