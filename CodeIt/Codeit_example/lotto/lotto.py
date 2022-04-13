from random import randint

def generate_numbers(n):
    num_list = []
    while len(num_list) < n:
        num = randint(1,45)
        if num not in num_list:
            num_list.append(num)
    return num_list

def draw_winning_numbers():
    draw_list = generate_numbers(6)
    draw_list.sort()
    while len(draw_list) < 7:
        num = randint(1, 45)
        if num not in draw_list:
            draw_list.append(num)
    return draw_list

def count_matching_numbers(list_1, list_2):
    count = 0
    for i in range(len(list_1)):
        if list_1[i] in list_2:
            count += 1
    return count

def check(numbers, winning_numbers):
    c = count_matching_numbers(numbers, winning_numbers)
    for i in numbers:
        if (i == winning_numbers[-1] and c == 6):
            return 50000000
    if c == 3:
        return 5000
    elif c == 4:
        return 50000
    elif c == 5:
        return 1000000
    elif c == 6:
        return 1000000000
    else:
        return 0