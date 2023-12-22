import os

#### F I L E  R E A D   L O G I C ####
filename = __file__.split("\\")[-1].split(".")[0] # day_n
input_file_path = os.path.join(os.path.dirname(__file__), "inputs\\", filename)
f = open(input_file_path,"r")
input = f.readlines()


######### S O L U T I O N ############
#########   P A R T  1    ############
card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
hand_ranks = ["high","1pair","2pair","house","3oak","4oak","5oak"]

def rank_hand(cards):
  sorted(cards,reverse=True)
  max_of_kind = cards[max(cards, key=cards.get)]
  pairs = len([cards[card] for card in cards if cards[card] == 2])

  rank = "high"
  rank = "5oak" if max_of_kind == 5 else rank
  rank = "4oak" if max_of_kind == 4 else rank
  if max_of_kind == 3:
    rank = "3oak" 
    if pairs > 1:
      rank = "house"
  if max_of_kind == 2:
    rank = "1pair"
    if pairs > 1:
      rank = "2pair"
  return rank

for line in input:
  hand, bet = line.split(" ")
  cards = {}
  highest_idx = 1
  for card in hand:
    cards[card] = 1 if not card in cards else cards[card] + 1
    highest_idx = card_ranks.index(card) if card_ranks.index(card) > highest_idx else highest_idx
  hand_value = rank_hand(cards)

  print(hand,hand_value)
  