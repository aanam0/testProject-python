import csv
from lib.Bear import *


def generate_animals():
    # dictionary
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
        # CSV format: name,type,size
        str_split = i.split(',')
        a = Animal(str_split[0], str_split[1], str_split[2])

        # add to dictionary
        animals[str_split[0]] = a

    for i in activity_input:
        str_split = i.split(',')
        animals[str_split[0]].add_activity(str_split[1])

    for a in animals.values():
        a.introduce()
        a.state_activities()


def generate_animals_csv():
    # Open the data and activities files using csv library
    file_animals = open("data/animals.csv", "r")
    animal_data = csv.reader(file_animals, delimiter=',', doublequote=True, quotechar="'")

    # this does the same as above with less params
    file_activities = open("data/activities.csv", "r")
    activity_data = csv.reader(file_activities)

    animals = {}

    # Create an animal obj with data from csv.
    # Add each animal to a dict with the 'Name' as the key
    next(animal_data)  # Skip the headers
    for data in animal_data:
        animal = Animal(data[0], data[1], data[2])
        animals[data[0]] = animal

    # Create for each activity, add to the animal it belongs to
    # Get the correct animal obj from dict using key 'Name' then run addActivity()
    next(activity_data)  # Skip the headers
    for activity in activity_data:
        animals[activity[0]].add_activity(activity[1])

    # Iterate over all animals and run introduce + stateActivities
    for a in animals.values():
        a.introduce()
        a.state_activities()

    # Close files (seems like it's something you're supposed to do)
    file_animals.close()
    file_activities.close()


def bear_test():
    name = "Paddie"
    animal_type = "Polar Bear"
    size = "small"
    hibernating = False

    b = Bear(name, animal_type, size, hibernating)
    b.introduce()
    b.do_hibernate()
    b.introduce()


generate_animals_csv()
bear_test()
