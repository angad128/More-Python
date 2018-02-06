import pandas as pd
import quandl

mydata = quandl.get('WIKI/GOOGL')
#print(mydata.head())

mydata = mydata[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
#print(mydata)

mydata['HL_PCT'] = (mydata['Adj. High']-mydata['Adj. Close']) / mydata['Adj. Close'] * 100.0
#print(mydata['HL_PCT'])
mydata['PCT_change'] = (mydata['Adj. Close']-mydata['Adj. Open']) / mydata['Adj. Open'] * 100.0
#print(mydata['PCT_change'])

mydata = mydata[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
print(mydata)