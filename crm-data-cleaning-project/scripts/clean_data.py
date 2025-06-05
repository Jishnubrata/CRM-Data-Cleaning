import pandas as pd
import re
import os

# Load raw CRM data
df = pd.read_csv('data/raw_crm_data.csv')

# Strip extra spaces
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Capitalize name and company properly
df['Name'] = df['Name'].apply(lambda x: x.title() if isinstance(x, str) else x)
df['Company'] = df['Company'].apply(lambda x: x.title() if isinstance(x, str) else x)

# Validate email using regex
def is_valid_email(email):
    if not isinstance(email, str):
        return False
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(regex, email))

df['Valid Email'] = df['Email'].apply(is_valid_email)

# Validate phone (only digits, 10+ length)
def is_valid_phone(phone):
    if not isinstance(phone, str):
        return False
    digits = re.sub(r'\D', '', phone)
    return len(digits) >= 10

df['Valid Phone'] = df['Phone'].apply(is_valid_phone)

# Drop invalid rows (optional)
df_cleaned = df[df['Valid Email'] & df['Valid Phone']].copy()

# Drop helper columns
df_cleaned.drop(columns=['Valid Email', 'Valid Phone'], inplace=True)

# Save cleaned data
os.makedirs('cleaned_data', exist_ok=True)
df_cleaned.to_csv('cleaned_data/cleaned_crm_data.csv', index=False)

print("✅ Data cleaned and saved to cleaned_data/cleaned_crm_data.csv")
