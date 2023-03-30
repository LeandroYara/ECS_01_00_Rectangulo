# Python program to read
# json file
  
  
import json
  
# Opening JSON file
f = open('assets/cfg/level_01.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
print(data['enemy_spawn_events'])
  
# Closing file
f.close()