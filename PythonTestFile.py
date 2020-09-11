import pandas as pd
df = pd.read_csv('.\Sales_Data\Sales_January_2019.csv')
for df in pd.read_csv('.\Sales_Data\Sales_January_2019.csv', chunksize=5):
    #print('CHUNK DF')
    print(df)

new_df = pd.DataFrame(columns = df.columns)
new_df = pd.DataFrame(columns = df.columns)

for df in pd.read_csv('.\Sales_Data\Sales_January_2019.csv', chunksize=5):
    results = df.groupby(df['Product']).sum()
    new_df = pd.concat([results, new_df], sort = True)

print(new_df)