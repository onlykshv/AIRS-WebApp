import pandas as pd
import os

# Load your CSV file (adjust path and filename as needed)
csv_path = "data/raw_reports/final(2).csv"  # Point to your CSV

df = pd.read_csv(csv_path)

# --- Extract unique entities ---
entities = set()
for col in ["Ransomware", "Operator", "Victim", "Technique"]:
    entities.update(df[col].dropna().unique())

# Save entities
entities_df = pd.DataFrame(list(entities), columns=["Entity"])
os.makedirs("data/processed", exist_ok=True)
entities_df.to_csv("data/processed/entities.csv", index=False)

# --- Extract relations ---
relations = []
for _, row in df.iterrows():
    relations.append((row["Operator"], "uses", row["Ransomware"]))
    relations.append((row["Ransomware"], "targets", row["Victim"]))
    relations.append((row["Operator"], "executes", row["Technique"]))
    relations.append((row["Ransomware"], "attacked_on", row["Date"]))

relations_df = pd.DataFrame(relations, columns=["Source", "Relation", "Target"])
relations_df.to_csv("data/processed/relations.csv", index=False)
