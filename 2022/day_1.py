import os

#### F I L E  R E A D   L O G I C ####
filename = __file__.split("\\")[-1].split(".")[0] # day_n
input_file_path = os.path.join(os.path.dirname(__file__), "inputs\\", filename)
f = open(input_file_path,"r")
# input = f.readlines()

input = f.read()

max_elf_calories = 0
elf_calories = []

elves = input.split("\n\n")
for elf in elves:
  elf_sum = 0
  items = elf.split("\n")
  for item in items:
    elf_sum += int(item.strip())
  elf_calories.append(elf_sum)

  # if elf_sum > max_elf_calories:
  #   max_elf_calories = elf_sum
elf_calories = sorted(elf_calories, reverse=True)
top_three = sum(elf_calories[:3])

# print(input)
print(max_elf_calories)
print(top_three)
