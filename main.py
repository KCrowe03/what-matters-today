from datetime import date  # Getting today's date so I can log it with my answers

# STEP 1: Set up today's date
today = date.today()  # Example: 2025-04-07 — may be useful later for trends or summaries

# Print welcome message with the date
print(f"\nWhat Matters Today – {today}")
print("Please answer 'yes' or 'no' to each question.\n")

# STEP 2: List the tasks I want to check in on
# May expand this later 
tasks = [
    "Did you practice coding today?",
    "Did you practice Python today?",
    "Did you practice SQL today?",
    "Did you complete any WGU assignments?",  # May expand to specific assignments later
    "Did you check Code:You slack?",
    "Did you check email?",
    "Did you check 4H calendar today?",
    "Did you check Dojo app?",
    # Might add: walked, water, sleep, family time,homeschool, bills, mail etc.
]

# STEP 3: Collect my answers
# Reminder: This list will hold the yes/no answers that I'll save to CSV
responses = []

# STEP 4: Ask each question and store the response
for task in tasks:
    answer = input(task + " ")  # Ask the question in the terminal
    responses.append(answer.lower())  # Save in lowercase (yes/no) for consistency

# STEP 5: Wrap it up
# May expand later to give a motivational quote or summary
print("\nThank you for checking in today.")

import csv  # This handles saving to a CSV file
import os   # Used to check if the file already exists

# STEP 6: Save the date + responses to a CSV file
filename = "what_matters_log.csv"

# Check if the file already exists (so we I don't write the header twice)
file_exists = os.path.isfile(filename)

# Open the file in append mode (add to the end of it)
with open(filename, mode="a", newline="") as file:
    writer = csv.writer(file)

    # If the file is brand new, write the header row first
    if not file_exists:
        header = ["Date"] + tasks
        writer.writerow(header)

    # Then write today's row of answers
    row = [today] + responses
    writer.writerow(row)


