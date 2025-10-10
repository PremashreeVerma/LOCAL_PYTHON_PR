import pandas as pd
import random
from faker import Faker

fake = Faker()

# Account Type ↔ Code Mapping
account_type_map = {
    "Checking": "AT001",
    "Savings": "AT002",
    "CD (Certificate of Deposit)": "AT003",
    "Brokerage / Securities": "AT004",
    "Business Checking": "AT005",
    "Loan": "AT006",
    "Money Market": "AT007",
    "Custodial Account": "AT008",
    "Trust Account": "AT009",
    "Credit Card Account": "AT010",
    "Mortgage Loan": "AT011"
}

# Account Status List
account_statuses = ["Active", "Closed", "Matured", "Inactive", "Pending"]
currencies = ["USD", "EUR", "INR", "GBP", "CAD"]
interest_types = ["Fixed", "Variable", "N/A"]
balance_types = [
    "Current Balance", "Available Balance", "Final Balance",
    "Market Value", "Book Value", "Principal Owed"
]

records = []

# Keep track of used account numbers
used_account_numbers = set()

def generate_unique_account_number():
    while True:
        acc_num = random.randint(1000000000, 9999999999)
        if acc_num not in used_account_numbers:
            used_account_numbers.add(acc_num)
            return str(acc_num)

# Generate 1000 records
for i in range(1, 1001):
    acc_type = random.choice(list(account_type_map.keys()))
    acc_code = account_type_map[acc_type]
    acc_status = random.choice(account_statuses)
    
    open_date_obj = fake.date_between(start_date="-20y", end_date="-2y")
    open_date = open_date_obj.strftime("%d-%m-%Y")
    
    close_date = ""
    if acc_status == "Closed":
        close_date_obj = fake.date_between(start_date=open_date_obj, end_date="today")
        close_date = close_date_obj.strftime("%d-%m-%Y")
    
    city = fake.city()
    state = fake.state_abbr()
    country = "USA"
    postal_code = f"{random.randint(10000,99999)}-{random.randint(1000,9999)}"
    zip5, zip4 = postal_code.split("-")

    record = {
        "BankID": f"BANK{random.randint(1000, 9999)}",  # can repeat
        "BankName": fake.company(),                       # can repeat
        "AccountName": fake.name(),
        "AccountNumber": generate_unique_account_number(),  # unique
        "AccountType": acc_type,
        "AccountTypeCode": acc_code,
        "AccountStatus": acc_status,
        "OpenDate": open_date,
        "CloseDate": close_date,
        "BaseCurrency": "USD",
        "SettlementCurrency": random.choice(currencies),
        "InterestRate": round(random.uniform(0.1, 8.0), 2),
        "InterestRateType": random.choice(interest_types),
        "ElectronicStatementDelivery": random.choice(["TRUE", "FALSE"]),
        "Latest StatusChangeDate": fake.date_between(start_date="-5y", end_date="today").strftime("%d-%m-%Y"),
        "Latest FromStatus": random.choice(account_statuses),
        "Latest ToStatus": acc_status,
        "BalanceType (Current)": random.choice(balance_types),
        "AsOfDate (Current)": "09-10-2025",
        "BalanceAmount (Current)": round(random.uniform(1000.0, 200000.0), 2),
        "BalanceCurrency (Current)": "USD",
        "Address Input": f"{fake.street_address()}, {city}, {state} {postal_code}",
        "Address Line 1": fake.street_address(),
        "Address Line 2": random.choice(["", fake.secondary_address()]),
        "City": city,
        "State or Province": state,
        "Country": country,
        "Postal Code": postal_code,
        "Zip5": zip5,
        "Zip4": zip4
    }

    records.append(record)

# Save to CSV in current folder
df = pd.DataFrame(records)
df.to_csv("new_generated_account_records_1k.csv", index=False)
print("✅ CSV file 'generated_account_records_1k.csv' created successfully!")
