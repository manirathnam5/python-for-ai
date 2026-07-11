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
