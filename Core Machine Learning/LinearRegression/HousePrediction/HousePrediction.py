import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df=pd.read_csv(r"D:\AI ML\AI-ML\Core Machine Learning\LinearRegression\HousePrediction\HousePrice.csv")
X = df[["Area_sqft", "Bedrooms", "Bathrooms", "Age", "Distance_to_City_km"]]
y = df["Price_USD"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

predictions = model.predict(X_test)
print("Predictions:", predictions)
