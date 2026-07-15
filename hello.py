import requests

latitude = 48.85
longitude = 2.35


url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"


response = requests.get(url)
data = response.json()

print(data)

favorite_food = "Hyderabadi Biryani"
city = "Bangalore"
print(f"My favorite food is {favorite_food} and I live in {city}.")

flat = 504
area = "Marathahalli"
print(f"I live in {area} and my flat number is {flat}.")


def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, stranger!")


greet("Manish")


def first_function():
    pass


def second_function():
    pass


long_string = "This is a very long string that spans multiple lines for readability"

print(long_string)

shirt_price = 3000
print(shirt_price)

pant_price = 2000
print(f"Pant price: {pant_price}")

fridge_price = 15000
print(f"Fridge price : {fridge_price}")

isPremium_user = True
if isPremium_user:
    print("User is a premium user.")
else:
    print("User is not a premium user.")

age = 23
print(type(age))


company = "OpenAI"
print(type(company))


is_active = True
print(type(is_active))


total_amount = 100.50 + 200.75
print(total_amount)


first_name = "Swamy"
last_name = "Reddy"
full_name = first_name + " " + last_name
print(full_name)


tab_name = "Samsung"
print(f"Tab name: {tab_name}")

print(type(4.34))

print(type("Hello"))

print(type(True))


pi = 3.14159
price = 19.99
temperature = 25.5
print(f"Pi: {pi}, Price: {price}, Temperature: {temperature}")

total = 100 + 200.5
print(f"Total: {total}")

cube = 3**3
print(f"Cube of 3: {cube}")

sqaure = 5**2
print(f"Square of 5: {sqaure}")

result = 10 / 3
print(f"Result of 10 divided by 3: {result}")


result2 = 10 // 3
print(f"Result of 10 floor divided by 3: {result2}")


income = 50000
tax = 300
net_income = income // tax
print(f"Net income: {net_income}")


million = 1_000_000
print(f"Million: {million}")

welcome_message = "Welcome to the Python world!"
print(welcome_message)

flat_info = """
flat number: 504
area: Marathahalli
city: Bangalore 
"""
print(flat_info)


stars = "*" * 5
print(stars)

name = "John"
print(len(name))

name = "Alice"
print(len(name))


has_permission = True
if has_permission:
    print("User has permission.")
else:
    print("User does not have permission.")

    age = 25

# Equality
print(age == 25)  # True - equals
print(age != 30)  # True - not equals

# Greater/Less than
print(age > 20)  # True - greater than
print(age < 30)  # True - less than
print(age >= 25)  # True - greater or equal
print(age <= 25)  # True - less or equal


# Operators
print(10 + 5)
print(20 - 45)
print(10 * 4)
print(20 / 5)
