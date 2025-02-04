from faker import Faker
from utils.helper import get_specific_date
from random import randrange, random

fake = Faker()


class User:
    def __init__(self):
        self.user_name = f"username-{get_specific_date()}"
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.email = f"email{get_specific_date()}@gmail.com"
        self.password = fake.password()
        self.address = fake.address()
        self.state = fake.state()
        self.city = fake.city()
        self.zipcode = fake.zipcode()
        self.mobile_number = fake.phone_number()
        self.gender = "1"  # 1 = Mr. / 2 = Mrs.
        self.day_birth = str(randrange(1, 31))
        self.month_birth = str(randrange(1, 12))
        self.year_birth = str(randrange(1900, 2021))
