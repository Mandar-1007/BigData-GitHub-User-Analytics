import yaml
import requests
import time
import json

# Load GitHub Token from config.yaml
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)
GITHUB_TOKEN = config["github"]["token"]

# GitHub API URL
github_api_url = "https://api.github.com/users?since={}"
headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

# Parameters
num_samples = 1000
sleep_time = 2

# Store results
user_data_list = []

# Start fetching users from ID 0
since_id = 0
for _ in range(num_samples // 30):  # Each request returns ~30 users
    print(f"Fetching users starting from ID {since_id}")
    response = requests.get(github_api_url.format(since_id), headers=headers)

    if response.status_code == 200:
        users = response.json()
        if not users:
            print("No more users found.")
            break
        user_data_list.extend(users)
        since_id = users[-1]["id"]  # Update since_id to fetch next batch
    elif response.status_code == 403:
        print("Rate limit exceeded. Sleeping for 60 seconds...")
        time.sleep(60)
    else:
        print(f"Unexpected error: {response.status_code}")
        break

    time.sleep(sleep_time)  # Avoid hitting API limits

# Save results to a JSON file
with open("github_users_sample.json", "w") as f:
    json.dump(user_data_list, f, indent=4)

print("Data crawling completed. Saved to 'github_users_sample.json'")
