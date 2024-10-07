import matplotlib.pyplot as plt
import numpy as np
import math
velocities = []
times = []
accelerations = []
def ask():
    grav = float(input("What do you want your gravitational acceleration to be? (Enter a number greater than 0: "))
    if (grav > 0):
        i1 = float(input("what do you want your initial velocity to be for line1?: "))
        i2 = float(input("what do you want your initial velocity to be for line2: "))
        if (i1 < 1000 and i2 < 1000):
            step_size1 = float(input("what do you want your step size for line 1 to be? "))
            step_size2 = float(input("what do you want your step size for line 2 to be? "))

            if (step_size1 > 0) and (step_size2 > 0):
                total_time1 = float(input("what do you want your total time for line 1 to be? "))
                total_time2 = float(input("what do you want your total time for line 2 to be? "))
                if (total_time1 > 0) and (total_time2 > 0):
                    drag_coefficient1 = float(input("what do you want your drag coefficient for line 1 to be? "))
                    drag_coefficient2 = float(input("what do you want your drag coefficient for line 2 to be? "))
                    if (drag_coefficient1 > 0) and (drag_coefficient2 > 0):
                        print("Proceeding...")
                        return grav, i1, i2, step_size1, step_size2, total_time1, total_time2, drag_coefficient1, drag_coefficient2
                    else:
                        print("wrong, try again")
                        ask()
            else:
                print("wrong, try again")
                ask()
        else:
            print("wrong, try again")
            ask()
    else:
        print("wrong, try again")
        ask()

class Line:
    def __init__(self, gravitational_acceleration, initial_velocity, step_size, total_time, drag_coefficient, number):
        self.gravitational_acceleration = gravitational_acceleration
        self.initial_velocity = initial_velocity
        self.step_size = step_size
        self.total_time = total_time
        self.drag_coefficient = drag_coefficient
        self.number = number
    def __str__(self):
        return f"Gravitational Acceleration: {self.gravitational_acceleration}, Initial Velocity: {self.initial_velocity}, Step size: {self.step_size}, Total time: {self.total_time}, Drag Coefficient: {self.drag_coefficient}"
    def find_data(self):
        velocities.append([])
        times.append([])
        accelerations.append([])

        velocities[self.number-1].append(self.initial_velocity)

        for i in range(int(self.total_time // self.step_size)):
            velocities[self.number-1].append(velocities[self.number-1][i]+self.step_size*(self.gravitational_acceleration-(self.drag_coefficient*velocities[self.number-1][i])))
            times[self.number-1].append(i*self.step_size)
        for i in range(int(self.total_time // self.step_size)):
            accelerations[self.number-1].append((velocities[self.number-1][i+1]-velocities[self.number-1][i])/self.step_size)
grav, i1, i2, step_size1, step_size2, total_time1, total_time2, drag_coefficient1, drag_coefficient2 = ask()
line1 = Line(grav, i1, step_size1, total_time1, drag_coefficient1, 1)
line2 = Line(grav, i2, step_size2, total_time2, drag_coefficient2, 2)

def plot(number):
    plt.figure(figsize=(10, 10))
    plt.subplot(2, 1, 1)
    plt.plot(times[number - 1], velocities[number - 1][:-1], label=f'Line {number} Velocity')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title(f'Velocity vs Time for Line {number}')
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.plot(times[number - 1], accelerations[number - 1], label=f'Line {number} Acceleration', color='orange')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s^2)')
    plt.title(f'Acceleration vs Time for Line {number}')
    plt.legend()
    plt.tight_layout()
    plt.show()
def main():
    print(line1)
    print(line2)
    line1.find_data()
    line2.find_data()
    print(velocities)
    print(times)
    print(accelerations)
    plot(1)
    plot(2)
if __name__ == "__main__":
    main()
