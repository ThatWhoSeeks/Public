from datetime import datetime

# Ask the user for their age
age = int(input("Wie alt bist du? "))

# Get the current year
current_year = datetime.now().year

# Calculate the birth year
birth_year = current_year - age

# Display the birth year
print(f"Du wurdest im Jahr {birth_year} geboren.")
