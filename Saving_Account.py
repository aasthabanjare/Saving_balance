class SavingsAccount:
    def __init__(self, annual_Inter_rate, saving_balance):
        self.annual_Inter_rate = annual_Inter_rate
        self.saving_balance = saving_balance

    def MonthlyInterest(self):
        self.monthly_interest = (self.annual_Inter_rate*self.saving_balance)/1200
        print("Monthly Interest: ",self.monthly_interest)
        self.saving_balance += self.monthly_interest
        print("Saving Balance :", self.saving_balance)

    def modifyInterestRate(self,rate):
        self.annual_inter_rate = rate


sarver1 = SavingsAccount(5, 2000)
sarver2 = SavingsAccount(5, 3000)

sarver1.MonthlyInterest()
sarver2.MonthlyInterest()

sarver1.modifyInterestRate(7)
sarver2.modifyInterestRate(7)

sarver1.MonthlyInterest()
sarver2.MonthlyInterest()





