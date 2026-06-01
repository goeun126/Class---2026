file = open('C:/lge/python/test.txt', 'w') # 파일을 '쓰기' 모드로 open한다.
result = file.write('Hello python!')       # 쓰기(write)
print(f'result:{result}')
file.close()                               # 파일 닫기(외부자원 해제)

file = open('C:/lge/python/test.txt', 'r')
readResult =  file.read()
print(f'readResult:{readResult}')
print(f'readResult:{type(readResult)}')

readResult = int(readResult)
readResult += 1
print(f'readResult:{readResult}')

file.close()

file = open('C:/lge/python/test.txt', 'a') 
file.write('\nhello~')
file.close()

file = open('C:/lge/python/test.txt', 'a') 
file.write('\nhi~')
file.close()

with open('C:/lge/python/test.txt', 'a') as file:
    for n in range(10):
     file.write('\nhello~')

# 예외 처리(보험)
# 세상에 모든 프로그램은 100% 완벽할수 없다.

try:
    print(10 / 0)
    print(10 + 20)
    print(10 - 20)
    print(10 * 20)
except Exception as e:
    print(f'e:{e}')

else:
   print('에러가 발생하지않으면 실행되는 코드')

finally:
   print('에러가 발생하든 안하든 무조건 실행되는 코드')

# 예외 처리 기본 문법
# try ~ Exception
