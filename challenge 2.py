###
#while문
###
ja = 4 #ja=분자
mo = 2 #mo=분모
pi = 3+(ja/(mo*(mo+1)*(mo+2))) #pi=파이값
re = 300 #re=반복횟수

while re>0:
    ja *= -1
    mo += 2
    pi = pi+(ja/(mo*(mo+1)*(mo+2)))
    re -= 1

print(f"pi={pi}")


###
#for문
###
ja = 4 #ja=분자
mo = 2 #mo=분모
pi = 3+(ja/(mo*(mo+1)*(mo+2))) #pi=파이값

for i in range(300):
    ja *= -1
    mo += 2
    pi = pi+(ja/(mo*(mo+1)*(mo+2)))

print(f"pi={pi}")