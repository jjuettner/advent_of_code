import os

#### F I L E  R E A D   L O G I C ####
filename = __file__.split("\\")[-1].split(".")[0] # day_n
input_file_path = os.path.join(os.path.dirname(__file__), "inputs\\", filename)
f = open(input_file_path,"r")
input = f.readlines()

######### S O L U T I O N ############
#########   P A R T  1    ############

def getWins(card):
  winning_numbers = card.split(":")[1].split("|")[0].strip().replace("  "," ").split(" ")
  winning_numbers = [int(i) for i in winning_numbers]
  ticket_numbers = card.split("|")[1].strip().replace("  "," ").split(" ")
  ticket_numbers = [int(i) for i in ticket_numbers]
  wins = 0
  for tnum in ticket_numbers:
    if tnum in winning_numbers:
      wins += 1
  return wins


result = 0
for card in input:
  wins = getWins(card)
  result += int(2**(wins-1))
print("Solution Part 1",result)

######### S O L U T I O N ############
#########   P A R T  2    ############

wins = [] # make a list with the number of wins for every card
for card_number,card in enumerate(input):
  wins.append(getWins(card))

# make an array the length of wins and initialize with 1 (every original card)
copies = [1] * len(wins)

result = 0
for i,w in enumerate(wins):
  #for every original card, increment the w following cards | w = wins on the original card
  for card in range(i+1,i+w+1):
    # increment each of the copies by the number of copies of the original card 
    # (bc all of those copies will increment the copies of the following cards)
    copies[card] += copies[i]
# add up all the copies
print("Solution Part 2",sum(copies))