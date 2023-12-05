import os
import re

#### F I L E  R E A D   L O G I C ####
filename = __file__.split("\\")[-1].split(".")[0] # day_n
input_file_path = os.path.join(os.path.dirname(__file__), "inputs\\", filename)
f = open(input_file_path,"r")
input = f.readlines()

######### S O L U T I O N ############
#########   P A R T  1    ############

# find symbols
symbols = ""
for line in input:
  for c in line:
    if not c.isdigit() and not c == "." and not c == "\n":
      if symbols.find(c) == -1:
        symbols += c
# print("symbols: "+symbols)

def getNumberAndPositionsAtIndex(line, index):
  number = ""
  for ci,c in enumerate(line):
    if ci < index:
      # skip characters until index is reached
      continue
    if c.isdigit():
      number += c
    else:
      # stop and record end position when encountering non digit number
      end = ci
      break
  # return number, start and end position
  return [int(number),index,end]

def checkForAdjacentSymbol(line,start,end):
  last_line_index = len(input)-1
  start_line = line-1 if line > 0 else 0
  end_line = line+1 if line < last_line_index else last_line_index
  for search_line in range(start_line,end_line+1):
    for symbol in symbols:
      startpos = start-1 if start > 0 else 0
      endpos = end+1 if len(input[line]) > end else len(input[line])
      search_string = input[search_line][startpos:endpos]
      if search_string.find(symbol) > -1:
        # print("found symbol in line",search_line,search_string)
        return True
  # print("no adjacent symbol found")
  return False

result = []
for li,line in enumerate(input):
  found_number = ""
  for ci,c in enumerate(line):
    if c.isdigit() and not line[ci-1].isdigit(): #first digit after a non-digit
      [number,start,end] = getNumberAndPositionsAtIndex(line,ci)
      # print("found",number,"at",li,":",ci)
      found = checkForAdjacentSymbol(li, start,end)
      if found:
        result.append(number)
print("Solution Part 1",sum(result))

######### S O L U T I O N ############
#########   P A R T  2    ############

def getLinesToSearch(line_no):
  start = line_no - 1 if line_no > 0 else 0
  end = line_no + 1 if line_no < len(input) else len(input)
  return range(start,end+1)

def ranges_overlap(range1, range2):
    # Assuming each range is a tuple (start, end)
    start1, end1 = range1
    start2, end2 = range2

    # Check for overlap
    return end1 >= start2 and start1 <= end2

def findAdjacentNumbers(line_pos,char_pos):
  result = []
  for search_line_pos in getLinesToSearch(line_pos):
    # match.end() returns the next character, not the last thats still part of the number, therefore subtract 1
    matches = [(match.start(), match.end()-1) for match in re.finditer(r'\d+', input[search_line_pos])]
    numbers = [int(match.group()) for match in re.finditer(r'\d+', input[search_line_pos])]
    # check if any of the matches are next to gear
    for i,match in enumerate(matches):
      if ranges_overlap(match,(char_pos-1,char_pos+1)):
        result.append(numbers[i])
  return result

result = 0
for li,line in enumerate(input):
  for ci,c in enumerate(line):
    if c == "*":
      adjNumbers = findAdjacentNumbers(li,ci)
      if len(adjNumbers) == 2:
        result += int(adjNumbers[0]) * int(adjNumbers[1])
print("Solution Part 2",result)