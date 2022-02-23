import pandas as pd
# There is a excel file, which contains the dates and slots in the respective order. I'm using pandas to extract that value and work with it.
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
