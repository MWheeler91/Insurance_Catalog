import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Home_Catalog.settings')

import django
django.setup()


import random
from faker import Faker
from catalog.models import *


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Home_Catalog.settings')


# fake pop script
fakegen = Faker()


def main():
    print("Populating the script!")

    FakeItem(30000)
    print("Complete!")



# creates Fake address for Person


def FakeItem(n):
    all_categories = list(Category.objects.all())
    all_conditions = list(Condition.objects.all())
    all_rooms = list(Room.objects.all())
    for x in range(n):
        categories_index = random.randrange(len(all_categories))
        conditions_index = random.randrange(len(all_conditions))
        rooms_index = random.randrange(len(all_rooms))

        item = Item.objects.get_or_create(
            item_name=fakegen.street_name(),
            item_description=fakegen.street_name(),
            item_category=all_categories[categories_index],
            condition=all_conditions[conditions_index],
            room=all_rooms[rooms_index],
            value=random.randint(1, 5000),
        )



if __name__ == '__main__':
    main()