import yaml
import requests
import time
import json

# Load GitHub Token from config.yaml
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)
GITHUB_TOKEN = config["github"]["token"]
headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

# GitHub API URL for "since" API
github_api_url = "https://api.github.com/users?since={}"

# Parameters
max_id = 10_000  # Validation set range (1 to 10,000)
sleep_time = 2  # Adjust based on API rate limits

# Store results
validation_data = []
since_id = 0  # Start from ID 0

print("Collecting validation set (active users in range 1-10,000)...")
while since_id < max_id:
    print(f"Fetching users starting from ID {since_id}")
    response = requests.get(github_api_url.format(since_id), headers=headers)

    if response.status_code == 200:
        users = response.json()
        if not users:
            print("No more users found.")
            break
        validation_data.extend(user for user in users if user["id"] <= max_id)  # Keep only users in range
        since_id = users[-1]["id"]  # Update "since" ID for next batch
    elif response.status_code == 403:
        print("Rate limit exceeded. Sleeping for 60 seconds...")
        time.sleep(60)
    else:
        print(f"Unexpected error: {response.status_code}")
        break

    time.sleep(sleep_time)

# Save validation set to a JSON file
with open("validation_set.json", "w") as f:
    json.dump(validation_data, f, indent=4)

print(f"Validation set collection complete. Total active users collected: {len(validation_data)}")
