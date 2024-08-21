import os
import django
from django.db.models import F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# Create queries within functions


def create_pet(name: str, species: str):
    Pet.objects.create(
        name=name,
        species=species
    )
    return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )
    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    locations = Location.objects.all().order_by('-id')

    return '\n'.join(str(l) for l in locations)


def new_capital():
    location = Location.objects.first()
    location.is_capital = True
    location.save()


def get_capitals():
    return Location.objects.all().filter(is_capital=True).values('name')


def delete_first_location():
    Location.objects.first().delete()


def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        percentage_discount = sum(int(x) for x in str(car.year)) / 100
        discount = float(car.price) * percentage_discount
        car.price_with_discount = float(car.price) - discount
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    tasks = Task.objects.all()
    return '\n'.join(str(t) for t in tasks)


def complete_odd_tasks():
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):
    tasks = Task.objects.all().filter(title=task_title)
    encoded_text = ''.join(chr(ord(x) - 3) for x in text)

    for task in tasks:
        task.description = encoded_text
        task.save()


def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')
    even_id_deluxe_rooms = []

    for room in deluxe_rooms:
        if room.id % 2 == 0:
            even_id_deluxe_rooms.append(str(room))

    return '\n'.join(even_id_deluxe_rooms)


def increase_room_capacity():
    rooms = HotelRoom.objects.all().order_by('id')
    prev_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if not prev_room_capacity:
            room.capacity += room.id

        else:
            room.capacity += prev_room_capacity

        prev_room_capacity = room.capacity

        room.save()


def reserve_first_room():
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()

    if last_room.is_reserved:
        last_room.delete()


def update_characters():
    Character.objects.filter(class_name='Mage').update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7,
    )

    Character.objects.filter(class_name='Warrior').update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4,
    )

    Character.objects.filter(class_name__in=['Assassin', 'Scout']).update(
        inventory='The inventory is empty',
    )


def fuse_characters(first_character, second_character):
    fuse_name = first_character.name + ' ' + second_character.name
    fuse_class = 'Fusion'
    fuse_level = (first_character.level + second_character.level) // 2
    fuse_strength = (first_character.strength + second_character.strength) * 1.2
    fuse_dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    fuse_intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    fuse_hit_points = (first_character.hit_points + second_character.hit_points)
    fuse_inventory = None
    if first_character.class_name in ['Mage', 'Scount']:
        fuse_inventory = 'Bow of the Elven Lords, Amulet of Eternal Wisdom'
    else:
        fuse_inventory = 'Dragon Scale Armor, Excalibur'

    Character.objects.create(
        name=fuse_name,
        class_name=fuse_class,
        level=fuse_level,
        strength=fuse_strength,
        dexterity=fuse_dexterity,
        intelligence=fuse_intelligence,
        hit_points=fuse_hit_points,
        inventory=fuse_inventory,
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.update(dexterity=30)


def grand_intelligence():
    Character.objects.update(intelligence=40)


def grand_strength():
    Character.objects.update(strength=50)


def delete_characters():
    Character.objects.filter(inventory='The inventory is empty').delete()

