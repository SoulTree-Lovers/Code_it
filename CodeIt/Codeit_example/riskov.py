class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        self.name = name
        self._wage = wage

    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self._wage *= self.raise_percentage

    @property
    def wage(self):
        return self._wage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


class Cashier(Employee):
    """리스코프 치환 원칙을 지키지 않는 계산대 직원 클래스"""
    burger_price = 4000

    def __init__(self, name, wage, number_sold=0):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def raise_pay(self, raise_amount):
        """직원 시급을 인상하는 메소드"""
        self.wage += self.raise_amount

    @property
    def wage(self):
        return "시급 정보를 알려줄 수 없습니다"

# Employee 인스턴스들 생성
employee_1 = Employee("성태호", 7000)
employee_2 = Employee("강영훈", 6500)

# Cashier 인스턴스 생성
cashier = Cashier("김대위", 9000)

# 생성한 모든 직원 인스턴스들을 리스트에 추가
employee_list = []
employee_list.append(employee_1)
employee_list.append(employee_2)
employee_list.append(cashier)

# 모든 직원들의 시급 인상
for employee in employee_list:
    employee.raise_pay()

# 모든 직원들의 총 시급 구하기
total_wage = 0

for employee in employee_list:
    total_wage += employee.wage

print(total_wage)
