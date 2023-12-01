import os

filename = __file__.split("\\")[-1].split(".")[0]
input_file_path = os.path.join(os.path.dirname(__file__), "inputs\\", filename)
f = open(os.path.join(os.path.dirname(__file__), "inputs\\", filename),"r")
input = f.readlines()

######### S O L U T I O N ############
#########   P A R T  1    ############
result = 0
for line in input:
  for c in line:
    if c.isnumeric():
      first_digit = c
      break
  for c in reversed(line):
    if c.isnumeric():
      last_digit = c
      break
  lineresult = str(first_digit) + str(last_digit)
  result += int(lineresult)

print("Solution Part 1: ",result)

######### S O L U T I O N ############
#########   P A R T  2    ############

result = 0
number_words = ["one","two","three","four","five","six","seven","eight","nine"]
for line in input:
  matches = []
  # iterate over every character in current line
  for i,c in enumerate(line): 
    # c: current character | i: index of current character
    # if current character is a digit, add it to the matches array
    if c.isdigit():
      matches.append(c)
    # iterate over number words that could appear in this position
    for d, word in enumerate(number_words):
      # word: current number word string we are checking for | d: position of number word in number_words array
      # if a number word is starting at current position (i), append to the matches array
      if line[i:].startswith(word):
        matches.append(d+1) # get the digit from the number word we were checking, "one"(1) is at index 0, so add 1 to the result
  
  # create the two digit number from the first and last match
  # cast to strings to concatenate
  lineresult = str(matches[0]) + str(matches[-1])

  # add two digit number to total
  result += int(lineresult)
  
print("Solution Part 2: ", result)







