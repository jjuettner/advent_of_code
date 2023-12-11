import os

#### F I L E  R E A D   L O G I C ####
filename = __file__.split("\\")[-1].split(".")[0] # day_n
input_file_path = os.path.join(os.path.dirname(__file__), "inputs\\", filename)
f = open(input_file_path,"r")
input = f.read()


# parse input
segments = input.split("\n\n")
seeds = [int(i) for i in segments[0].split(":")[1].strip().split(" ")]

maps = {
  "seed_soil": segments[1].split("\n")[1:],
  "soil_fertilizer": segments[2].split("\n")[1:],
  "fertilizer_water": segments[3].split("\n")[1:],
  "water_light": segments[4].split("\n")[1:],
  "light_temp": segments[5].split("\n")[1:],
  "temp_humidity": segments[6].split("\n")[1:],
  "humidity_location": segments[7].split("\n")[1:],
}

for map in maps:
  res = []
  for curmap in maps[map]:
    res.append([int(i) for i in curmap.split(" ")])
  maps[map] = res


def findDestination(input,map_table_name):
  result = input
  for dst,src,lgt in maps[map_table_name]:
    if input >= src and input < src+lgt:
      result = input + (dst - src)
      break
  return result



######### S O L U T I O N ############
#########   P A R T  1    ############

locations=[]
for si, seed in enumerate(seeds):
  # path = ["seed: "+str(seed)]
  destination = seed
  for map in maps:
    destination = findDestination(destination,map)
    # path.append(map.split("_")[1]+": "+str(destination))
  # print(path)
  locations.append(destination)
print("Solution Part 1",min(locations))


######### S O L U T I O N ############
#########   P A R T  1    ############

# seed_numbers = []
# for i,l in enumerate(seeds):
#   if i%2 != 0:
#     for no in range(seeds[i-1],seeds[i-1]+l):
#       seed_numbers.append(no)
# print("seed numbers to check",len(seed_numbers))

min_loc = -1
for i,l in enumerate(seeds):
  snum = 0
  if i%2 != 0:
    for seed in range(seeds[i-1],seeds[i-1]+l):
      destination = seed
      for map in maps:
        destination = findDestination(destination,map)
      if min_loc < 0 or destination < min_loc:
        min_loc = destination
      snum += 1
    print("range",str(i/2),":",snum," entries")

print("Solution Part 2",min_loc)