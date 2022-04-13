from collections import deque

stack = deque()

# 스택 맨 끝에 데이터 추가
stack.append("T")
stack.append("a")
stack.append("e")
stack.append("h")
stack.append("o")

# 스택 출력
print(stack)

# 맨 끝 데이터 접근
print(stack[-1])

# 맨 끝 데이터 삭제
print(stack.pop())
print(stack.pop())
print(stack.pop())

# 스택 출력
print(stack)