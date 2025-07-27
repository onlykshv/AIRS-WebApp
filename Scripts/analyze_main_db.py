import pandas as pd

csv_path = "D:/AIRS WebApp/data/raw_reports/final(2).csv"  # set to your downloaded file path
df = pd.read_csv(csv_path)

print("Columns in CSV:")
print(df.columns.tolist())
print("\nSample rows:")
print(df.head(3).to_string())
