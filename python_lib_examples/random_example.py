import random

# 1. Generate a random floating-point number between 0.0 and 1.0
random_float = random.random()
print(f"Random float between 0.0 and 1.0: {random_float}")

# 2. Generate a random integer between 10 and 50 (inclusive)
random_int = random.randint(10, 50)
print(f"Random integer between 10 and 50: {random_int}")

# 3. Choose a random element from a list
choices = ["apple", "banana", "cherry", "date"]
random_choice = random.choice(choices)
print(f"Random choice from the list: {random_choice}")

# 4. Shuffle a list in place
random.shuffle(choices)
print(f"Shuffled list: {choices}")

# 5. Generate a random sample of 2 elements from the list
random_sample = random.sample(choices, 2)
print(f"Random sample of 2 elements: {random_sample}")

# 6. Generate a random floating-point number within a specified range
random_uniform = random.uniform(1.5, 7.5)
print(f"Random float between 1.5 and 7.5: {random_uniform}")

# 7. Generate a random number from a normal (Gaussian) distribution with
# mean 0 and standard deviation 1
random_gauss = random.gauss(0, 1)
print("Random number from a normal distribution (mean=0, stddev=1):"
      f" {random_gauss}")
