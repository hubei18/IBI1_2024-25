# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# set variables for beta, gamma and times
beta = float(input('beta'))
gamma = float(input('gamma'))
times = 100

# make population map
size=int(input('size'))
population=np.zeros((size,size))

# create outbreak
outbreak=np.random.choice(range(size),2)
population[outbreak[0],outbreak[1]]=1

# define function for recover, input is the position
def recover(x,y):
    global population
    population[x][y]+=np.random.choice(range(2),p=[1-gamma,gamma])

# define function for infect, input is the position
def infect(x,y):
    global population
    for i in range(-1,2):
        if x+i<0 or x+i>size-1:
            continue
        for j in range(-1,2):
            if y+j<0 or y+j>size-1:
                continue
            if population[x+i][y+j]==0:
                population[x+i][y+j]+=np.random.choice(range(2),p=[1-beta,beta])

# set variable for save_data
# add initial time to saved data 
saved=[(0,population.copy())]

# loop for times
# go through each person and check infect and recover
# draw figure per ten time
for time in range(1,times+1):
    now=population.copy()
    for m in range(size):
        for n in range(size):
            if now[m][n]==1:
                infect(m,n)
                recover(m,n)
    #if time in [10,50,100]:
    if time % 20 == 0:
        saved.append((time,population.copy()))

# draw plot with 6 subplots
fig,axs=plt.subplots(2,3,dpi=150)
axs=axs.ravel()
for index,(time,present) in enumerate(saved):
    ax=axs[index]
    ax.imshow(present,cmap='viridis',interpolation='nearest')
    ax.set_title(f'{time} days')
    ax.axis('off')
plt.tight_layout()
plt.show()