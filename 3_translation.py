# Ex 3
# Pgm that reads DNA sequence and returns the protein sequence

# Dictionnary for the genetic code
gencode = {}
with open ('gencode.txt', 'r') as geneticcode:
    for line in geneticcode:
        cod = line [:3]
        ami = line [8:9]
        gencode [cod] = ami

# Opening sequence file
with open ('seq1.txt', 'r') as seq:
    seq = seq.read()

# Sequence > list of nucleotides
seq_list = list(seq)

# Filter if any non-nucleotide character
new_seq = []
for i in seq_list:
    if i == 'G' or i == 'C' or i == 'T' or i == 'A':
        new_seq.append (i)
seq_list = new_seq

# Putting the sequence back in the str
seq = ''.join (seq_list)


# Splitting the str 3 nt by 3 nt = generating the codons
# also filtering any str that is not 3 nt

# Reading frame 1
n = 3
codons_1 = []
for i in range (0, len(seq), n):
    cod = seq [i:i+n]
    if len(cod) == 3:
        codons_1.append (cod)

# Reading frame 2
n = 3
codons_2 = []
for i in range (1, len(seq), n):
    cod = seq [i:i+n]
    if len(cod) == 3:
        codons_2.append (cod)

# Reading frame 3
n = 3
codons_3 = []
for i in range (2, len(seq), n):
    cod = seq [i:i+n]
    if len(cod) == 3:
        codons_3.append (cod)


# Looking up in the genetic code dictionnary the amino acid for each codons

# RF1
protlist_1 = []
for i in codons_1:
    aa = gencode [i]
    protlist_1.append (aa)

prot_1 = ''.join (protlist_1)

# RF2
protlist_2 = []
for i in codons_2:
    aa = gencode [i]
    protlist_2.append (aa)

prot_2 = ''.join (protlist_2)

# RF3
protlist_3 = []
for i in codons_3:
    aa = gencode [i]
    protlist_3.append (aa)

prot_3 = ''.join (protlist_3)

# Print nicely the three protein sequences
print "Reading frame 1:", prot_1
print "Reading frame 2:", prot_2
print "Reading frame 3:", prot_3
