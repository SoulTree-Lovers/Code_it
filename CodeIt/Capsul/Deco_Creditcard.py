class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
        self.__name = name
        self.__password = password
        self.__payment_limit = payment_limit
    
    @property
    def name(self):
        return self.__name
    
    @property
    def password(self):
        return "비밀 번호는 볼 수 없습니다"

    @property
    def payment_limit(self):
        return self.__payment_limit
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @password.setter
    def password(self, value):
        self.__password = value
    
    @payment_limit.setter
    def payment_limit(self, value):
        if 0 < value < CreditCard.MAX_PAYMENT_LIMIT:
            self.__payment_limit = value
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해주세요!")

card = CreditCard("강영훈", "123", 100000)

print(card.name)
print(card.password)
print(card.payment_limit)

card.name = "성태호"
card.password = "1234"
card.payment_limit = -10

print(card.name)
print(card.password)
print(card.payment_limit)