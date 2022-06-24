"""
    Choose import file
    Save data to JSON
    Auto load data
    Load data from JSON

    Json data
    - import file names
"""
import csv
import os

# do a test read of the test text file
f = open('test1.txt', 'r')
content = f.read()
print(content)
f.close()

localFile = os.listdir()
csvList = []
txtList = []

# organize by file type
for item in localFile:
    if item.endswith('.csv'):
        csvList.append(item)
    elif item.endswith('txt'):
        txtList.append(item)

# print('-- csv list --')
# for i in csvList:
#     print(i)

# print('-- text list --')
# for i in txtList:
#     print(i)

# choose a file
for idx, item in enumerate(txtList):
    print(str(idx +  1) + ". " + str(item))

# prompt input