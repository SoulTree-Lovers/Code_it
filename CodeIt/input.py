import random

answer = random.randint(1, 21)

for i in range(4, 0, -1):
    num = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(i)))    
    if num < answer:
        print("Up")
        if i == 1:
            print("아쉽습니다. 정답은 {}였습니다.".format(answer))
        
    elif num > answer:
        print("Down")
        if i == 1:
            print("아쉽습니다. 정답은 {}였습니다.".format(answer))
    
    else:
        print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(4-i))
        break
    