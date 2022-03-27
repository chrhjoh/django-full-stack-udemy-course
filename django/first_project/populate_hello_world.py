import os
import django
import random
from faker import Faker

# Needs to be set for the population before loading models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()

from hello_world.models import AccessRecord, WebPage, Topic


def add_topic():
    TOPICS = ['Search', 'Social', 'Marketplace', 'News', 'Games']
    t = Topic.objects.get_or_create(top_name=random.choice(TOPICS))[0]
    t.save()
    return t

def populate(n=5):
    for i in range(n):
        
        top = add_topic()
        fakegen = Faker()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Since topic is foreign key, then need to pass entire Topic object
        webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

def main():


    DATA_POINTS=20
    print(f"Populating Topic, WebPage and AccessRecord tables with {DATA_POINTS} observations")
    populate(DATA_POINTS)
    print("Done!")

if __name__ == "__main__":
    main()

