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
import itertools

"""
    The budget class reads the budget spreadsheet and
    and compares those values to those in the cash flow

    methods:
    - read budget csv
    - list primary categories
    - list secondary categories
    - sum primary category goals
    - diff categories with cash flow
"""
class Budget:
    pass


class CashFlow:
    def __init__(self) -> None:
        self.cashFlow = self.readCash('Cash-flow-2022-05-29-to-2022-07-02.csv')
        self.categories = self.makeCategoryList(self.cashFlow)

    def readCash(self, input):
        with open(input, newline='',encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            data = list(reader)
        return data
   
    #cashFlow = readCash('Cash-flow-2022-05-29-to-2022-07-02.csv')

    def makeCategoryList(self, cashFlow):
        cats = []
        # use itertools to loop from from the second row onwards
        for rows in itertools.islice(cashFlow, 1, None):
            exists = False
            # check if category is in list
            for items in cats:
                if items == rows[2]:
                    exists = True
            if not exists:
                cats.append(rows[2])
        return sorted(cats)

    #categories = makeCategoryList(cashFlow)

    def sumShared(self):
        sum = 0.0
        for rows in self.cashFlow:
            if rows[4] == 'y':
                sum = sum + float(rows[1])
        return sum
   
    def sumNotShared(self):
        sum = 0.0
        for rows in self.cashFlow:
            if rows[4] == 'n':
                sum = sum + float(rows[1])
        return sum

    def sumByCategory(self):
        print('Choose category:\n')
        for cat in self.categories:
            print(cat)
        catChoice = input()
        # sum values
        sum = 0.0
        for rows in self.cashFlow:
            if rows[2] == catChoice:
                sum = sum + float(rows[1])
        return sum
        
b = CashFlow()

while True:
    print('-- Budget app --\n' + 
        '1. Sum shared  2. Sum not shared   3. Sum by category  0. Exit')
    menuChoice = input()
    if int(menuChoice) == 1:
        print('Sum of shared = ' + str(b.sumShared()) + '\n')
    if int(menuChoice) == 2:
        print('Sum of not shared = ' + str(b.sumNotShared()) + '\n')
    if int(menuChoice) == 3:
        catSum = b.sumByCategory()
        print('Sum = ' + str(catSum) + '\n')
    if int(menuChoice) == 0:
        break