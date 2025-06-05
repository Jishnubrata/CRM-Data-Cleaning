import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_crm_data(num_records=100):
    data = []
    for _ in range(num_records):
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        company = fake.company()
        job_title = fake.job()
        country = fake.country()
        notes = fake.sentence(nb_words=12)

        # Add some dirty data
        if random.random() < 0.1:
            email = email.replace("@", "")  # Invalid email
        if random.random() < 0.1:
            phone = ""  # Missing phone
        if random.random() < 0.05:
            name = name.lower()  # messy name

        data.append([name, email, phone, company, job_title, country, notes])

    df = pd.DataFrame(data, columns=["Name", "Email", "Phone", "Company", "Job Title", "Country", "Notes"])
    df.to_csv("data/raw_crm_data.csv", index=False)
    print("✅ Sample CRM data generated: data/raw_crm_data.csv")

if __name__ == "__main__":
    generate_crm_data()
