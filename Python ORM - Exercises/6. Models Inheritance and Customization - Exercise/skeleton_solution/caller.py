import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Mage, Necromancer, Message, UserProfile, Student, CreditCard

#
#
# mage = Mage.objects.create(
#     name="Fire Mage",
#     description="A powerful mage specializing in fire magic.",
#     elemental_power="Fire",
#     spellbook_type="Ancient Grimoire"
# )
#
# necromancer = Necromancer.objects.create(
#     name="Dark Necromancer",
#     description="A mage specializing in dark necromancy.",
#     elemental_power="Darkness", spellbook_type="Necronomicon",
#     raise_dead_ability="Raise Undead Army"
# )
# print(mage.elemental_power)
# print(mage.spellbook_type)
# print(necromancer.name)
# print(necromancer.description)
# print(necromancer.raise_dead_ability)


# Create users
# user1 = UserProfile.objects.create(username='john_doe', email='john@example.com', bio='Hello, I am John Doe.')
#
# user2 = UserProfile.objects.create(username='jane_smith', email='jane@example.com', bio='Hi there, I am Jane Smith.')
#
# user3 = UserProfile.objects.create(username='alice', email='alice@example.com', bio='Hello, I am Alice.')
#
# # Create a message from user1 to user2
# message1 = Message.objects.create(
#     sender=user1,
#     receiver=user2,
#     content="Hello, Jane! Could you please tell Alice that tomorrow we are going on vacation?")
# print(message1.content)
#
# # Mark the message as read
# message1.mark_as_read()
# print(f"Is read: {message1.is_read}")
#
# # Create a reply from user2 to user1
# reply_message = message1.reply_to_message(
#     receiver=user1,
#     reply_content="Hi John, sure! I will forward this message to her!")
# print(reply_message.content)
#
# # Create a forwarded message from user2 to user3
# forwarded_message = message1.forward_message(sender=user2, receiver=user3)
# print(f"Forwarded message from {forwarded_message.sender.username} to {forwarded_message.receiver.username}")


# Test cases
# student1 = Student(name="John", student_id=12345)
# student1.save()
#
# student2 = Student(name="Alice", student_id=45.23)
# student2.save()
#
# student3 = Student(name="Bob", student_id="789")
# student3.save()
#
# # Retrieving student IDs from the database
# retrieved_student1 = Student.objects.get(name="John")
# retrieved_student2 = Student.objects.get(name="Alice")
# retrieved_student3 = Student.objects.get(name="Bob")
#
# print(retrieved_student1.student_id)
# print(retrieved_student2.student_id)
# print(retrieved_student3.student_id)
# Create CreditCard instances with card owner names and card numbers


credit_card1 = CreditCard.objects.create(card_owner="Krasimir", card_number="1234567890123450")
credit_card2 = CreditCard.objects.create(card_owner="Pesho", card_number="9876543210987654")
credit_card3 = CreditCard.objects.create(card_owner="Vankata", card_number="4567890123456789")

# Save the instances to the database
credit_card1.save()
credit_card2.save()
credit_card3.save()

# Retrieve the CreditCard instances from the database
credit_cards = CreditCard.objects.all()

# Display the card owner names and masked card numbers
for credit_card in credit_cards:
    print(f"Card Owner: {credit_card.card_owner}")
    print(f"Card Number: {credit_card.card_number}")
