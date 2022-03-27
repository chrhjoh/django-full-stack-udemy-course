import os
import django
from faker import Faker

# Needs to be set for the population before loading models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')
django.setup()

from AppTwo.models import User


def populate(n=5):
    for _ in range(n):
        fakegen = Faker()
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        email = fakegen.email()

        User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)

def main():

    DATA_POINTS=20
    print(f"Populating User table with {DATA_POINTS} observations")
    populate(DATA_POINTS)
    print("Done!")

if __name__ == "__main__":
    main()

