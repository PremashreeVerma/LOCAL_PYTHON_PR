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
for _ in range(1):
    print(generate_fake_headline())


