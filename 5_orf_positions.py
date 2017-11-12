# Ex 5
# Pgm that reads DNA sequence and returns positions (Start, Stop) of the ORF

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

###################################################################
# Scanning the three reading frames 3 by 3 to look for start codons
# and return the positions in lists
# Generate the ORFs = pairs of start/stop

# Reading frame 1
print 'Reading frame 1'
starts_1 = []
stops_1 = []
n = 3
for i in range (0, len(seq), n):
    cod = seq [i:i+n]
    if cod == 'ATG':
        starts_1.append(i+1)
    if cod == 'TAA' or cod == 'TAG' or cod == 'TGA':
        stops_1.append (i+1)

# Generate the pairs
for start in starts_1:
    for stop in stops_1:
        if stop > start:
            print 'ORF:', start, '>', stop
print ''

#################
# Reading frame 2
print 'Reading frame 2'
starts_2 = []
stops_2 = []
n = 3
for i in range (1, len(seq), n):
    cod = seq [i:i+n]
    if cod == 'ATG':
        starts_2.append(i+1)
    if cod == 'TAA' or cod == 'TAG' or cod == 'TGA':
        stops_2.append (i+1)

# Generate the pairs
for start in starts_2:
    for stop in stops_2:
        if stop > start:
            print 'ORF:', start, '>', stop
print ''

#################
# Reading frame 3
print 'Reading frame 3'
starts_3 = []
stops_3 = []
n = 3
for i in range (2, len(seq), n):
    cod = seq [i:i+n]
    if cod == 'ATG':
        starts_3.append(i+1)
    if cod == 'TAA' or cod == 'TAG' or cod == 'TGA':
        stops_3.append (i+1)

# Generate the pairs
for start in starts_3:
    for stop in stops_3:
        if stop > start:
            print 'ORF:', start, '>', stop
