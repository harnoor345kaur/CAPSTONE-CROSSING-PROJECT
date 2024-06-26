COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
from random import randint

class CarManager():
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        random_chance = randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(COLORS[randint(0,5)])
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setpos((300,randint(-250,250)))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)






