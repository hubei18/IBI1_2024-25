# What does this piece of code do?
# Answer: how many times it need to match first_n with second_n

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
first_n=1
second_n=0
while first_n != second_n:
	progress+=1
	first_n = randint(1,6)
	second_n = randint(1,6)
print(progress)

