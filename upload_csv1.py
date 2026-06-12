import pandas as pd
import mysql.connector

# CSV Read
df =pd.read_csv("Social_Network_Ads.csv")

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pammysaini",   # apna password likho
    database="social_network"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    sql = """
    INSERT INTO social_network_ads
    (User_ID, Gender, Age, EstimatedSalary, Purchased)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        int(row["User ID"]),
        row["Gender"],
        int(row["Age"]),
        int(row["EstimatedSalary"]),
        int(row["Purchased"])
    )

    cursor.execute(sql, values)

conn.commit()

print("Data inserted successfully!")

cursor.close()
conn.close()
