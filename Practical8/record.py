# make the patients class
# define the name, age, date, history as the feature of patients
# define the function that print these data in one line
class patients():
    def __init__(self,name,age,date,history):
        self.name=name
        self.age=age
        self.date=date
        self.history=history
    def print(self):
        print('name:'+self.name+'.  age:'+self.age+'.  date of latest admission:'+self.date+'.  medical history:'+self.history+'.')

# get input for the patient data
name=input('enter the name:')
age=input('enter the age:')
date=input('enter the date of latest admission:')
history=input('enter the medical history:')

# creat object for the patient who belong to patient class
# print the details
x=patients(name,age,date,history)
x.print()


# here is an example
# input Sha Rui
# input 18
# input 2025.01.01
# input None
# print 'name:Sha Rui.  age:18.  date of latest admission:2025.01.01.  medical history:None.'