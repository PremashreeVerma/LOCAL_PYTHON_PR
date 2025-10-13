import pandas as pd
import random
from faker import Faker

fake = Faker()

# Predefined reference values
company_types = ["Private", "Public", "LLC", "Non-Profit", "Government", "Partnership"]
validation_statuses = ["Validated", "Pending", "Rejected", "In Review", "Approved"]
phone_types = ["Mobile", "Office", "Home", "Fax"]
email_types = ["Business", "Personal", "Support", "HR", "Sales"]
identifier_types = ["PAN", "GST", "EIN", "TIN", "DUNS", "LEI"]
status_list = ["Active", "Inactive"]

# Function to create nested Address (Reference)
def generate_address():
    return {
        "AddressLine1": fake.street_address(),
        "AddressLine2": random.choice(["", fake.secondary_address()]),
        "City": fake.city(),
        "State": fake.state_abbr(),
        "Country": "USA",
        "PostalCode": f"{random.randint(10000,99999)}-{random.randint(1000,9999)}"
    }

# Function to create nested Phone
def generate_phone():
    return {
        "Type": random.choice(phone_types),
        "Number": fake.phone_number()
    }

# Function to create nested Email
def generate_email():
    return {
        "Type": random.choice(email_types),
        "Value": fake.email(),
        "Active": random.choice([True, False]),
        "TaxID": f"TAX{random.randint(10000,99999)}"
    }

# Function to create nested Identifiers
def generate_identifiers():
    return {
        "Type": random.choice(identifier_types),
        "Value": fake.bothify(text="??#####"),
        "Status": random.choice(status_list)
    }

# Number of records
num_records = 1000

records = []
for _ in range(num_records):
    address = generate_address()
    phone = generate_phone()
    email = generate_email()
    identifiers = generate_identifiers()

    record = {
        "Name": fake.company(),
        "CompanyType": random.choice(company_types),
        "Address": f"{address['AddressLine1']}, {address['City']}, {address['State']}, {address['Country']} - {address['PostalCode']}",
        "Phone_Type": phone["Type"],
        "Phone_Number": phone["Number"],
        "ValidationStatus": random.choice(validation_statuses),
        "Email_Type": email["Type"],
        "Email_Value": email["Value"],
        "Email_Active": email["Active"],
        "TaxID": email["TaxID"],
        "Identifiers_Type": identifiers["Type"],
        "Identifiers_Value": identifiers["Value"],
        "Identifiers_Status": identifiers["Status"]
    }

    records.append(record)

# Save to CSV
df = pd.DataFrame(records)
df.to_csv("organization_data.csv", index=False)
print("✅ File 'company_entity_data.csv' created successfully with 1000 synthetic company records.")
