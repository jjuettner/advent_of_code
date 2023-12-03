import os

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
        print("found symbol in line",search_line,search_string)
        return True
  print("no adjacent symbol found")
  return False




result = []
for li,line in enumerate(input):
  found_number = ""
  for ci,c in enumerate(line):
    if c.isdigit() and not line[ci-1].isdigit(): #first digit after a non-digit
      [number,start,end] = getNumberAndPositionsAtIndex(line,ci)
      print("found",number,"at",li,":",ci)
      found = checkForAdjacentSymbol(li, start,end)
      if found:
        result.append(number)
print(sum(result))