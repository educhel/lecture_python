# 입금과 출금, 조회

# 케이스 1
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder 
        self.balance = balance

    def deposit(self, amount):
        if type(amount) == int and amount > 0:
            self.balance += amount
        else:
            print('잘못된 값입니다.')
    
    def withdraw(self, amount):
        if type(amount) == int and amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print('잔액이 부족합니다.')
        else:
            print('잘못된 값입니다.')
        
# 케이스 2

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