class Animal:

    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size
        self.activities = []

    def introduce(self):
        print(f"Hi! I'm {self.name}. I'm a {self.size} {self.type}!")

    def add_activity(self, activity):
        self.activities.append(activity)

    def state_activities(self):
        print("\tHere is a list of my activities: ")
        if not self.activities: print ("\t\tNone")
        for i in self.activities:
            print(f"\t\t{i}")