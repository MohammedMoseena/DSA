import time

# Generate a large dataset
data = list(range(1000000))  # List with 1,000,000 elements
search_element = 999999

# # Searching in a list
# start_time = time.time()
# print(search_element in data)
# print(f"List search took {time.time() - start_time} seconds")

# Convert list to set for faster search
data_set = set(data)

# Searching in a set
start_time = time.time()
print(search_element in data_set)
print(f"Set search took {time.time() - start_time} seconds")
