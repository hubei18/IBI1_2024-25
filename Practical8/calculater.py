# calculate volumn(ml) by weight(kg) and strength(mg/ml)
def calculate(weight, strength):
    volumn=weight*15/strength
    return volumn

# get input for weight
# examine whether the weight is between 10 and 100 kg
# if not, input again
while True:
    weight=int(input('input weight in kg (should be between 10 and 100kg):'))
    if 10<=weight<=100:
        break
    print("weight wrong. input again")

# get input for strength
# examine whether the strength is input correctly
# if not, input again
data=[24,50]
while True:
    strength=int(input('input 0 for 120 mg/5 ml or 1 for 250 mg/5 ml:'))
    if strength in [1,0]:
        strength=data[strength]
        break
    print('strength wrong. input again')

# call the 'calculate' function to get the volumn
# print the result
volumn=calculate(weight,strength)
print('the volumn should be',volumn,'ml')



# here is the example

# 1.
# input 100 and 0
# print 'the volumn should be 62.5 ml'

# 2.
# input 110
# print 'weight wrong. input again'
# input 120
# print 'weight wrong. input again'
# input 1
# print 'weight wrong. input again'
# input 20
# input 2
# print 'strength wrong. input again'
# input 0
# print 'the volumn should be 12.5 ml'