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
    return categorySums

''' File paths '''
# file paths
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
budgetPrimarySum   = sumByCategory(budgetData,budgetPrimaryCat,1,0)
budgetSecondarySum = sumByCategory(budgetData,budgetSecondaryCat,2,0)
cashPrimarySum     = sumByCategory(cashData,cashPrimaryCat,2,1)
cashSecondarySum   = sumByCategory(cashData,cashSecondaryCat,3,1)

''' diff by category '''
# diff = budget sum - cash sum
# TO DO
# loop over cash sum then search budget sum to get diff
def diffCashBudget(cashSum,budgetSum):
    diffList = []
    extraEntry = False
    diff = 0
    extra = 0
    for idx, entry in enumerate(cashSum):
        # ensure we are not exceeding budget list length
        if idx < len(budgetSum):
            if entry[0] == budgetSum[idx][0]:
                diff = budgetSum[idx][1] - entry[1]
            diffList.append([entry[0],diff])
        else:
            extra = extra + entry[1]
            extraEntry = True
    if extraEntry == True:
        diffList.append(['Unaccounted for',extra])
    return diffList
        
diffPrimary   = diffCashBudget(cashPrimarySum,budgetPrimarySum)
diffSecondary = diffCashBudget(cashSecondarySum,budgetSecondarySum)

''' print data to csv '''

# for debug
pass
