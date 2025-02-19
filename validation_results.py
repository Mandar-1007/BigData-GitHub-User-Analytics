import json

# Load validation set (ground truth)
with open("validation_set.json", "r") as f:
    validation_data = json.load(f)

# Count actual active users in the validation range since each entry is an active user
actual_active_users = len(validation_data)

# Load sample-based estimation results
with open("github_users_sample.json", "r") as f:
    sampled_data = json.load(f)

# Compute estimated active users in range 1-10,000
sample_size = len(sampled_data)
valid_users_sampled = sum(1 for user in sampled_data if user["id"] <= 10_000)  # Check only validation range
missing_users_sampled = sample_size - valid_users_sampled
missing_ratio = missing_users_sampled / sample_size

# Apply estimation formula
estimated_active_users = 10_000 * (1 - missing_ratio)

# Compute accuracy
error = abs(estimated_active_users - actual_active_users)
error_percentage = (error / actual_active_users) * 100

print("Validation Results:")
print(f"Actual Active Users in Validation Range: {actual_active_users}")
print(f"Estimated Active Users from Sampling: {int(estimated_active_users)}")
print(f"Absolute Error: {error}")
print(f"Error Percentage: {error_percentage:.2f}%")
