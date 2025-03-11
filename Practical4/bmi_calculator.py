# get weight and height
# calculate BMI
# compare BMI with 18.5 and 30
# give result 

mass=int(input("mass"))
height=int(input("height"))
bmi=mass/height**2
if bmi < 18.5:
    print("thin")
elif bmi > 30:
    print("fat")
else:
    print("health")