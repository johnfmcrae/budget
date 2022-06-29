'''
    budget.py calculates budget information
    The inputs to the budget script are a budget spreadsheet in csv format
    and a cash flow spreadsheet, also in csv format

    Inputs:
    - budget csv
    - cash flow csv

    Output:
    - sum and diff csv
'''
import csv
import itertools

''' reused functions '''
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

def sumByCategory(data,categoryList,categoryCol,valueCol):
    categorySums = []
    for category in categoryList:
        sum = 0
        for rows in data:
            if rows[categoryCol] == category:
                sum = sum + float(rows[valueCol])
        categorySums.append([category,sum])
        #categorySums = categorySums + (category,sum)
    return categorySums

def diffCashBudget(cashSum,budgetSum):
    diffList = []
    extra = 0
    for entry in cashSum:
        # filter budget sum, casefold() ignores string case
        budgetEntry = list(filter(lambda e: e[0].casefold() == entry[0].casefold(), budgetSum))
        if budgetEntry == []:
            extra = extra + entry[1]
        else:
            diffList.append([entry[0],budgetEntry[0][1],entry[1],budgetEntry[0][1] - entry[1]])
    if extra != 0:
        diffList.append(['Unaccounted for',extra,'',''])
    return diffList

''' File paths '''
# file paths
# TO DO: make these a user input
budgetFile = 'Budget-2022-07.csv'
cashFile   = 'Cash-flow-2022-05-29-to-2022-07-02.csv'

''' Read files '''
# read budget
with open(budgetFile, newline='',encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    budgetData = list(reader)

# read cash flow
with open(cashFile, newline='',encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    cashData = list(reader)

''' Read categories '''
budgetPrimaryCat   = makeCategoryList(budgetData,1)
budgetSecondaryCat = makeCategoryList(budgetData,2)
cashPrimaryCat     = makeCategoryList(cashData,  2)
cashSecondaryCat   = makeCategoryList(cashData,  3)

''' Sum by category '''
budgetPrimarySum   = sumByCategory(budgetData,budgetPrimaryCat,  1,0)
budgetSecondarySum = sumByCategory(budgetData,budgetSecondaryCat,2,0)
cashPrimarySum     = sumByCategory(cashData,cashPrimaryCat,      2,1)
cashSecondarySum   = sumByCategory(cashData,cashSecondaryCat,    3,1)

''' diff by category '''        
diffPrimary   = diffCashBudget(cashPrimarySum,  budgetPrimarySum)
diffSecondary = diffCashBudget(cashSecondarySum,budgetSecondarySum)

''' print data to csv '''
# category, budget, spent, diff
outputCSVname = 'Budget-diff.csv'
with open(outputCSVname, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write primary categories
    writer.writerow(['Primary Categories'])
    writer.writerow(['Category','Budget','Spent','Diff'])
    writer.writerows(diffPrimary)
    writer.writerow('')
    writer.writerow(['Secondary Categories'])
    writer.writerow(['Category','Budget','Spent','Diff'])
    writer.writerows(diffSecondary)
