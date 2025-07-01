import datetime
import json
# TODO: Write to file: Task to complete, deadline
# TODO: Check if file created or initialised with expected values

'''

Wants: write and store tasks (could make sense to have these created as objects with classes)
It should:
- Record tasks and deadlines
- Show upcoming deadlines on request (based on set or custom intervals)
'''

def todo_highest_item():
    # TODO First: Load sorted data by highest score
    with open("data.json", 'r') as file:
        loaded_data = json.load(file)
    return loaded_data

def score_calc():
    # TODO: Write score for item based on user defined score, or eisenhower matrix q&a
    ...

def main_screen():
    # TODO: Display ordered todo list
    name = input("What's your name again?: ")
    print(f"Hi {name}, welcome back to Neglectful Hobbies")
    first_todo = todo_highest_item()
    print(f"Upcoming...\n {first_todo}")

main_screen()

# TODO: Calc Operations: Checks at set/custom intervals for upcoming deadlines
# TODO: Hard - Send Operations: Notification to user in phone

