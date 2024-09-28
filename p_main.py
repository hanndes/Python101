import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('Housing.csv')
plt.figure()
plt.hist(df['area'], bins=20, color='blue', edgecolor='white')
plt.title('Area Distribution')
plt.xlabel('Area')
plt.ylabel('Frequency')
plt.show()

plt.figure()
plt.hist(df['bedrooms'], bins=20, color='green', edgecolor='white')
plt.title('Bedrooms Distribution')
plt.xlabel('Bedrooms')
plt.ylabel('Frequency')
plt.show()

plt.figure()
plt.hist(df['stories'], bins=20, color='red', edgecolor='white')
plt.title('Stories Distribution')
plt.xlabel('Stories')
plt.ylabel('Frequency')
plt.show()

avg_price_by_bathrooms = df.groupby('bathrooms')['price'].mean()

plt.figure()
avg_price_by_bathrooms.plot(kind='bar', color='purple')
plt.title('Average Price by Number of Bathrooms')
plt.xlabel('Number of Bathrooms')
plt.ylabel('Average Price')
plt.show()

avg_price_by_furnishing = df.groupby('furnishingstatus')['price'].mean()

plt.figure()
avg_price_by_furnishing.plot(kind='bar', color='orange')
plt.title('Average Price by Furnishing Status')
plt.xlabel('Furnishing Status')
plt.ylabel('Average Price')
plt.show()





