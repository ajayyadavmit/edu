# import math

# # importing random module
# import random

# random.seed(3)

# # print a random number between 1 and 1000.
# print(random.randint(1, 1000))

# # if you want to get the same random number again then,
# random.seed(3) 
# print(random.randint(1, 1000))

# # If seed function is not used

# # Gives totally unpredictable responses.
# print(random.randint(1, 1000))


import kagglehub

# Download latest version
path = kagglehub.dataset_download("theseus200719/math-equations-dataset-aidav7-modified")

print("Path to dataset files:", path)