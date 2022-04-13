class Clock:
    # 현재 시간을 설정하는 코드
    def __init__(self, time, minute, second):
        self.time = time
        self.minute = minute
        self.second = second

    # 현재 시간을 출력하는 코드
    def __str__(self):
        return f"{self.time}:".zfill(3) + f"{self.minute}:".zfill(3) + f"{self.second}".zfill(2)
    
    # 현재 시간을 재설정하는 코드
    def set(self, time, minute, second):
        self.time = time
        self.minute = minute
        self.second = second
    
    # 현재 시간을 늘리는 코드
    def tick(self):
        if self.second > 59:
            self.second = 1
            self.minute += 1
            if self.minute > 59:
                self.minute = 0
                self.time += 1
                if self.time > 23:
                    self.time = 0
        else:
            self.second += 1        


    
        
# 1시 30분 48초인 시계 인스턴스 생성
clock = Clock(1, 30, 48)
    
# 13초를 늘린다
for i in range(13):
    clock.tick()
    
# 시계의 현재 시간 출력
print(clock)
    
# 2시 3분 58초로 시계 세팅
clock.set(2, 3, 58)
    
# 5초를 늘린다
for i in range(5):
    clock.tick()
    
# 시계의 현재 시간 출력
print(clock)
    
# 23시 59분 57초로 세팅
clock.set(23, 59, 57)
    
# 5초를 늘린다
for i in range(365):
    clock.tick()
    
# 시계의 현재 시간 출력
print(clock)