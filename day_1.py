import os

#### F I L E  R E A D   L O G I C ####
filename = __file__.split("\\")[-1].split(".")[0] # day_1
input_file_path = os.path.join(os.path.dirname(__file__), "inputs\\", filename)
f = open(input_file_path,"r")
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
#########   P A R T  1    ############
######## ( R E W R I T E ) ###########

result = 0
for line in input:
  matches = []
  for c in line: 
    if c.isdigit():
        matches.append(c)
  result += int(str(matches[0])+str(matches[-1]))
print("Solution 1 (Rewrite)", result)



######### S O L U T I O N ############
#########   P A R T  2    ############

result = 0
number_words = ["one","two","three","four","five","six","seven","eight","nine"]
for line in input:
  matches = []
  # iterate over every character in current line
  for ci,c in enumerate(line): 
    # c: current character | ci: index of current character
    # if current character is a digit, add it to the matches array
    if c.isdigit():
      matches.append(c)
    # iterate over number words that could appear in this position
    for wi, word in enumerate(number_words):
      # word: current number word string we are checking for | wi: index of number word in number_words array
      # if a number word is starting at current position (i), append to the matches array
      if line[ci:].startswith(word):
        matches.append(wi+1) # get the digit from the number word we were checking, "one"(1) is at index 0, so add 1 to the result
  
  # create the two digit number from the first and last match
  # cast to strings to concatenate
  lineresult = str(matches[0]) + str(matches[-1])

  # add two digit number to total
  result += int(lineresult)
  
print("Solution Part 2: ", result)







