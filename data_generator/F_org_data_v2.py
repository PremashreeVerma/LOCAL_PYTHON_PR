import pandas as pd
import random
import re
from faker import Faker

fake = Faker("en_US")  # US locale for consistent data

# Reference lists
company_types = ["Private", "Public", "LLC", "Non-Profit", "Government", "Partnership"]
validation_statuses = ["Validated", "Pending", "Rejected", "In Review", "Approved"]
phone_types = ["Mobile", "Office", "Home", "Fax"]
email_types = ["Business", "Personal", "Support", "HR", "Sales"]
identifier_types = ["PAN", "GST", "EIN", "TIN", "DUNS", "LEI"]
status_list = ["Active", "Inactive", "Pending", "Expired"]

# Convert company name → domain
def company_to_domain(name):
    domain = re.sub(r"[^a-zA-Z0-9]", "", name.split()[0]).lower()
    return f"{domain}.com"

# Generate Address (expanded)
def generate_address():
    zip5 = random.randint(10000, 99999)
    zip4 = random.randint(1000, 9999)
    postal_code = f"{zip5}-{zip4}"
    addr_line1 = fake.street_address()
    addr_line2 = random.choice(["", fake.secondary_address()])
    city = fake.city()
    state = fake.state_abbr()
    country = "USA"
    address_input = f"{addr_line1}, {addr_line2 + ', ' if addr_line2 else ''}{city}, {state} {postal_code}"
    return {
        "AddressInput": address_input,
        "AddressLine1": addr_line1,
        "AddressLine2": addr_line2,
        "City": city,
        "State": state,
        "Country": country,
        "PostalCode": postal_code,
        "Zip5": str(zip5),
        "Zip4": str(zip4)
    }

# Generate US Phone
def generate_us_phone():
    area_code = random.randint(201, 999)
    exchange = random.randint(200, 999)
    subscriber = random.randint(1000, 9999)
    return f"({area_code}) {exchange}-{subscriber}"

# Generate Email
def generate_email(company_name):
    first_name = fake.first_name().lower()
    last_name = fake.last_name().lower()
    domain = company_to_domain(company_name)
    return f"{first_name}.{last_name}@{domain}"


# Generate Identifiers
def generate_identifiers():
    return {
        "Type": random.choice(identifier_types),
        "Value": fake.bothify(text="??#####"),
        "Status": random.choice(status_list)
    }

# Generate data
num_records = 1000
records = []

for _ in range(num_records):
    company_name = fake.company()
    address = generate_address()
    email_val = generate_email(company_name)
    identifiers = generate_identifiers()

    record = {
        "Name": company_name,
        "CompanyType": random.choice(company_types),
        "ValidationStatus": random.choice(validation_statuses),

        # Phone
        "Phone_Type": random.choice(phone_types),
        "Phone_Number": generate_us_phone(),

        # Email
        "Email_Type": random.choice(email_types),
        "Email_Value": email_val,
        "Email_Active": random.choice([True, False]),
        "TaxID": f"TAX{random.randint(10000,99999)}",

        # Identifiers
        "Identifiers_Type": identifiers["Type"],
        "Identifiers_Value": identifiers["Value"],
        "Identifiers_Status": identifiers["Status"],

        # Address (expanded)
        "Address Input": address["AddressInput"],
        "Address Line 1": address["AddressLine1"],
        "Address Line 2": address["AddressLine2"],
        "City": address["City"],
        "State or Province": address["State"],
        "Country": address["Country"],
        "Postal Code": address["PostalCode"],
        "Zip5": address["Zip5"],
        "Zip4": address["Zip4"]
    }

    records.append(record)

# Save to CSV
df = pd.DataFrame(records)
df.to_csv("F_org_data_v2.csv", index=False)
print("✅ File 'company_entity_data_v2.csv' created successfully with full address breakdown and US-format contact info.")
