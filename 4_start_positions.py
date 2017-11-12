# Ex 4
# Pgm that reads DNA sequence and returns position of the start codons

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


# Scanning the three reading frames 3 by 3 to look for start codons
# and return the positions in lists

# Reading frame 1
starts_1 = []
n = 3
for i in range (0, len(seq), n):
    cod = seq [i:i+n]
    if cod == 'ATG':
        starts_1.append(i+1)

# Reading frame 2
starts_2 = []
n = 3
for i in range (1, len(seq), n):
    cod = seq [i:i+n]
    if cod == 'ATG':
        starts_2.append(i+1)

# Reading frame 3
starts_3 = []
n = 3
for i in range (2, len(seq), n):
    cod = seq [i:i+n]
    if cod == 'ATG':
        starts_3.append(i+1)

# Print the results

print "Positions of start codons in reading frame 1:", starts_1
print "Positions of start codons in reading frame 2:", starts_2
print "Positions of start codons in reading frame 3:", starts_3
