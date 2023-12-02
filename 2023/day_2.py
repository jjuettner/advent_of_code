import os

#### F I L E  R E A D   L O G I C ####
filename = __file__.split("\\")[-1].split(".")[0] # day_n
input_file_path = os.path.join(os.path.dirname(__file__), "inputs\\", filename)
f = open(input_file_path,"r")
input = f.readlines()


######### S O L U T I O N ############
#########   P A R T  1    ############

limits = {"red": 12,"green": 13,"blue":14}

possible_game_id_sum = 0
for game in input:
  game_possible = True
  game_id = game.split(":")[0].split(" ")[1]
  rolls = game.split(":")[1].split(";")
  maxResults = {"red": 0,"green": 0,"blue": 0}
  for roll in rolls:
    results = roll.split(",")
    for result in results:
      color = result.strip().split(" ")[1]
      amount = int(result.strip().split(" ")[0])
      if int(amount) > int(maxResults[color]):
        maxResults[color] = amount
      for colorkey in limits:
        if maxResults[colorkey] > limits[colorkey]:
          # print("Game ",game_id,"failed:",colorkey,maxResults[colorkey],"/",limits[colorkey])
          game_possible = False
          break
      if not game_possible:
        break
    if not game_possible:
      break
  if game_possible:
    possible_game_id_sum += int(game_id)

print("Sum of all possible game IDs:",possible_game_id_sum)



######### S O L U T I O N ############
#########   P A R T  2    ############

power_sum = 0
for game in input:
  game_possible = True
  game_id = game.split(":")[0].split(" ")[1]
  rolls = game.split(":")[1].split(";")
  maxResults = {"red": 0,"green": 0,"blue": 0}
  for roll in rolls:
    results = roll.split(",")
    for result in results:
      color = result.strip().split(" ")[1]
      amount = int(result.strip().split(" ")[0])
      if int(amount) > int(maxResults[color]):
        maxResults[color] = amount
  game_power = 1
  for colorkey in maxResults:
    game_power *= maxResults[colorkey]
  power_sum += game_power
print("Combined Game Power:",power_sum)






