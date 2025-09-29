# Create an empty box to store names and birthdays
friends_birthdays = {}

# Ask for birthday info 5 times
for i in range(5):
    name = input(f"What's the name of friend {i+1}? ")
    birthday = input(f"What is {name}'s birthday? (e.g., 12/03/2010) ")
    friends_birthdays[name] = birthday  # Store the info

# Show all the birthdays
print("\nHere are the birthdays Raj collected:")
for name, birthday in friends_birthdays.items():
    print(f"{name}'s birthday is on {birthday}")
