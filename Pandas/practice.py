import pandas as pd

df = pd.read_csv("nba.csv")

print("Dataset")
print(df.head())

print(40*'-')

first = df["Name"]
print("\nSingle Column selected from Dataset")
print(first.head(5))

print(40*'-')

first = df[["Age", "College", "Salary"]]
print("\nMultiple Columns selected from Dataset")
print(first.head(5))

print(40*'-')

all_rows_specific_columns = df.loc[:, ["Team", "Position", "Salary"]]
print(all_rows_specific_columns)

print(40*'-')


print(df.tail())

print(40*'-')

value = df.loc[df["Name"] == "Avery Bradley", "Age"]
print(value)

print(40*'-')

value = df.loc[df["Name"] == "Avery Bradley", "Age"]
print(value.iloc[0])

print(40*'-')


result = df.query("Age > 25 and College == 'Duke'")
print(result)


