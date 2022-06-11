"""
    budget.py calculates budget information
    The inputs to the budget script are a budget spreadsheet in csv format
    and a cash flow spreadsheet, also in csv format

    methods:
    - sum shared amounts
    - sum not shared amounts
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

class Budget:
    def readCash(input):
        with open(input, newline='',encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            data = list(reader)
        return data
   
    cashFlow = readCash('Cash-flow-2022-05-29-to-2022-07-02.csv')

    def sumNotShared(self):
        sum = 0.0
        for rows in Budget.cashFlow:
            if rows[4] == 'n':
                sum = sum + float(rows[1])
        return sum

b = Budget()

print('Sum of not shared = ' + str(b.sumNotShared()))