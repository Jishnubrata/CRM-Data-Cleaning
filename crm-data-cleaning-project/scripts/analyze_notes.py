import pandas as pd
from textblob import TextBlob
import os

# Load cleaned CRM data
df = pd.read_csv('cleaned_data/cleaned_crm_data.csv')

# Analyze sentiment of each note
def get_sentiment(text):
    if not isinstance(text, str) or text.strip() == "":
        return "Neutral"
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

df['Sentiment'] = df['Notes'].apply(get_sentiment)

# Save updated file with sentiments
os.makedirs('cleaned_data', exist_ok=True)
df.to_csv('cleaned_data/cleaned_crm_data.csv', index=False)

print("✅ Sentiment analysis done. Updated file saved to cleaned_data/cleaned_crm_data.csv")
