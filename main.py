import pandas as pd

# Read raw data
df = pd.read_csv("data/customers_raw.csv")

print("RAW DATA")
print(df)

# 1. Remove duplicate rows
df = df.drop_duplicates()

# 2. Standardize city names
df["city"] = df["city"].str.strip().str.title()

# 3. Handle missing age
df["age"] = df["age"].fillna(df["age"].median())

# 4. Handle missing email
df["email"] = df["email"].fillna("unknown")

# 5. Save cleaned data
df.to_csv("data/customers_clean.csv", index=False)

print("\nCLEANED DATA")
print(df)

print("\nMissing values:")
print(df.isnull().sum())
