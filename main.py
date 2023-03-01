#Budgeting tool that will require all monthly bills statically input
#Pay schedule frequency will be necessary to allocate funds
#End result will be amount to leave in account for bills, amount to transfer for savings/debts, and the remaining balance for miscellaneous


class newBudget:
    def __init__(self, utilities, housing, autoLoan, insurances, studentLoans, debts, other, savings):
        self.utilities = utilities
        self.housing = housing
        self.autoLoan = autoLoan
        self.insurances = insurances
        self.studentLoans = studentLoans
        self.debts = debts
        self.other = other
        self.savings = savings
        self.total = self.utilities + self.housing + self.autoLoan + self.insurances + self.studentLoans + self.debts

    def staticMath(self):

        print("Total of all primary static bills is: " + str(self.total))


myBudget = newBudget(400,500,11,1300,90,15,450,600)
myBudget.staticMath()    