import seaborn as sns
import matplotlib as plt
import pandas as pd


# Reading the data and exploring it
df = pd.read_csv("http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv")
df.head()
print(df.head())