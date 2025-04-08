# define the function
# input is the DNA sequence and the sequence recognised by the restriction enzyme
# return the position of cut sites
# examine the DNA sequence and find  the first amino acid that matchs
def find(sequence, enzyme):
    length=len(enzyme)
    position=[]
    i=0
    while i <=len(sequence)-length:
        data=sequence[i:i+length]
        if data==enzyme:
            position.append(i)
            i+=length+1
            continue
        i+=1
    return position

# definethe function
# check whether the sequence wass composed of only canoical nucleotides
def check(sequence):
    for i in sequence:
        if not i in ['A','G','C','T']:
            return False
    return True

# get input for DNA sequence
# check whether the sequence wass composed of only canoical nucleotides
while True:
    DNA=input('enter the DNA sequence:')
    if check(DNA):
        break
    print('wrong DNA sequence. input again')

# get input for enzyme
# check whether the sequence wass composed of only canoical nucleotides
while True:
    enzyme=input('enter the enzyme recognised sequence:')
    if check(enzyme):
        break
    print('wrong sequence. input again')

# call the 'find' function to find all the position that was cut
# print the result
position=find(DNA,enzyme)
print(position)