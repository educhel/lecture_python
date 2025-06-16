# 입금과 출금, 조회

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder 
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

# 객체 생성 및 메서드 호출
account = BankAccount("홍길동")

# 잔액 조회
print(f"초기 잔액: {account.balance}원")

# 입금
account.deposit(1500)

# 출금
account.withdraw(10000000000)

# 잔액 조회
print(f"현재 잔액: {account.balance}원")

account.withdraw(1200)

print(f"현재 잔액: {account.balance}원")

# 계좌 소유자 조회
print(f"계좌 소유자: {account.account_holder}")