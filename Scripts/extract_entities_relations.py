import pandas as pd
import os

# Path to your CSV
csv_path = "D:/AIRS WebApp/data/raw_reports/final(2).csv"  # Change accordingly!
df = pd.read_csv(csv_path)

# Create output folder if not exists
os.makedirs("data/processed", exist_ok=True)

# --- Extract Unique Entities ---
families = df['Family'].dropna().unique().tolist()
sedd_addresses = df['SeddAddress'].dropna().unique().tolist()
exp_addresses = df['ExpAddress'].dropna().unique().tolist()
ip_addresses = df['IPaddress'].dropna().unique().tolist()
threats = df['Threats'].dropna().unique().tolist()

# Save entity lists
pd.DataFrame({'Family': families}).to_csv('data/processed/families.csv', index=False)
pd.DataFrame({'SeddAddress': sedd_addresses}).to_csv('data/processed/sedd_addresses.csv', index=False)
pd.DataFrame({'ExpAddress': exp_addresses}).to_csv('data/processed/exp_addresses.csv', index=False)
pd.DataFrame({'IPaddress': ip_addresses}).to_csv('data/processed/ip_addresses.csv', index=False)
pd.DataFrame({'Threats': threats}).to_csv('data/processed/threats.csv', index=False)

# --- Extract Relations ---
relations = []

for _, row in df.iterrows():
    # Relations between Family and addresses
    if pd.notna(row['Family']):
        if pd.notna(row['SeddAddress']):
            relations.append([row['Family'], 'has_SeddAddress', row['SeddAddress']])
        if pd.notna(row['ExpAddress']):
            relations.append([row['Family'], 'has_ExpAddress', row['ExpAddress']])
        if pd.notna(row['IPaddress']):
            relations.append([row['Family'], 'has_IPaddress', row['IPaddress']])
        if pd.notna(row['Threats']):
            relations.append([row['Family'], 'associated_with_Threat', row['Threats']])
    # Optionally add relations for ports, predictions, or other attributes if needed

# Save relations CSV
relations_df = pd.DataFrame(relations, columns=['Source', 'Relation', 'Target'])
relations_df.to_csv('data/processed/relations.csv', index=False)

print("Entities and relations extracted and saved in 'data/processed/' folder.")
