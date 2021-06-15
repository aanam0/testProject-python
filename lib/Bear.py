from lib.Animal import *


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
