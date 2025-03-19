# use 'bar' to generate a figure
# use 'title' to set a title
# set labels for x and y axis 
# set x ticks, it is not int
# show the figure

import matplotlib.pyplot as plt

usage = {"JavaScript":62.3,"HTML":52.9,"Python":51.0,"SQL":51.0,"TypeScript":38.5}
print(usage)
plt.bar(usage.keys(),usage.values())
plt.title(" the percentage of developers who use the top 5 programming languages globally as of February 2024")
plt.xlabel("language")
plt.ylabel("users(percentage)")
plt.xticks(range(5),usage.keys())
plt.legend()
plt.show()

# get the language that need to check
# print its percentage. if not exist, print not found

x=input("the language provided:")
print(usage.get(x,"not found"))