"""
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
            if rows[5] == 'y':
                sum = sum + float(rows[1])
        return sum
   
    def sumNotShared(self):
        sum = 0.0
        for rows in self.cashFlow:
            if rows[5] == 'n':
                sum = sum + float(rows[1])
        return sum

    def sumByCategory(self):
        print('Choose category:\n')
        # add index using enumerate()
        for cat in self.categories:
            print(cat)
        catChoice = input()
        # sum values
        sum = 0.0
        for rows in self.cashFlow:
            if rows[2] == catChoice:
                sum = sum + float(rows[1])
        return sum