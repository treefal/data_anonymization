import csv
from collections import defaultdict
from faker import Factory
from faker.providers.person.en_US import Provider

fake = Factory.create('en-US')
fake.add_provider(Provider)

first_names = defaultdict(fake.first_name)
last_names = defaultdict(fake.last_name)
companies = defaultdict(fake.company)


def make_name(first_name, last_name):
    return first_name + ' ' + last_name


def make_email(first_name, last_name):
    return first_name.lower() + '.' + last_name.lower() + '@gmail.com'


def get_state(address):
    return address.split()[-2]


def get_zip(address):
    return address.split()[-1]


def anonymize_rows(rows):

    for row in rows:
        first_name = first_names[row['Name']]
        last_name = last_names[row['Name']]

        row['Name'] = make_name(first_name, last_name)
        row['Company'] = companies[row['Company']]
        row['Address'] = get_state(row['Address']) + ', ' + get_zip(row['Address'])
        row['Email'] = make_email(first_name, last_name)
        row['Phone'] = hash(row['Phone'])

        yield row


def anonymize(source, target):
    with open(source, 'r', newline='') as f:
        with open(target, 'w') as o:
            writer = csv.writer(o)
            writer.writerow(['Name', 'Company', 'Address', 'Email', 'Phone'])

            reader = csv.DictReader(f)
            writer = csv.DictWriter(o, reader.fieldnames)

            for row in anonymize_rows(reader):
                writer.writerow(row)


anonymize('data/customer_data.csv', 'data/anonymized_data.csv')
