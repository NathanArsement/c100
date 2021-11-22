import time


class Atm(object):
    def __init__(self,cardNo, pin, AMOUNT):
        self.pin=pin
        self.cardNo=cardNo
        self.AMOUNT=AMOUNT
    
    def CashWithdrawl(self, amount):
        self.AMOUNT-=amount
    def CashDeposit(self, deposit):
        self.AMOUNT+=deposit
    def BalanceEnquiry(self):
        print(self.AMOUNT)

atm=Atm(0000, 111212121, 1000)
wh=1
while wh==1:
    ask=int(input('''
    What do you want to do?
    1. Withdrawl
    2. Deposit
    3. Check Balance
    4. Stop
    '''))
    if ask==1:
        choose=int(input("How much?"))
        atm.CashWithdrawl(choose)
    elif ask==2:
        choose=int(input("How much?"))
        atm.CashDeposit(choose)
    elif ask==3:
        atm.BalanceEnquiry()
    elif ask==4:
        wh=0
    else:
        print("Choose Correctly")
    time.sleep(1)
