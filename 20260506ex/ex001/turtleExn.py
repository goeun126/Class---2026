#회전하는각도 (amgle) 전진하는길이 (length) 정오각형 만들기
#정육각형의 내각은 72도

import turtle

t = turtle.Turtle()     #그림 그리기 준비 완료
t.shape('turtle')       #아이콘 설정
t.speed(1)

angle = int(input('회전 각도를 입력하세요. '))          #60
length = int(input('전진 길이를 입력하세요.'))          #100

t.left(angle)              #왼쪽으로 60도 회전
t.forward(length)          #100픽셀 실선 그리기

t.left(angle)              #왼쪽으로 60도 회전
t.forward(length)          #100픽셀 실선 그리기

t.left(angle)              #왼쪽으로 60도 회전
t.forward(length)          #100픽셀 실선 그리기

t.left(angle)              #왼쪽으로 60도 회전
t.forward(length)          #100픽셀 실선 그리기

t.left(angle)              #왼쪽으로 60도 회전
t.forward(length)          #100픽셀 실선 그리기
