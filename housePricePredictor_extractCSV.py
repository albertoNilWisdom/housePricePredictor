import pandas as pd
import csv
import re
from prophet import Prophet
#http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-complete.csv
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

    csvFile = '/home/ted/Documents/programming/datasets/gov-paid-prices-housing/pp-complete.csv'
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
        df.rename(columns={'date':'ds','price':'y'}, inplace = True)
        df['ds'] = pd.to_datetime(df['ds']).dt.date
        df=df[['ds','y']]
        df.to_csv(r'/home/ted/Documents/programming/datasets/gov-paid-prices-housing/currentSearch.csv', index = False)
    else:
        print('there are no results.',end="\r")

def prediction():
    df = pd.read_csv('/home/ted/Documents/programming/datasets/gov-paid-prices-housing/currentSearch.csv')
    df.head
    m = Prophet(seasonality_mode ='multiplicative',mcmc_samples=300).fit(df, show_progress=True)
    future = m.make_future_dataframe(periods=365)
    fcst = m.predict(future)
    fig = m.plot(fcst)
    fcst.to_csv('predict_output.csv')

search(regex)
prediction()

