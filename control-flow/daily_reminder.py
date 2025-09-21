# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder = ""
suffix = ""

# Use a match case statement to handle priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unrecognized priority"

# Use an if statement to check for time sensitivity
if time_bound == "yes":
    suffix = " that requires immediate attention today!"
elif time_bound == "no":
    suffix = ". Consider completing it when you have free time."

# Print the final reminder
print(reminder + suffix)
