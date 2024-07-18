import mysql.connector
from mysql.connector import Error
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
import joblib


# Database connection
try:
    dataBase = mysql.connector.connect(
        host='localhost',
        user='root',
        password='af1234@#', # Password to log in to the MySQL server
        database="scienceandtechnology" 
    )

    if dataBase.is_connected():
        cursor = dataBase.cursor(buffered=True)
        query = "SELECT Profession, Earning, Reviews, Hour_Rate from freelancers;"
        cursor.execute(query)
        dataset = cursor.fetchall()

except Error as e:
    print(f"Error while connecting to MySQL: {e}")


if dataBase.is_connected():
    cursor.close()
    dataBase.close()
    print("MySQL connection is closed")

# Converting to Integer Values
updated_dataset = []
for count,i in enumerate(dataset):
    review = (dataset[count][2].split(' '))[0]
    hourRate = (dataset[count][3].split(' '))[0]
    hourRate = int(hourRate[1:])
    updated_dataset.append((dataset[count][0], dataset[count][1], int(review), hourRate))

# Converting to Pandas DataFrame
df = pd.DataFrame(updated_dataset, columns=["Profession","Rating","Reviews","HourRate"])

# One-hot encoding for Profession column
encoder = OneHotEncoder()
encoded_data = encoder.fit_transform(df[["Profession"]])
encoded_data_dense = encoded_data.toarray()
encoded_columns = encoder.get_feature_names_out(["Profession"])
encoded_df = pd.DataFrame(encoded_data_dense, columns=encoded_columns)
encoded_df = pd.concat([df.drop(columns=["Profession"]), encoded_df], axis=1)
# print(encoded_df)

# Separate features and target
X = encoded_df.drop(columns=["HourRate"])
y = encoded_df["HourRate"]
print(X.columns)
# Pipeline with model
pipeline = Pipeline([
    ("model", LinearRegression())
])

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the pipeline (including one-hot encoding) on training data
pipeline.fit(X_train, y_train)
# Predict on test set
y_pred = pipeline.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Save the model to a file
joblib.dump(pipeline, "model.pkl")
print("Model saved as model.pkl")