from faker import Factory
from faker.providers.person.en_US import Provider
import re
import csv

fake = Factory.create('en-US')
fake.add_provider(Provider)

first_names = list(set(Provider.first_names))
last_names = list(set(Provider.last_names))


def generate_name():
    first_name = first_names.pop()
    last_name = last_names.pop()

    return f'{first_name} {last_name}'


def generate_company():
    return fake.company()


def generate_address():
    return fake.address()


def generate_email(nme, com):
    username = '.'.join(nme.lower().split())
    com = re.sub('[^0-9a-zA-Z]+', ' ', com)
    domain = '-'.join(com.lower().split())
    return f'{username}@{domain}.com'


def generate_phone():
    return fake.phone_number()


def generate_data():
    with open('data/customer_data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Company', 'Address', 'Email', 'Phone'])

        for _ in range(100):
            name = generate_name()
            company = generate_company()
            writer.writerow([name, company, generate_address(), generate_email(name, company), generate_phone()])


generate_data()
