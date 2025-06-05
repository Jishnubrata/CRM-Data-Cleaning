import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Load cleaned data
df = pd.read_csv('cleaned_data/cleaned_crm_data.csv')

# Function to find similar names using fuzzy matching
def find_duplicates(df, threshold=90):
    duplicates = []
    names = df['Name'].tolist()
    seen = set()

    for i, name in enumerate(names):
        if name in seen:
            continue
        matches = process.extract(name, names, scorer=fuzz.token_sort_ratio)
        similar = [match for match in matches if match[1] >= threshold and match[0] != name]
        for match in similar:
            match_index = df[df['Name'] == match[0]].index.tolist()
            for idx in match_index:
                duplicates.append((i, idx, name, match[0], match[1]))
        seen.add(name)

    return duplicates

dupes = find_duplicates(df)

# Display found duplicates
print(f"\n🔁 Found {len(dupes)} potential duplicates (based on name similarity ≥ 90):\n")
for original_idx, dup_idx, name1, name2, score in dupes:
    print(f"  - '{name1}' ⟷ '{name2}' (Score: {score})")

