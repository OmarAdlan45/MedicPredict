import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nazikelgaddal098.",
            database="health_db"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def fetch_data(query):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result
        except mysql.connector.Error as err:
            print(f"Query Error: {err}")
        return []

# Corrected query with the proper joins
query = """
SELECT p.FirstName, p.LastName, SUM(b.total_amount) AS total_amount
FROM Patients p
JOIN Appointments a ON p.PatientID = a.PatientID
JOIN Billing b ON a.AppointmentID = b.AppointmentID
GROUP BY p.PatientID;
"""

# Fetch and process data
data = fetch_data(query)
df = pd.DataFrame(data)

# Debugging: Check DataFrame content
print("DataFrame Head:")
print(df.head())
print("\nDataFrame Info:")
print(df.info())

# Rename columns for clarity (optional)
df.rename(columns={'total_amount': 'amount'}, inplace=True)

# Ensure 'amount' is float and check for NaN values
if 'amount' in df.columns:
    df['amount'] = df['amount'].astype(float)
    print("\nChecking for NaN values in 'amount':")
    print(df['amount'].isna().sum())
else:
    print("Error: 'amount' column not found in DataFrame!")

# Plotting
if not df.empty and 'FirstName' in df.columns and 'amount' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="FirstName", y="amount", palette="viridis")  # Correct column name 'FirstName'
    plt.title("Billing Amounts by Patients")
    plt.xlabel("Patients' First Name", fontsize=12)
    plt.ylabel("Billing Amount ($)", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

else:
    print("Error: DataFrame is empty or missing required columns!")
