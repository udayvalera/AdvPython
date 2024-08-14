import pandas as pd

test = pd.read_csv('test.csv')
test = test.head(10)

print(test.head())