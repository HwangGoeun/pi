###
#원주율 구하기 (터틀 있는 ver.)
###
import random
import turtle
t=turtle.Turtle()
t.shape("turtle")

#사각형+원 만들기
#원은 반지름이 100, 사각형은 각 변의 길이가 200인 정사각형
t.speed(5)
t.pd()
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(200)
t.rt(180)
t.fd(100)
t.lt(90)
t.fd(100)
t.rt(180)
t.fd(200)
t.lt(90)
t.circle(100)

#점 찍고 파이 구하기
cnt = 0 #원 안의 점 갯수
t.speed(10) #터틀 속도 제어
pi = 0 #파이값
re = 100 #반복 횟수

for i in range(re):
    x = random.uniform(-100,100) #x,y 좌표값 랜덤으로 구하기
    y = random.uniform(-100,100)
    t.pu() #거북이의 경로 표시 X
    t.goto(x,y) #랜덤으로 정해진 좌표로 거북이 이동
    if((x**2)+(y**2)<=10000): #좌표의 값을 피타고라스의 정리로 계산했을 때, 반지름의 길이 이하이면
        cnt += 1 #원 안의 점 갯수 +1
        t.pd() #펜 내리기
        t.color("red") #거북이 색깔은 빨간색으로 바꾸기
        t.dot(10) #10 크기의 점 찍기
    else: #아니라면
        t.pd() #펜 내리기
        t.color("blue") #거북이 색깔은 파란색
        t.dot(10) #10크기의 점 찍기

pi = (cnt/re)*4 #파이의 값 계산
print(f"파이의 값은 {pi}입니다.")

turtle.mainloop()
turtle.bye()

'''
###
#파이 구하기 (터틀 없는 ver.)
#(터틀로 점 찍으면서 구하면 너무 시간이 오래 걸려서 만들었습니다)
###
import random

cnt = 0 #원 안에 들어간 점 갯수
re = 10000000 #반복 횟수

for i in range(re):
    x = random.random() #0~1까지의 실수 랜덤으로 고르기
    y = random.random()
    if(x*x + y*y <= 1): #위의 식처럼 피타고라스 정리 했을 때 1이하면
        cnt += 1 #원 안에 들어간 점 갯수 +1

print("pi=",str((cnt/re)*4))
'''