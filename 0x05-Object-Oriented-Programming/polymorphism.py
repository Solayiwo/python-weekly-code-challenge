#!/usr/bin/python3


class Car():
    def move(self):
        res = "The car is driving."
        return res

class Plane():
    def move(self):
        res = "The plane is flying."
        return res

class Boat():
    def move(self):
        res = "The boat is sailing."
        return res


for object in [Car(), Plane(), Boat()]:
    print(object.move())

