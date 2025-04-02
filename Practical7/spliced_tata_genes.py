import re

# get input
while True:
    splice= input('input the splice donor: ')
    if splice in ['GTAG','GCAG','ATAC']:
        break
    print('WRONG!!! input again')

# open the file
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as file:

    # initialze data
    namelist=[]
    sequencelist=[]
    typelist=[]
    timeslist=[]
    gene_name=''
    sequence=''
    type=0
    times=0

    # loop through each line 
    for line in file: 

        # fine the first line of each sequence
        # add the data of each gene to list
        # initial data for next gene
        if line[0]=='>':
            if re.search(r'TATA[AT]A[AT]',sequence) and re.search(splice,sequence): # add the condition that splice gene should be in the seequence
                type=1
                times=len(re.findall(r'TATA[AT]A[AT]',sequence))
            namelist.append(gene_name)
            sequencelist.append(sequence)
            typelist.append(type)
            timeslist.append(times)
            sequence=''
            gene_name=re.findall(r'gene:\S+\s',line)
            gene_name=gene_name[0][5:-1]
            type=0
            times=0 # record the time that TATAWAW appear
            continue

        # combine the sequence
        sequence+=line.strip()
    if re.search(r'TATA[AT]A[AT]',sequence) and re.search(splice,sequence):
        type=1
        times=len(re.findall(r'TATA[AT]A[AT]',sequence))
    namelist.append(gene_name)
    sequencelist.append(sequence)
    typelist.append(type)
    timeslist.append(times)

# creat new file
# all sequence in one line
with open(f'{splice}_spliced_genes.fa','w') as newfile:
    for i in range(1,len(typelist)):
        if typelist[i]==1:
            newfile.write(f'>{namelist[i]}, number={timeslist[i]}\n')
            newfile.write(f'{sequencelist[i]}\n')