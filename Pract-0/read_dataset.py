import pandas as pd
import matplotlib.pyplot as plt

test = pd.read_csv("test.csv")
test = test.head(10)

plt.plot(test['Date '], test['Close '])
plt.show()