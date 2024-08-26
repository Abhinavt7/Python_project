import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
dataframe = pd.read_csv("Restaurant_Data.csv")
print(dataframe.head())

# Function to handle the rate conversion
def handleRate(value):
    value = str(value).split('/')
    try:
        value = float(value[0])
    except ValueError:
        value = np.nan  # Handle any non-numeric or missing ratings
    return value

# Apply the rate handling function
dataframe['rate'] = dataframe['rate'].apply(handleRate)
print(dataframe.head())

# Display dataset information
dataframe.info()

# Plotting the count of restaurant types
type_counts = dataframe['listed_in(type)'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(type_counts.index, type_counts.values, color='skyblue')
plt.xlabel("Type of Restaurant", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.title("Count of Restaurant Types", fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.show()

# Grouping by type and summing votes
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()

# Plotting the votes by restaurant type
plt.figure(figsize=(10, 6))
plt.plot(grouped_data.index, grouped_data.values, color="green", marker="o")
plt.xlabel("Type of Restaurant", color="red", fontsize=14)
plt.ylabel("Votes", color="red", fontsize=14)
plt.title("Total Votes by Restaurant Type", fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.show()

# Finding and printing the restaurant(s) with the maximum votes
max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']
print("Restaurant(s) with the maximum votes:")
print(restaurant_with_max_votes)

# Plotting the count of online orders
online_order_counts = dataframe['online_order'].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(online_order_counts.index, online_order_counts.values, color='lightcoral')
plt.xlabel("Online Order", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.title("Count of Online Orders", fontsize=16)
plt.show()

# Histogram of ratings
plt.figure(figsize=(8, 6))
plt.hist(dataframe['rate'].dropna(), bins=5, color='purple', edgecolor='black')
plt.xlabel("Rating", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.title("Ratings Distribution", fontsize=16)
plt.show()

# Countplot for approximate cost for two people
approx_cost_counts = dataframe['approx_cost(for two people)'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(approx_cost_counts.index, approx_cost_counts.values, color='orange')
plt.xlabel("Approx Cost for Two PeopleA", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.title("Count of Approximate Cost for Two People", fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.show()

# Boxplot for online order vs rate
online_order_unique = dataframe['online_order'].unique()
rate_values = [dataframe[dataframe['online_order'] == order]['rate'].dropna() for order in online_order_unique]

plt.figure(figsize=(8, 6))
plt.boxplot(rate_values, labels=online_order_unique)
plt.xlabel("Online Order", fontsize=14)
plt.ylabel("Rating", fontsize=14)
plt.title("Boxplot of Ratings by Online Order", fontsize=16)
plt.show()

# Creating a pivot table for heatmap visualization
pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)

# Heatmap visualization
plt.figure(figsize=(10, 8))
plt.imshow(pivot_table, cmap="YlGnBu", aspect='auto')
plt.colorbar(label="Count")
plt.xticks(ticks=np.arange(len(pivot_table.columns)), labels=pivot_table.columns, rotation=45, ha='right')
plt.yticks(ticks=np.arange(len(pivot_table.index)), labels=pivot_table.index)
plt.xlabel("Online Order", fontsize=14)
plt.ylabel("Listed In (Type)", fontsize=14)
plt.title("Heatmap of Restaurant Types by Online Order", fontsize=16)
plt.show()
