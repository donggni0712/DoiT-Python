person = dict(name="John", age=30, city="New York")

print(person["name"])  # John
print(person["age"])  # 30

person["age"] = 31

print(person)

person["job"] = "Engineer"
print(person)

del person["city"]
print(person)
