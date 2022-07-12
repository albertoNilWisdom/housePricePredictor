import pandas as pd
import csv
import re


print("WELCOME----")
print("Enter first section of postcode e.g. GU46, or the full post code, with a space.")
print("-----------")
postcode = input()

if len(postcode) == 4 or len(postcode) == 3:
    regex = re.compile(postcode.upper()+' ...')
elif len(postcode) == 8 or len(postcode) == 7:
    regex = re.compile(postcode.upper())
else: 
    print("error, invalid postcode")


def search(regex):
    df = pd.DataFrame({'code':[],
                     'price':[], 
                     'date':[], 
                     'postcode':[], 
                     'type':[], 
                     'unk':[], 
                     'holding':[], 
                     'streetnumber':[],
                     'housename':[],
                     'road':[], 
                     'bor':[], 
                     'town':[], 
                     'loc':[], 
                     'county':[], 
                     'unk1':[], 
                     'unk2':[]})

    csvFile = '/home/ted/Documents/Programming/datasets/gov-paid-prices-housing/pp-complete.csv'
    results = 0

    with open(csvFile) as f:
        reader = csv.reader(f)
        for row in reader:
            print("Searching..." + str(results) + " result(s) found" ,end="\r")
            if re.match(regex, row[3]):
                #output that row to the dataframe (df)
                df.loc[len(df)] = row
                results = results + 1

    if results > 0:
        print(str(results) + ' total results, output file')
        df.to_csv(r'/home/ted/Documents/Programming/datasets/gov-paid-prices-housing/currentSearch.csv', index = False)
    else:
        print('there are no results.',end="\r")

search(regex)

print("WELCOME----")
print("would you like to predict the future? (y/N)")
print("-----------")
postcode = input()