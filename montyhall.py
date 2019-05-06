import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm
from numpy import arange

def run_cycle(num_doors, decision_threshold):
        num_doors = int(num_doors)
        decision_threshold = int(decision_threshold)
        # generate scenario where Monty has opened all but two doors, one of which contains the car
        def gen_monty(n):
                doors = np.zeros(n)
                car_index = rnd.randint(0,n)
                doors[car_index] = 1
                
                initial_choice = rnd.randint(0,n)
                doors[initial_choice] = 2

                other_door = car_index

                if initial_choice == car_index:
                        while other_door == initial_choice:
                                other_door = rnd.randint(0,n)
                
                return initial_choice, other_door, car_index

        success = 0
        trials = 2500

        # simulation cycle
        for x in range(trials):
                initial_choice, other_door, car_index = gen_monty(num_doors)
                # use threshold to make decision
                if rnd.randint(100) > decision_threshold:
                        #switch decision
                        if other_door == car_index:
                                success += 1
                else:
                        #stay decision
                        if initial_choice == car_index:
                                success += 1

        # calculate results
        rate = (success / trials) * 100
        #print('Success rate of Monty Hall switching strategy: %.3f %%' %(rate))

        return rate

x = np.linspace(0,100, 101)
y = np.linspace(2,25, 24)
Z = np.zeros((24, 101))
X,Y = np.meshgrid(x,y)

# loop through different decision thresholds
for i in range(101):
# loop through different door numbers
        for j in range(2,24):
                Z[j][i] = run_cycle(j,i)

fig = plt.figure(figsize = (20,10))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z)
#plt.annotate('2/3 chance of winning with 3 doors', xy=(3,66), xytext=(15,50),arrowprops = dict(facecolor= 'black', shrink = 0.04),)
plt.title('Monty Hall Visualization')
ax.set_xlabel('% chance of sticking with first door')
ax.set_zlabel('Success rate of switching strategy')
ax.set_ylabel('Starting # of doors')
plt.show()
