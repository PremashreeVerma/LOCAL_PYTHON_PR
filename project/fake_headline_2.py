import random

def generate_fake_headline():
    subjects = [
        "AI", "Python", "Reltio MDM", "Data Engineers", "SpaceX", "Politicians", "Startups", "Students"
    ]
    verbs = [
        "discover", "launch", "criticize", "celebrate", "debunk", "hack", "transform", "redefine"
    ]
    objects = [
        "new technology", "the economy", "space travel", "education system", "data privacy", "social media"
    ]
    endings = [
        "in 2025", "amid global changes", "sparking debate", "surprising experts", "breaking records"
    ]

    headline = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)} {random.choice(endings)}"
    return headline

# Generate 5 fake headlines
value=input(" Do u want to generate fake headlines ? (yes/no)").strip().lower()

# ==================with if clause===============================

# if value == "yes":
#     print(generate_fake_headline())
# elif value=="no":
#     print("Thank you for visiting")
# else:
#     print("please insert valid value (yes/no)")


# ================with while clause=============
while value:
    if value=="no":
        print("Thank you for visiting")
    else:
        print(generate_fake_headline()) 
    break




