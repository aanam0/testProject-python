class Animal:

    def __init__(self, name, animal_type, size):
        self.name = name
        self.type = animal_type
        self.size = size
        self.activities = []

    def introduce(self):
        print(f"Hi! I'm {self.name}. I'm a {self.size} {self.type}!")

    def add_activity(self, activity):
        self.activities.append(activity)

    def state_activities(self):
        print("\tHere is a list of my activities: ")
        if not self.activities: print("\t\tNone")
        for i in self.activities:
            print(f"\t\t{i}")


class Bear(Animal):

    def __init__(self, name, animal_type, size, hibernating):
        super().__init__(name, animal_type, size)
        self.hibernating = hibernating

    def do_hibernate(self):
        self.hibernating = True
        print("Going into hibernation. Zzz...")

    def wake_up(self):
        self.hibernating = False
        print("What a great nap!")

    def introduce(self):
        if not self.hibernating:
            super().introduce()
        else:
            print("Zzz...")


