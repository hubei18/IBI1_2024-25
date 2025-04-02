import re 

# open the file
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as file :

    # initialize the variables
    namelist=[]
    sequencelist=[]
    typelist=[]
    gene_name=''
    sequence=''
    type=0

    # loop through each line 
    for line in file:

        # fine the first line of each sequence
        # add the data of each gene to list
        # initial data for next gene
        if line[0]=='>':
            if re.search(r'TATA[AT]A[AT]',sequence):
                type=1
            namelist.append(gene_name)
            sequencelist.append(sequence)
            typelist.append(type)
            sequence=''
            gene_name=re.findall(r'gene:\S+\s',line)
            gene_name=gene_name[0][5:-1]
            type=0
            continue

        # conbine each line into sequence
        sequence+=line.strip()
    if re.search(r'TATA[AT]A[AT]',sequence):
        type=1
    namelist.append(gene_name)
    sequencelist.append(sequence)
    typelist.append(type)

# creat new file 
# add data to new file 
# 60 bases per line
with open('tata_genes.fa','w') as newfile:
    for i in range(1,len(typelist)):
        if typelist[i]==1:
            newfile.write(f'>{namelist[i]}\n')
            sequence=sequencelist[i]
            for j in range(0,len(sequence),60):
                newfile.write(f'{sequence[j:j+60]}\n')

