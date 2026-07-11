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


raining = True  # Example value, replace with actual logic to determine if it's raining

if raining:
    print("It's raining, don't forget to carry an umbrella!")
else:
    print("Wear Sunglasses, enjoy your day!")

temperature = 32  # Example value, replace with actual logic to get the temperature
if temperature > 30:
    print("It's hot!")
    print("Turn on AC")

score =   # Example value, replace with actual logic to get the score
if score >= 90:
    print("Excellent!")
    if score >= 75:
        print("Good job!")


    print("Hello World)          
