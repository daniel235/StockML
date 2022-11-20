from numpy import genfromtxt
import pandas as pd
#import data
#stockprices = genfromtxt('stock.csv', delimiter=',')
stockprices = pd.read_csv('stock.csv')
print(stockprices)

#create train and test data
test_ratio = 0.2
training_ratio = 1 - test_ratio

train_size = int(training_ratio * len(stockprices))
test_size = int(test_ratio * len(stockprices))
print("train size: ", str(train_size))
print("test size: ", str(test_size))

train = stockprices[:train_size]
test = stockprices[train_size:]

print(train)
