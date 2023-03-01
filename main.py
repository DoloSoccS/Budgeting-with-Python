#Budgeting tool that will require all monthly bills statically input
#Pay schedule frequency will be necessary to allocate funds
#End result will be amount to leave in account for bills, amount to transfer for savings/debts, and the remaining balance for miscellaneous


class newBudget:
    def __init__(self, utilities, housing, autoLoan, insurances, studentLoans, debts, income):
        self.utilities = utilities
        self.housing = housing
        self.autoLoan = autoLoan
        self.insurances = insurances
        self.studentLoans = studentLoans
        self.income = income
        self.debts = debts / 12
        self.savings = income * 0.25
        self.livingExpenses = self.utilities + self.housing + self.autoLoan + self.insurances
        self.debts = self.studentLoans + self.debts


    def report(self):

        print("Total of all Living Expenses is: $" + str(self.livingExpenses))
        print("Total of all debts is: $" + str(self.debts))
        print("Total Savings commitment is: $" + str(self.savings))

    def standing(self):
        standing = self.income - (self.livingExpenses + self.debts + self.savings)

        if standing > 0:
            print("Your remaining budget for this period is: $" + str(standing))
        else:
            print("Your remaining budget is: $" + str(standing) + ". The 25%% savings percentage may be too high or your debts are piling up.")    


myBudget = newBudget(400,1500,500,230,90,6000, 4500)
myBudget.report()
myBudget.standing()