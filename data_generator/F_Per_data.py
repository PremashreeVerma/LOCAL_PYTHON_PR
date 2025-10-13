import random
import pandas as pd
from faker import Faker

fake = Faker('en_US')

validation_statuses = ["Active", "Inactive"]
genders = ["Male", "Female", "Other"]
prefixes = ["Mr.", "Ms.", "Mrs.", "Dr.", "Prof."]
suffixes = ["Jr.", "Sr.", "II", "III", "PhD", "MD"]

num_records = 1000  # You can adjust as needed

data = []

for _ in range(num_records):
    prefix = random.choice(prefixes)
    first_name = fake.first_name()
    middle_name = fake.first_name()
    last_name = fake.last_name()
    suffix = random.choice(suffixes)

    record = {
        # --- Name Info ---
        "Prefix": prefix,
        "FirstName": first_name,
        "MiddleName": middle_name,
        "LastName": last_name,
        "Suffix": suffix,
        "FullName": f"{prefix} {first_name} {middle_name} {last_name} {suffix}",
        "Gender": random.choice(genders),
        "DOB": fake.date_of_birth(minimum_age=18, maximum_age=60).strftime("%d-%m-%Y"),
        "ValidationStatus": random.choice(validation_statuses),

        # --- Email ---
        "Email.Type": random.choice(["Personal", "Work"]),
        "Email.Email": f"{first_name.lower()}.{last_name.lower()}@{fake.free_email_domain()}",

        # --- Phone ---
        "Phone.Type": random.choice(["Mobile", "Home", "Work"]),
        "Phone.Number": fake.phone_number(),

        # --- Address ---
        "Address.AddressInput": fake.street_address(),
        "Address.AddressLine1": fake.secondary_address(),
        "Address.AddressLine2": fake.street_name(),
        "Address.City": fake.city(),
        "Address.StateorProvince": fake.state(),
        "Address.Country": "United States",
        "Address.PostalCode": fake.postcode(),
        "Address.Zip5": fake.zipcode_in_state(),
        "Address.Zip4": fake.random_int(min=1000, max=9999),

        # --- Identifiers ---
        "Identifiers.Type": random.choice(["SSN", "DriverLicense", "Passport"]),
        "Identifiers.Value": fake.unique.bothify(text="??######"),

        # --- Education History ---
        "EducationHistory.InstitutionName": fake.company() + " University",
        "EducationHistory.Degree": random.choice(["B.Tech", "MBA", "PhD", "MSc", "BA"]),
        "EducationHistory.FieldofStudy": random.choice(["Computer Science", "Business", "Finance", "Engineering", "Biology"]),

        # --- Licenses ---
        "Licenses.Type": random.choice(["Medical", "Driving", "Professional"]),
        "Licenses.LicenseID": fake.unique.bothify(text="LIC#####"),

        # --- Certificates ---
        "Certificates.Type": random.choice(["ISO", "HIPAA", "PMP", "AWS", "Azure"]),
        "Certificates.CertID": fake.unique.bothify(text="CERT#####"),
    }

    data.append(record)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV file
output_path = "F_Per_data.csv"
df.to_csv(output_path, index=False, encoding="utf-8")

print(f"✅ CSV file '{output_path}' generated successfully with {num_records} records!")
