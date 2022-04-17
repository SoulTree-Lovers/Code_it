# 좌우동형 (재귀 X) #
def is_palindrome(word):
    new_word = ""
    for i in range(len(word)):
        new_word += word[len(word) - i - 1]
    
    if new_word == word:
        return True
    else:
        return False
        



# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))