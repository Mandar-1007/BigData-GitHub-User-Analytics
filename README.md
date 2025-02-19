# ESTIMATING ONLINE SITE (GITHUB) STATISTICS

# Introduction
GitHub is a widely used platform for version control and collaboration, with millions of users. However, not all assigned user IDs correspond to active accounts due to account deletions. Since GitHub assigns user IDs incrementally, there are gaps where users have deleted their accounts. The challenge is to estimate the total number of active GitHub users without exhaustively collecting all user data.

# Why is Sampling & Estimation Important?
GitHub's API has rate limits that prevent exhaustive collection of user IDs. Instead of downloading all IDs, we use sampling and estimation techniques to infer the total number of active users efficiently. This is important in big data analysis where full data collection is impractical. This project implements a statistical approach to estimate the number of valid GitHub users using sampling and unbiased estimation techniques. We validate our approach using a validation set and provide proof of unbiasedness and correctness through statistical visualizations.

# Project Structure
The repository contains the following Python scripts, each serving a specific purpose in data collection, estimation, and validation.

**1. Data Crawler: data_crawler.py**

**Purpose**
This script collects GitHub user data using GitHub's API and stores it in a JSON file.

**How It Works:**
- The script makes requests to the GitHub API using the "since" parameter to fetch users.
- It iterates through batches of 30 users per request, ensuring efficient crawling without exceeding API limits.
- The collected data is saved in github_users_sample.json.

**Output:**
JSON File: github_users_sample.json containing sampled users.
![image](https://github.com/user-attachments/assets/bd184ab6-da5a-42f0-b203-b632dd219c44)


**2. User Estimation: user_estimation.py**

**Purpose**
This script estimates the total number of valid GitHub users based on the missing user ratio in a sampled validation set.

**How It Works:**
- Defines a validation set (ID range 1-10,000) where we exhaustively collect users.
- Computes the missing ratio by comparing active users in this range.
- Uses this ratio to estimate the total number of valid users across all of GitHub.

**Output:**
![image](https://github.com/user-attachments/assets/ea32c74f-54f5-457a-8ff2-b332fba4230e)


**3. Unbiasedness Proof (Box Plot): unbiasedness_boxplot.py**

**Purpose**
This script generates a box plot to demonstrate that our estimation method is unbiased.

**How It Works:**
- Runs multiple experiments with different sampling budgets (10, 20, 30, ... 200).
- Plots the estimated total user count distributions across sample sizes.
- If the median line is centered, it confirms that the estimator is unbiased.

**Output:**
![image](https://github.com/user-attachments/assets/6a3ab4cd-7d89-4ba4-9794-2a364a64b50a)
The red horizontal line represents the average estimate. If it stays near the center, it means that our estimation method is neither overestimating nor underestimating consistently.


**4. Correctness of Proof: correctness_proof.py**

**Purpose**
This script validates that our estimator remains stable across different sampling budgets.

**How It Works:**
- Runs multiple Monte Carlo experiments with different sample sizes.
- Plots average estimates over different sample sizes.
- If the estimates remain stable, it confirms that our method is correct and reliable.

**Output:**
![image](https://github.com/user-attachments/assets/05f0a8ff-622a-481e-a57d-6aeafec2fbbb)
The green line shows how estimates change as we increase the sample size. If it fluctuates but stabilizes, our estimator is consistent.


**5. Validation Set Crawler: validation_crawler.py**

**Purpose**
This script exhaustively collects all active users in the validation range (1-10,000) to create a ground truth dataset

**How It Works:**
- Uses the GitHub API since parameter to retrieve all valid users within the range.
- Saves collected data in validation_set.json for validation.

**Output:**
JSON File: validation_set.json containing sampled users.
![image](https://github.com/user-attachments/assets/7bf79035-8eba-4a6c-94da-bea19b399a91)


**6. Validation Results: validation_results.py**

**Purpose**
This script compares the estimated user count against the ground truth validation set to measure accuracy.

**How It Works:**
- Computes the actual active users in the validation set.
- Applies the sampling-based estimation method to predict the active user count.
- Computes the absolute error and error percentage to evaluate accuracy.

**Output:**
![image](https://github.com/user-attachments/assets/eac602fd-bf79-47b8-a417-a105b2f6c1fd)


**7. Full GitHub ID Space Estimation: full_space_estimation.py**

**Purpose**
This script estimates the total number of valid GitHub users across the entire ID space.

**How It Works:**
- Uses all sampled users to estimate total valid users.
- Computes the missing user ratio in the full dataset.
- Estimates total active GitHub users using the same method as the validation set.

**Output:**
![image](https://github.com/user-attachments/assets/4ca3e36a-c343-4627-961c-701062109626)


# Key Takeaways:

✔ Sampling & estimation allows us to measure GitHub’s total users efficiently.

✔ The validation set helps assess accuracy and adjust the estimation model.

✔ Box plots confirm unbiasedness, proving the method is statistically sound.

✔ Correctness proof confirms stability, making our method reliable.

This project demonstrates the power of statistical inference and unbiased estimation in large-scale data collection


# How to Run the Project Locally

**1. Clone the repository**

git clone https://github.com/Mandar-1007/BigData-GitHub-User-Analytics.git

**2. Install dependencies**

pip install -r requirements.txt

**3. Run the scripts in order:**

Run the scripts in order
- python data_crawler.py
- python user_estimation.py
- python unbiasedness_boxplot.py
- python correctness_proof.py
- python validation_crawler.py
- python validation_results.py
- python full_space_estimation.py


# Conclusion

This project successfully estimates the total number of valid GitHub users using a sampling-based statistical approach. By leveraging GitHub's API and unbiased estimation techniques, we efficiently infer the number of active users despite API rate limits and missing user IDs.

**User Estimation Accuracy:**
- From our validation set (1-10,000), we found 9,433 active users.
- Our estimation method predicted 10,000 active users, with a 6.01% error rate, confirming high accuracy.

**Proof of Unbiasedness (Box Plot Analysis):**
- Our box plot visualization shows that estimated counts fluctuate symmetrically above and below the red average line, proving our estimation method is unbiased.
- The red horizontal line remains centered, confirming that our approach does not consistently overestimate or underestimate the total user count.

**Correctness Proof (Stability of Estimates):**
- Our correctness proof visualization demonstrates that average estimates remain stable across different sampling budgets.
- The estimates fluctuate initially but stabilize as the sample size increases, proving the consistency and reliability of our estimator.

**Full GitHub User Space Estimation:**
- Based on 990 sampled users, we estimated 10,128,194 total valid GitHub users, aligning with expected values.


# Final Remarks:

This study confirms that a sampling-based approach can provide a robust and scalable solution for estimating GitHub's total active users. Our unbiased estimator is validated through empirical results, demonstrating high accuracy and stability. The results highlight the effectiveness of statistical inference in big data acquisition and measurement, offering insights that can be applied to similar real-world estimation problems where complete data collection is infeasible.

The ability to estimate GitHub’s total valid users provides valuable insights across business, technology, research, and policymaking. Whether it’s tracking developer growth, measuring market trends, improving cybersecurity, support open-source adoption, and inform business and policy decisions, this data-driven approach opens up new ways to study and understand the evolving landscape of software development.
