
import json

# Specify the path to your JSON file
json_file_path = "userJson.txt"

# Read the JSON file
with open(json_file_path, "r") as file:
    json_body = file.read()

# Parse the JSON
data = json.loads(json_body)

# Extract the email addresses
users = data['users']
emails = [user['email'] for user in users]

# Print the email addresses
for email in emails:
    print(email)