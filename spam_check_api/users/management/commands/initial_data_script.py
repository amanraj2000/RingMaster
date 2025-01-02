import random
from django.core.management.base import BaseCommand
from users.models import User, Contact
from faker import Faker

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):  
            name = fake.name()
            email = fake.email()
            phone_number = self.generate_phone_number()

            user = User.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                password='INSTAHYRE_IS_AWESOME'
            )

            for _ in range(3):  
                contact_name = fake.name()
                contact_phone_number = self.generate_phone_number()
                Contact.objects.create(
                    user=user,
                    name=contact_name,
                    phone_number=contact_phone_number
                )

        print('Intial Sample data has been added to the database.')


    def generate_phone_number(self):
        return str(random.randint(1000000000, 9999999999))
