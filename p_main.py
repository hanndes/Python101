import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('Housing.csv')
plt.figure()
plt.hist(df['area'], weights=df['price'],bins=20, color='pink', edgecolor='white')
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Ev Fiyatlarının Area ile İlişkisi')
plt.show()


plt.figure()
plt.hist(df['bedrooms'], weights=df['price'], bins=10, color='lightblue', edgecolor='white')
plt.xlabel('Bedrooms')
plt.ylabel('Total Price')
plt.title('Ev Fiyatlarının Bedrooms ile İlişkisi')
plt.show()

plt.figure()
plt.hist(df['stories'], weights=df['price'], bins=5, color='lightgreen', edgecolor='white')
plt.xlabel('Stories')
plt.ylabel('Total Price')
plt.title('Ev Fiyatlarının Stories ile İlişkisi')
plt.show()

avg_price_by_bathrooms = df.groupby('bathrooms')['price'].mean()

plt.figure()
avg_price_by_bathrooms.plot(kind='bar', color='purple')
plt.title('Banyo Ortalama Fiyatı')
plt.xlabel('Number of Bathrooms')
plt.ylabel('Average Price')
plt.show()

avg_price_by_furnishing = df.groupby('furnishingstatus')['price'].mean()

plt.figure()
avg_price_by_furnishing.plot(kind='bar', color='orange')
plt.title('Mobilya Durumuna Göre Ortalama Fiyat')
plt.xlabel('Furnishing Status')
plt.ylabel('Average Price')
plt.show()





