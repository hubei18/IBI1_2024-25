# try something here
codon_table = {
'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp',
'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
}

codonbiascount = {
    'Phe': {'UUU': 0, 'UUC': 0},
    'Leu': {'UUA': 0, 'UUG': 0, 'CUU': 0, 'CUC': 0, 'CUA': 0, 'CUG': 0},
    'Ser': {'UCU': 0, 'UCC': 0, 'UCA': 0, 'UCG': 0, 'AGU': 0, 'AGC': 0},
    'Tyr': {'UAU': 0, 'UAC': 0},
    'Stop': {'UAA': 0, 'UAG': 0, 'UGA': 0},
    'Cys': {'UGU': 0, 'UGC': 0},
    'Trp': {'UGG': 0},
    'Pro': {'CCU': 0, 'CCC': 0, 'CCA': 0, 'CCG': 0},
    'His': {'CAU': 0, 'CAC': 0},
    'Gln': {'CAA': 0, 'CAG': 0},
    'Arg': {'CGU': 0, 'CGC': 0, 'CGA': 0, 'CGG': 0, 'AGA': 0, 'AGG': 0},
    'Ile': {'AUU': 0, 'AUC': 0, 'AUA': 0},
    'Met': {'AUG': 0},
    'Thr': {'ACU': 0, 'ACC': 0, 'ACA': 0, 'ACG': 0},
    'Asn': {'AAU': 0, 'AAC': 0},
    'Lys': {'AAA': 0, 'AAG': 0},
    'Val': {'GUU': 0, 'GUC': 0, 'GUA': 0, 'GUG': 0},
    'Ala': {'GCU': 0, 'GCC': 0, 'GCA': 0, 'GCG': 0},
    'Asp': {'GAU': 0, 'GAC': 0},
    'Glu': {'GAA': 0, 'GAG': 0},
    'Gly': {'GGU': 0, 'GGC': 0, 'GGA': 0, 'GGG': 0}
}

sequence=input("input")
for i in range(0,len(sequence)-2,3):
    if i+3>len(sequence):
        break
    codon=sequence[i:i+3]
    codonbiascount[codon_table[codon]][codon]+=1
    if codon_table[codon]=="Stop":
        break
for i in codonbiascount:
    dicts=codonbiascount[i]
    total=0
    for j in dicts:
        total+=dicts[j]
    if total==0:
        continue
    for j in dicts:
        dicts[j]=round(dicts[j]/total,2)
for i in codonbiascount:
    print(i,codonbiascount[i])