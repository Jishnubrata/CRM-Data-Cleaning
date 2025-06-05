# 🤖 CRM Data Cleaning & Validation Using AI

This project is a smart AI-powered CRM data cleaning and validation pipeline. It automates data quality improvements in customer relationship management (CRM) systems using Python, NLP, and fuzzy matching.

## 📌 Project Highlights

- 🔍 **Detects and removes duplicates** using fuzzy matching (like similar names)
- 📞 **Validates email addresses and phone numbers** using regex and basic logic
- 💬 **Analyzes customer sentiment** in CRM notes using TextBlob
- 🧹 **Cleans dirty or incomplete data** into structured, usable form
- 📊 **Generates visual insights** via Jupyter Notebook

> "Instead of just cleaning data manually, this project uses AI to enhance and automate CRM data validation."

---

## 🗂️ Project Structure (Must be structured before running the code)
```
crm-data-cleaning-project/
├── data/
│   ├── generate_sample_data.py         # Creates realistic CRM dataset
│   └── raw_crm_data.csv                # Auto-generated or already included sample data
├── cleaned_data/
│   └── cleaned_crm_data.csv            # Final cleaned data
├── scripts/
│   ├── clean_data.py                   # Cleans and validates raw CRM data
│   ├── detect_duplicates.py            # Identifies duplicate customer records
│   └── analyze_notes.py                # Analyzes sentiment in notes field
├── report.ipynb                        # Final report with charts & summaries
├── requirements.txt                    # All dependencies
└── README.md                           # This file
```

---

## 🚀 How to Run This Project

### 1. 📁 Unzip & Navigate
```bash
cd crm-data-cleaning-project
```

### 2. 🧪 Create a Virtual Environment
#### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
#### For Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. 🧠 Download NLP Models
```bash
python -m textblob.download_corpora
python -m spacy download en_core_web_sm
```

### 5. 📊 Launch the Notebook
```bash
jupyter notebook
```
Open `report.ipynb`, set kernel to `venv`, and run all cells.

> ✅ No need to re-run `generate_sample_data.py` or other scripts unless you want to test fresh data.

---

## 🔍 Sample Insights Generated
- Count of records by sentiment (Positive, Neutral, Negative)
- Count of invalid phone numbers & emails
- Count of duplicate entries detected

---

## 💡 Use Cases
- CRM software companies looking to improve customer data quality
- Data analysts cleaning sales/customer contact records
- AI projects integrating NLP and fuzzy logic into real-world pipelines

---

## 🙌 Credits
Built with ❤️ by B Tejaswini using:
- Python
- pandas, numpy
- fuzzywuzzy
- textblob
- spaCy
- seaborn & matplotlib

---

## 📬 Contact
Feel free to reach out on [B Tejaswini](https://www.linkedin.com/in/b-tejaswini-72b10a326)
 or check out more of my work on [GitHub - 09teju](https://github.com/09teju).

---

Let me know if you'd like to add screenshots, LinkedIn post text, or convert this into a blog format too!