from random import randint

# 컴퓨터는 0과 9 사이의 서로 다른 숫자 3개를 무작위로 뽑습니다.
def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        n = randint(0,9)
        if n not in numbers:
            numbers.append(n)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


# 사용자는 컴퓨터가 뽑은 숫자의 값과 위치를 맞추어야 합니다.
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []

    while len(new_guess) < 3:
        num = int(input(f"{len(new_guess) + 1}번째 숫자를 입력하세요:"))
        if (num not in new_guess and 0<=num<=9):
            new_guess.append(num)
        elif num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
    return new_guess


# 컴퓨터는 사용자가 입력한 숫자 3개에 대해서, 아래의 규칙대로 스트라이크와 볼의 개수를 알려줍니다.
def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif (guesses[i] in solution):
            ball_count += 1
    


    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    guess = take_guess()
    s, b = get_score(guess, ANSWER)
    if (guess == ANSWER):
        break
    else:
        print("{}S {}B".format(s, b))
        tries += 1
    
    

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))

# 기회는 무제한입니다. 하지만 몇 번의 시도 끝에 맞췄는지 기록됩니다.

# 3S가 나오면 게임이 끝납니다.

