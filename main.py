import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# read data frame
df = pd.read_csv('Border_Crossing_Entry_Data.csv')
df.head()

# Data Overview
print(df.info())
print(df.Measure.unique())
print(df.Border.unique())

# check for nan values
print(df.isna().sum())

# change type of Date column from object to time
df['Date'] = pd.to_datetime(df['Date']).dt.date

# filter dataframe to only Passengers (no Vehicles)
df2 = df[df['Measure'].isin(['Personal Vehicle Passengers','Bus Passengers','Pedestrians','Train Passengers'])]
print(df2.head())

# show Passenger Count by Border
df_passengers_total = df2.groupby(['Border']).agg({'Value': 'sum'})
print(df_passengers_total)

# Plot % of Passenger Count by Border
df_passengers_total.plot(kind='pie', subplots=True, legend=False, autopct='%.2f%%', figsize=(7,7), title= "Comparison Count of Border Crossings", fontsize=12)
plt.show()


# Show Passenger Count by Measure of Crossing and by Border
df_measure = df2.groupby(['Border','Measure']).agg({'Value':'sum'})
print(df_measure)


# Plot Passenger Count by Measure of Crossing and by Border
plt.figure(figsize=(12,7))
sns.barplot(data=df2, x="Border", y="Value", hue="Measure")
plt.box(False)
plt.title("Measures of Border Crossing - by Border", fontweight='bold', fontsize=15)
plt.show()


# Plotting all Crossings by Measure and Border
plt.figure(figsize=(15,7))
plt.box(False)
sns.barplot(data=df, x='Border', y='Value', hue='Measure')
plt.title("Crossings by all Measures and by Border")
plt.show()

# plotting Border Crossings throughout Time - Passengers + Vehicles
plt.figure(figsize=(15,7))
sns.lineplot(data=df, x='Date',y='Value', hue='Border')
plt.box(False)
plt.title('Border Crossings throughout Time - Passengers & Vehicles', fontweight='bold', fontsize=15)
plt.show()

# plotting Border Crossings throughout Time - only Passengers
plt.figure(figsize=(15,7))
sns.lineplot(data=df2, x='Date',y='Value', hue='Border')
plt.box(False)
plt.title('Border Crossings throughout Time - only Passengers', fontweight='bold')
plt.show()


# Plotting Crossings throughout Time by Measure Type
plt.figure(figsize=(20,10))
sns.lineplot(data=df, x='Date', y='Value',hue='Measure', palette='bright')
plt.box(False)
plt.show()


