"""AI Self-Driving Cars

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nDlUeY01Y0vBQrczzwFPRzJdEReM9TZg
"""

import random

class SelfDrivingCar:
    def __init__(self):
        self.position = 0
        self.speed = 0

    def perceive_environment(self, obstacles):
        # AI perceives environment, e.g., through sensors
        if obstacles:
            return True
        else:
            return False

    def make_decision(self, obstacles):
        if self.perceive_environment(obstacles):
            # If obstacles detected, decide to slow down or change direction
            self.speed -= 1
            print("Obstacle detected! Slowing down...")
        else:
            # Otherwise, continue driving forward
            self.speed = min(5, self.speed + 1)

    def move(self):
        # Move the car forward based on its speed
        self.position += self.speed

    def display_status(self):
        print(f"Current position: {self.position}, Speed: {self.speed}")

def simulate_self_driving_car():
    car = SelfDrivingCar()
    obstacles = False  # Simulate no obstacles initially

    for _ in range(10):  # Simulate 10 time steps
        car.make_decision(obstacles)
        car.move()
        car.display_status()

        # Simulate random occurrence of obstacles
        obstacles = random.choice([True, False])

simulate_self_driving_car()
