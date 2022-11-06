# Print result after every function to check
# Read the info in every functions to get the proper understanding of desired output

import json
from multiprocessing.sharedctypes import Value

filepaths = 'Devsoc/data.json'


# IMPORTANT: Change the filepath to your actual file path while working

def read_data(filepath):
    with open(filepath) as json_file:
        data = json.load(json_file)
    # Read data from filepaths
    return data


# Added return data
data = read_data(filepaths)
print(data)


# Added print statement to check the working

def get_oldest_avenger(data):
    max = 0
    oldest_avenger = []
    # Added a null list named oldest_avenger
    for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['age'] > max):
            max = data["AVENGERS"][i]['age']
            oldest_avenger = data["AVENGERS"][i]
    # Return all info of the oldest avenger
    return oldest_avenger


# returns info: Thor

print(get_oldest_avenger(data))

def get_oldest(data):
    max = 0
    # Changed max= inf to max=0
    c = 0
    oldest = []
    # Created a NUll list named oldest
    for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['age'] > max):
            max = data["AVENGERS"][i]['age']
            oldest = data["AVENGERS"][i]

    for i in data["DC"]:
        if (data["DC"][i]['age'] > max):
            max = data["DC"][i]['age']
            oldest = data["DC"][i]

        if data["DC"][i]['age'] == max:
            oldest[c] = data["DC"][i]
            c += 1
    # Return all info of the oldest superheroes
    # Return all info of the oldest superheroes
    return oldest


print(get_oldest(data))

def get_total_points(data):
    total_points = {}
    for i in data["AVENGERS"]:
        key = data["AVENGERS"][i]["name"]
        total_points[key] = 0
        for j in data["AVENGERS"][i]['points']:
            total_points[key] += data["AVENGERS"][i]['points'][j]
    for i in data["DC"]:
        # Changed DCU to DC
        key = data["DC"][i]["name"]
        total_points[key] = 0
        for j in data["DC"][i]['points']:
            total_points[key] += data["DC"][i]['points'][j]
    # Return a dictionary
    # Key: superhero name
    # Value: total points
    return total_points


# returns info: Dict of superhero name and total points
print(get_total_points(data))


def get_more_than_average(data):
    more_than_average = []
    # changed () to []
    avg_mcu = 0
    avg_dc = 0
    for i in data["AVENGERS"]:
        avg_mcu += data["AVENGERS"][i]["points"]["stealth"]
    avg_mcu = avg_mcu / len(data["AVENGERS"])
    for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['points']['stealth'] > avg_mcu):
            more_than_average.append(data["AVENGERS"][i])
    # Used append funtion instead of assinging values to the list
    for i in data["DC"]:
        avg_dc += data["DC"][i]['points']['strength']
    avg_dc = avg_dc / len(data["DC"])
    for i in data["DC"]:
        if (data["DC"][i]['points']['strength'] > avg_dc):
            more_than_average.append(data["DC"][i])
    # Used append funtion instead of assinging values to the list
    '''
    Return list of superheroes with stealth more than average in MCU 
    and list of superheroes with strength more than average in DCEU
    '''
    return more_than_average


print(get_more_than_average(data))


# returns info: Steve Rogers and Superman

def get_names(data):
    names = []
    for i in data["AVENGERS"]:
        names.append(data["AVENGERS"][i]['name'])
    # Changed insert to append and gave correct indexing for names
    for j in data["DC"]:
        names.append(data["DC"][j]['name'])
    # Changed insert to append and gave correct indexing for names
    # Return a list of superhero names
    return names


print(get_names(data))
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and
