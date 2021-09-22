class Atm(object):
    def __init__(card,pin,bank):
        self.card = card
        self.pin=pin
        self.bank=bank
       


    def  CashWithdrawl(self):
        print("CashWithDrawling ")

    def BalanceEnquiry(self):
        print(" balancing Enquring")

    def CashDeposit(self):
       print("Cash deposit ")
      
            

icic = Atm("card""pin""bankname")
icic.CashDeposit()