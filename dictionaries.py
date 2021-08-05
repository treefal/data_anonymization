from collections import defaultdict
from faker import Factory
from faker.providers.person.en_US import Provider

fake = Factory.create('en-US')
fake.add_provider(Provider)

# Dictionaries are global in order to produce same fake data for same original data
first_names = defaultdict(fake.first_name)
last_names = defaultdict(fake.last_name)
companies = defaultdict(fake.company)