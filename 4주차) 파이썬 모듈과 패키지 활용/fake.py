from faker import Faker

fake = Faker('ko-KR')
data = [{fake.name():fake.address()} for i in range(5)]
print(data)