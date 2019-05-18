import random

import os

import ipdb

def createDir():
  # ipdb.set_trace()
  print("Creating folder")
  experiment_id = random.randint(10000, 20000)
  os.mkdir(f"/Users/krzyczak/Desktop/test/data/{experiment_id}")
  return f"{experiment_id}"

# try:
#   print(f"your_path fomr from config before set: {your_path}")
# except NameError:
#   your_path = createDir()

# print(f"your_path fomr from config before set: {your_path}")

your_path = createDir()
print(f"your_path fomr from config after set: {your_path}")

DIR_RAW = f"{your_path}/main_data"

