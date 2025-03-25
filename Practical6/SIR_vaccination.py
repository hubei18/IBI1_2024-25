# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# set variables for beta, gamma and times
beta = 0.3
gamma = 0.05
times = 1000

# set loop to show time flow
    # calculate recovery
    # calculate infected
    # record them into the variables for susceptible, infected, and recovery
def aftertime(susceptible,infected,recovery):
    for time in range(1,times+1):
        rate = infected[time-1]/10000*beta
        i=sum(np.random.choice(range(2),susceptible[time-1],p=[1-rate,rate]))
        r=sum(np.random.choice(range(2),infected[time-1],p=[1-gamma,gamma]))
        susceptible.append(susceptible[time-1]-i)
        infected.append(infected[time-1]+i-r)
        recovery.append(recovery[time-1]+r)
    return susceptible,infected,recovery

# get vaccination rate
# loop for vaccination rate
# recovery increase and susceptible decrease
# set variables for susceptible, infected and recovery
vaccine=range(0,110,10)
for j in vaccine:
    recovery=[int(9999*j/100)]
    susceptible=[9999-int(9999*j/100)]
    infected=[1]
    susceptible,infected,recovery=aftertime(susceptible,infected,recovery)
    plt.plot(range(times+1),infected, color=cm.viridis(j*4),label=f'{j}%')
plt.title('SIR model with different vaccination rates')
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend()
plt.show()