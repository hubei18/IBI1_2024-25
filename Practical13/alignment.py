# import necessary library
# import the BLOSUM62 matrix
from Bio.Align import substitution_matrices
blosum62 = substitution_matrices.load("BLOSUM62")

# read the .fasta file
def read(filename):
    sequence=''
    with open(filename,'r') as file:
        for line in file:
            if line[0]!='>':
                sequence+=line.strip()
    return sequence

# calculate the percentage of identical amino acid
def identity(seq1,seq2):
    distance=sum(c1==c2 for c1,c2 in zip(seq1,seq2))
    return distance/len(seq1)*100

# calculate the alignment score based on BLOSUM62
def score(seq1,seq2):
    return sum(blosum62[c1][c2] for c1,c2 in zip(seq1,seq2))

# get the input
human=read('P04179.fasta.txt')
mouse=read('P09671.fasta.txt')
random=read('random.fasta')

# print out the results
print(f'For human and mouse, the alignment score is {score(human,mouse)}, the percentage of identical amino acids is {identity(human,mouse)}')
print(f'For human and random, the alignment score is {score(human,random)}, the percentage of identical amino acids is {identity(human,random)}')
print(f'For random and mouse, the alignment score is {score(random,mouse)}, the percentage of identical amino acids is {identity(random,mouse)}')

