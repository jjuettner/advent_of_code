import os
import re
import numpy
import math

#### F I L E  R E A D   L O G I C ####
filename = __file__.split("\\")[-1].split(".")[0] # day_n
input_file_path = os.path.join(os.path.dirname(__file__), "inputs\\", filename)
f = open(input_file_path,"r")
input = f.readlines()


######### S O L U T I O N ############
#########   P A R T  1    ############

def simulate(record_to_beat,distance):
  options = []
  for t in range(1,record_to_beat+1):
    speed = t # speed in m/s = wind up time in ms
    time_elapsed = speed # first movement starts after wind up
    distance_traveled = 0 
    while(time_elapsed < record_to_beat):
      # increase traveled distance by speed for every 1ms
      time_elapsed+=1
      distance_traveled+=speed
      # if i wanna beat the record i have to have traveled more than the distance of the race within the record time, otherwise im just tied
      if(distance_traveled > distance):
        options.append(t)
        break
  return options

record_times = [int(s.strip()) for s in re.findall(r'\d+', input[0][10:])]
distances = [int(s.strip()) for s in re.findall(r'\d+', input[1][10:])]

results = []
for i in range(len(record_times)):
  options = simulate(record_times[i],distances[i])
  results.append(len(options))
  print(str(len(options))+" options found!")
print("Solution Part 1:",numpy.prod(results))

######### S O L U T I O N ############
#########   P A R T  2    ############

def part2(time,distance):
    exact_acceleration = (time - math.sqrt((time**2 - 4*distance))) / 2
    min_acceleration = int(exact_acceleration + 1)
    return time - 2*min_acceleration + 1

record_time = int("".join(str(time) for time in record_times))
distance = int("".join(str(dist) for dist in distances))

# assume two functions
# A: y = distance (d)
# B: y = mx + b
# shift the function to the right by the amount of wind-up-time (w) im ms
# B: y = m(x-w) + b
# look for the intersections (start and end of the range that will break the record)
# d = m(x-w) + b
# solve for w and set b to 0
# w^2 - wx + d = 0
# w1 = (x+sqrt(x2-4d))/2
# w2 = (x-sqrt(x2-4d))/2
# where x is time

w1 = (record_time - math.sqrt((record_time**2 - 4*distance))) / 2
w2 = (record_time + math.sqrt((record_time**2 - 4*distance))) / 2

print("Solution Part 2",round(w2 - w1 - 1))
