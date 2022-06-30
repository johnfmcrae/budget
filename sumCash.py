'''
    sumCash does the summing operation used in budget and prints
    the result to a csv without doing the diffs performed in budget.py
'''

import csv
import itertools
import os
from datetime import datetime

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

''' File paths '''
localFile = os.listdir()
csvList = []
for item in localFile:
    if item.endswith('.csv'):
        csvList.append(item)

print("Choose cash flow file:")
# choose a file
for idx, item in enumerate(csvList):
    print(str(idx +  1) + ". " + str(item))
cashFile = csvList[int(input()) - 1]

''' Read file '''
# read cash flow
with open(cashFile, newline='',encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    cashData = list(reader)

''' Read categories '''
cashPrimaryCat     = makeCategoryList(cashData,  2)
cashSecondaryCat   = makeCategoryList(cashData,  3)

''' Sum by category '''
cashPrimarySum     = sumByCategory(cashData,cashPrimaryCat,      2,1)
cashSecondarySum   = sumByCategory(cashData,cashSecondaryCat,    3,1)

''' print data to csv '''
# category, budget, spent, diff
outputCSVname = 'Cash-flow-sums-' + datetime.today().strftime('%Y-%m-%d') + '.csv'
with open(outputCSVname, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write primary categories
    writer.writerow(['Primary Categories'])
    writer.writerow(['Category','Sum'])
    writer.writerows(cashPrimarySum)
    writer.writerow('')
    writer.writerow(['Secondary Categories'])
    writer.writerow(['Category','Sum'])
    writer.writerows(cashSecondarySum)
print("Sums written to:" + outputCSVname)