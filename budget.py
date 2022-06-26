"""
    budget.py calculates budget information
    The inputs to the budget script are a budget spreadsheet in csv format
    and a cash flow spreadsheet, also in csv format

    methods:
    - sum shared amounts
    - sum not shared amounts
    - list categories
    - sum by category
    - sort by date
    - sort by amount
    - display category
    - display shared
    - display not shared
    - read cash flow data
    - read budget
"""
import csv
import enum
import itertools

"""
    The budget class reads the budget spreadsheet and
    and compares those values to those in the cash flow

    methods:
    - read budget csv
    - list primary categories
    - list secondary categories`
    - sum primary category goals
    - diff categories with cash flow
"""

def makeCategoryList(array,index):
    cats = []
    # use itertools to loop from from the second row onwards
    for rows in itertools.islice(array, 1, None):
        exists = False
        # check if category is in list
        for items in cats:
            if items == rows[index]:
                exists = True
        if not exists:
            cats.append(rows[index])
    return sorted(cats)

class Budget:
    def __init__(self) -> None:
        self.budgetList = self.readBudget('Budget-2022-07.csv')
        self.primaryList = makeCategoryList(self.budgetList,1)
        self.primaryList = makeCategoryList(self.budgetList,2)

    def readBudget(self, input):
        with open(input, newline='',encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            data = list(reader)
        return data

    def sumPrimaryAmounts(self, budget, category):
        sum = 0
        for rows in budget:
            if budget[1] == category:
                sum = sum + budget[0]
        return sum



class CashFlow:
    def __init__(self) -> None:
        self.cashFlow = self.readCash('Cash-flow-2022-05-29-to-2022-07-02.csv')
        self.primaryCategories = makeCategoryList(self.cashFlow,2)
        self.secondaryCategories = makeCategoryList(self.cashFlow,3)

    def readCash(self, input):
        with open(input, newline='',encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            data = list(reader)
        return data

    def sumShared(self):
        sum = 0.0
        for rows in self.cashFlow:
            if rows[5] == 'y':
                sum = sum + float(rows[1])
        return sum
   
    def sumNotShared(self):
        sum = 0.0
        for rows in self.cashFlow:
            if rows[5] == 'n':
                sum = sum + float(rows[1])
        return sum

    def sumByCategory(self,catList,rowIdx):
        print('Choose category:\n')
        # add index using enumerate()
        for idx, cat in enumerate(catList):
            print(str(idx + 1) + ". " + cat, end = "\t")
        print("\n")
        catChoice = catList(int(input()) - 1)
        # sum values
        sum = 0.0
        for rows in self.cashFlow:
            if rows[rowIdx] == catChoice:
                sum = sum + float(rows[1])
        return catChoice, sum

        
b = CashFlow()

class userInterface():
    def __init__(self,Budget,CashFlow) -> None:
        self.budget = Budget
        self.cash   = CashFlow

    def homePage():
        print('\n=================== BUDGET CALCULATOR ===================\n\n' + 
            '1. Choose files   2. Display files   3. Show sums  0. Exit')
        menuChoice = input()
        if int(menuChoice) == 0:
            return False
        elif int(menuChoice) == 3:
            pass # sumPage
        else:
            return False

    def sumPage():
        print('\n------------------------ Show Sums ------------------------\n\n' + 
            '1. Sum total cash flow  2. Sum by primary category  3. Sum by secondary category')
        menuChoice = input()
        if int(menuChoice) == 1:
            pass
        
        


runUI = True
while runUI == True:
    # print('-- Budget app --\n' + 
    #     '1. Sum shared  2. Sum not shared   3. Sum by category  0. Exit')
    # menuChoice = input()
    # if int(menuChoice) == 1:
    #     print('Sum of shared = ' + str(b.sumShared()) + '\n')
    # if int(menuChoice) == 2:
    #     print('Sum of not shared = ' + str(b.sumNotShared()) + '\n')
    # if int(menuChoice) == 3:
    #     catSum = b.sumByCategory()
    #     print('Sum = ' + str(catSum) + '\n')
    # if int(menuChoice) == 0:
    #     break

    runUI = userInterface()