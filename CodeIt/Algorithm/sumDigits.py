# n의 각 자릿수의 합을 리턴
# def sum_digits(n):
#     index = 0
#     if index == len(str(n)) - 1:
#         return n 
#     else:
#         x = int(str(n)[index])
#         index += 1
#         return x + sum_digits(n - x * 10**(len(str(n)) - index))

# 해답
def sum_digits(n):
    # base case
    if n < 10:
        return n

    # recursive case
    return n % 10 + sum_digits(n // 10)

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))