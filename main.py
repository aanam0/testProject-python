from Animal.Animal import *
import csv


def generate_animals():
    animals = {}

    data = open("data/animals.csv", "r")

    # open file, split the file so each line is 1 item of a list
    # skip the first line

    data_input = data.read().splitlines()[1:]
    activities = open("data/activities.csv", "r")
    activity_input = activities.read().splitlines()[1:]

    # print(data_input)
    # print(activity_input)

    for i in data_input:
        # split the CSV format
        str_split = i.split(',')
        a = Animal(str_split[0], str_split[1], str_split[2])
        animals[str_split[0]] = a

    for i in activity_input:
        str_split = i.split(',')
        animals[str_split[0]].add_activity(str_split[1])

    for a in animals.values():
        a.introduce()
        a.state_activities()


def csv_test():
    # Open the data and activities files using csv library
    file = open("data/animals.csv", "r")
    animal_data = csv.reader(file, delimiter=',', doublequote=True, quotechar="'")

    # this does the same as above with less params
    file2 = open("data/activities.csv", "r")
    activity_data = csv.reader(file2)

    animals = {}

    # Skip the headers
    # Create an animal obj with data from csv.
    # Add each animal to a dict with the 'Name' as the key
    next(animal_data)
    for data in animal_data:
        animal = Animal(data[0], data[1], data[2])
        animals[data[0]] = animal

    # Skip headers
    # Create for each activity, add to the animal it belongs to
    # Get the correct animal obj from dict using key 'Name' then run addActivity()
    next(activity_data)
    for activity in activity_data:
        animals[activity[0]].add_activity(activity[1])

    # Iterate over all animals and run introduce + stateActivities
    for a in animals.values():
        a.introduce()
        a.state_activities()

    # Close files (seems like it's something you're supposed to do)
    file.close()
    file2.close()


generate_animals()
print("=========================================")
csv_test()
