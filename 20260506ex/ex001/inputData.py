# 데이터 입력 (input data)
# input()


print('데이터를 입력하세요.')
inputData = input()
print(inputData)


print('정수를 입력하세요.')
inputIntegr = input()           #6
print(inputIntegr)              #6
print(type(inputIntegr))        #str


print('실수 입력하세요.')
inputFloat = input()
print(inputFloat)
print(type(inputFloat))


print('논리형 데이터 입력하세요.', end='') #논리형 데이터를 입력하세요.(자동개행)
inputBoolean = input()
print(inputBoolean)
print(type(inputBoolean))



inputBoolean = input('논리형 데이터 입력하세요.\n')
print(inputBoolean)
print(type(inputBoolean))

# 자료형을 변환해야 한다 (data type casting)
userInputData = input('사용자야~~~~ 정수 입력해라~')
print(userInputData)
print(type(userInputData))
userInputData = int(userInputData)
print(type(userInputData))

# str -> boolean
userInputData = input('True or False 입력하세요.')
print(userInputData)
print(type(userInputData))
userInputData = bool(userInputData)
print(type(userInputData))

# ser -> float
userInputData = input ('실수를 입력하세요')
print(userInputData)
print(type(userInputData))
userInputData = float(userInputData)
print(type(userInputData))

userInpudata = 'True'
userInpudata = bool(userInpudata)
print(type(userInpudata))

x = 3
y = float(x)
print(y)

x = 3.141592
y = int(x)
print(y)
print(float(y))
