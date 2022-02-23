import pandas as pd

data = pd.read_csv(r"timtable.csv")

lv = 13
lh = 6
for i in range(1, lh):
    c = 0
    for j in range(1, lv):
        if data[i,j] != 'NaN':
            c += 1
        print(c,i)
print(data)