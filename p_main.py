import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Housing.csv')

plt.figure()
plt.hist(df['area'], weights=df['price'], bins=20, color='pink', edgecolor='white')
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Relationship Between House Prices and Area')
plt.show()

plt.figure()
plt.hist(df['bedrooms'], weights=df['price'], bins=10, color='lightblue', edgecolor='white')
plt.xlabel('Bedrooms')
plt.ylabel('Total Price')
plt.title('Relationship Between House Prices and Number of Bedrooms')
plt.show()

plt.figure()
plt.hist(df['stories'], weights=df['price'], bins=5, color='lightgreen', edgecolor='white')
plt.xlabel('Stories')
plt.ylabel('Total Price')
plt.title('Relationship Between House Prices and Number of Stories')
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
