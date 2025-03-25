# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# set variables for susceptible, infected, and recovery
# set variables for beta and gamma
# set variable for times
# set loop to show time flow
    # calculate recovery
    # calculate infected
    # record them into the variables for susceptible, infected, and recovery
susceptible = [9999]
infected = [1]
recovery = [0]
beta = 0.3
gamma = 0.05
times = 1000
for time in range(1,times+1):
    rate = infected[time-1]/10000*beta
    i=sum(np.random.choice(range(2),susceptible[time-1],p=[1-rate,rate]))
    r=sum(np.random.choice(range(2),infected[time-1],p=[1-gamma,gamma]))
    susceptible.append(susceptible[time-1]-i)
    infected.append(infected[time-1]+i-r)
    recovery.append(recovery[time-1]+r)

# draw plot
plt.plot(range(times+1),susceptible,color='b',label='susceptible')
plt.plot(range(times+1),infected, color='r',label='infected')
plt.plot(range(times+1),recovery, color='g',label='recovery')
plt.title("SIR model")
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend()
plt.show()