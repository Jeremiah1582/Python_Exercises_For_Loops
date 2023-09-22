# Note: there are many solutions to every problem, This is just one

# ......................code here............
# List of weekend days
weekend = ['Saturday', 'Sunday']

# Loop through each day in the weekend list
for day in weekend:
    weather = input(f"What's the weather on {day}? (rainy, sunny, or cold) ").lower()

    # Use conditional statements to provide outfit recommendations
    if weather == "rainy":
        print(f"On {day}, wear a raincoat and carry an umbrella.")
    elif weather == "sunny":
        print(f"On {day}, wear a t-shirt and sunglasses!")
    elif weather == "cold":
        print(f"On {day}, grab a heavy jacket and a scarf.")
    else:
        print(f"I'm not sure about the outfit for {day} with that weather condition.")
        
# ......................code here ............